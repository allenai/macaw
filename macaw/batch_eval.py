import argparse
import logging
import json
import os
import sys
import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, T5Tokenizer
from transformers import logging as transformers_logging

# sys.path.append(os.path.join(os.getcwd()))

from macaw.utils import decompose_slots, save_json, make_input_string
from macaw.eval_utils import collate_scores, score_prediction

#######################################
#
# Script for batch prediction/evaluation with Macaw. Sample usage:
# $ python -m macaw.batch_eval --model_name_or_path allenai/macaw-large --output_dir output --input_files inputs.jsonl --add_metrics
#
# Sample input file lines:
#
# Basic QM->A angle:
# {"id":"ARCCH_Mercury_7103565","question":"High-pressure systems stop air from rising into the colder regions of the atmosphere where water can condense. What will most likely result if a high-pressure system remains in an area for a long period of time?","mcoptions":"(A) fog (B) rain (C) drought (D) tornado","answer":"drought","angle":[["question","mcoptions"],["answer"]]}
# Also include generation scores for each multiple-choice answer:
# {"id":"ARCCH_Mercury_7103565","question":"High-pressure systems stop air from rising into the colder regions of the atmosphere where water can condense. What will most likely result if a high-pressure system remains in an area for a long period of time?","mcoptions":"(A) fog (B) rain (C) drought (D) tornado","answer":"drought","angle":[["question","mcoptions"],["answer"]],"explicit_outputs":["fog","rain","drought","tornado"]}
# Alternate QA->M angle:
# {"id":"ARCCH_Mercury_7103565","question":"High-pressure systems stop air from rising into the colder regions of the atmosphere where water can condense. What will most likely result if a high-pressure system remains in an area for a long period of time?","mcoptions":"(A) fog (B) rain (C) drought (D) tornado","answer":"drought","angle":[["question","answer"],["mcoptions"]]}
#
# The output predictions.jsonl has each prediction, as well metrics if gold output is part of input
# The metrics.json file contains aggregated metrics per angle
#
#######################################

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
transformers_logging.set_verbosity_info()


def run_model_with_outputs(args, model, tokenizer, batch_instances):
    with torch.no_grad():
        input_strings = [x['input'] for x in batch_instances]
        output_strings = [x['output'] for x in batch_instances]
        inputs_dict = tokenizer.batch_encode_plus(input_strings, max_length=args.max_tokens, return_tensors="pt",
                                                  padding=True, truncation=True)
        outputs_dict = tokenizer.batch_encode_plus(output_strings, max_length=args.max_length, return_tensors="pt",
                                                  padding=True, truncation=True)
        input_ids = inputs_dict.input_ids.to(args.device)
        attention_mask = inputs_dict.attention_mask.to(args.device)
        output_ids = outputs_dict.input_ids.to(args.device)
        # Special value for labels to be ignored
        output_ids[output_ids[:, :] == tokenizer.pad_token_id] = -100
        res = model(input_ids, attention_mask=attention_mask, labels=output_ids, return_dict=True)
        res_softmax = torch.softmax(res.logits, dim=2)

        # Flip back to valid token ids
        output_ids[output_ids[:, :] == -100] = tokenizer.pad_token_id
        token_probs = torch.gather(res_softmax, 2, output_ids.unsqueeze(-1)).squeeze(-1)
        # set probability for padded tokens to 1
        token_probs[output_ids[:, :] == tokenizer.pad_token_id] = 1
        total_probs = torch.prod(token_probs, dim=1)
        output_tokens = [tokenizer.convert_ids_to_tokens(x) for x in output_ids]
        all_res = batch_instances.copy()
        for idx, instance in enumerate(all_res):
            tokens_with_prob = [(token, prob.item()) for token, prob in zip(output_tokens[idx], token_probs[idx]) if token != "<pad>"]
            prediction = {'output_text': instance['output_text'], 'output_prob': total_probs[idx].item(), 'token_probs': tokens_with_prob}
            instance['prediction'] = prediction
    return all_res


def run_generate(args, model, tokenizer, batch_instances):
    with torch.no_grad():
        input_strings = [x['input'] for x in batch_instances]
        inputs_dict = tokenizer.batch_encode_plus(input_strings, max_length=args.max_tokens, return_tensors="pt",
                                                  padding=True, truncation=True)
        input_ids = inputs_dict.input_ids.to(args.device)
        attention_mask = inputs_dict.attention_mask.to(args.device)
        outputs = model.generate(
            input_ids,
            attention_mask=attention_mask,
            num_beams=args.num_beams,
            min_length=args.min_length,
            max_length=args.max_length,
            early_stopping=False,
            #num_return_sequences=args.num_return_sequences,
            #no_repeat_ngram_size=args.no_repeat_ngram_size,
            do_sample=args.do_sample > 0,
            top_p=args.top_p,
            top_k=args.top_k,
            temperature=args.temperature
        )
        answers = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        all_res = batch_instances.copy()
        for idx, instance in enumerate(all_res):
            answer = answers[idx]
            answer_slots = decompose_slots(answer)
            # add extra list to support future multi-inputs from top-n generation
            instance['output_raw_list'] = [answer]
            instance['output_slots_list'] = [answer_slots]
        return all_res


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name_or_path", default=None, type=str, required=True,
        help="Path to pretrained checkpoints or model identifier from huggingface.co/models")
    parser.add_argument("--output_dir", default=None, required=True, type=str,
                        help="Directory to store predictions.")
    parser.add_argument("--input_files", default=None, required=True, type=str,
                        help="Input files for evaluation, separated by commas")
    parser.add_argument("--n_eval", default=-1, type=int, help="Max number of instances to run per input file")
    parser.add_argument("--add_metrics", action="store_true", help="Add metrics if gold slots are available")
    parser.add_argument("--eval_batch_size", default=8, type=int,
        help="Batch size per GPU/CPU for evaluation.")
    parser.add_argument( "--num_beams", default=1, type=int,
        help="Number of beams to be used when generating answers")
    parser.add_argument("--min_length", default=1, type=int, help="Min length of the generated answers")
    parser.add_argument("--max_length", default=128, type=int, help="Max length of the generated answers")
    parser.add_argument("--max_tokens", default=512, type=int, help="Max length of input in tokens")
    parser.add_argument("--do_sample", default=0, type=int, help="Set to 1 to do output sampling")
    parser.add_argument("--top_k", default=50, type=int, help="Sample top k tokens")
    parser.add_argument("--top_p", default=1.0, type=float, help="Sample top p probability (nucleus sampling)")
    parser.add_argument("--temperature", default=1.0, type=float, help="Sampling temperature")
    parser.add_argument("--n_gpu", default=0, type=int, help="Number of GPUs to split model across")

    args = parser.parse_args()
    return args


def main(args):
    input_files = [x.strip() for x in args.input_files.split(',')]
    try:
        tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
    except:
        # All T5 tokenizers are the same, up to max length restrictions
        tokenizer = T5Tokenizer.from_pretrained("t5-11b")
    model = AutoModelForSeq2SeqLM.from_pretrained(args.model_name_or_path)
    model.eval()

    args.device = torch.device("cuda" if args.n_gpu > 0 else "cpu")

    device_map = None
    if args.n_gpu and args.n_gpu > 1:
        num_layers = model.config.num_layers
        layers_per_gpu = num_layers // args.n_gpu
        has_one_extra = args.n_gpu - (num_layers - layers_per_gpu * args.n_gpu)
        device_map = {}
        current = 0
        for n in range(args.n_gpu):
            next = current + layers_per_gpu
            if n >= has_one_extra:
                next += 1
            device_map[n] = list(range(current, next))
            current = next
        logger.info(f"Using device_map: {device_map}")
    if device_map is not None:
        model.parallelize(device_map)
    else:
        model.to(args.device)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    all_metrics_aggregated = {}
    for input_file in input_files:
        if not os.path.exists(input_file):
            raise ValueError(f"Input file {input_file} does not exist!")
        if len(input_files) == 1:
            output_file_base = "predictions.jsonl"
        else:
            input_file_base = os.path.basename(input_file)
            output_file_base = f"predictions-{input_file_base}"
        output_file = os.path.join(args.output_dir, output_file_base)
        predictions = []
        xpredictions = []

        with open(input_file, "r") as eval_file, open(output_file, "w") as preds_file:
            batch_instances = []
            xbatch_instances = []
            counter = 0
            for line in eval_file:
                if args.n_eval > 0 and counter >= args.n_eval:
                    break
                try:
                    instance_raw = json.loads(line.strip())
                except:
                    instance_raw = {"input": line.strip()}
                counter += 1
                if counter % 100 == 0:
                    logger.info(f"Processed {counter} lines.")
                angle = instance_raw.get('angle')
                explicit_outputs = instance_raw.get('explicit_outputs')
                instance = {'id': instance_raw.get('id', f'line-{counter}')}
                instance['line'] = counter
                if angle is None:
                    instance['input'] = instance_raw['input']
                else:
                    if len(angle) != 2:
                        raise ValueError(f"Invalid angle: {angle}")
                    instance['angle'] = angle
                    slots = {k:v for k,v in instance_raw.items() if k in angle[0] or k in angle[1]}
                    instance['slots'] = slots
                    input, _, angle_str = make_input_string(slots, angle)
                    instance['input'] = input
                    instance['angle_str'] = angle_str
                    if explicit_outputs is not None:
                        assert len(angle[1]) == 1
                        slot = angle[1][0]
                        for explicit_output in explicit_outputs:
                            xinstance = instance.copy()
                            output_raw = make_input_string({slot: explicit_output})[0]
                            xinstance['output'] = output_raw
                            xinstance['output_text'] = explicit_output
                            xbatch_instances.append(xinstance)
                            if len(xbatch_instances) == args.eval_batch_size:
                                xpredictions += run_model_with_outputs(args, model, tokenizer, xbatch_instances)
                                xbatch_instances = []
                batch_instances.append(instance)

                if len(batch_instances) == args.eval_batch_size:
                    predictions += run_generate(args, model, tokenizer, batch_instances)
                    # Show the first set of predictions
                    if len(predictions) == args.eval_batch_size:
                        for p in predictions:
                            logger.info(f"Sample prediction: {p}")

                    batch_instances = []
            if len(batch_instances) > 0:
                predictions += run_generate(args, model, tokenizer, batch_instances)
            if len(xbatch_instances) > 0:
                xpredictions += run_model_with_outputs(args, model, tokenizer, xbatch_instances)
            # collate instances using explicit_outputs
            xpredictions_idx = 0
            for prediction in predictions:
                explicit_output_res = []
                current_line = prediction['line']
                if args.add_metrics:
                    pred_slots = prediction['output_slots_list'][0]
                    gold_slots = prediction.get('slots', {})
                    if len(set(pred_slots.keys()).intersection(gold_slots.keys())) > 0:
                        metrics = score_prediction({"slots": pred_slots, "angle": prediction['angle']}, gold_slots)
                        prediction['metrics'] = metrics
                while xpredictions_idx < len(xpredictions) and xpredictions[xpredictions_idx]['line'] == current_line:
                    explicit_output_res.append(xpredictions[xpredictions_idx])
                    xpredictions_idx += 1
                if len(explicit_output_res) > 0:
                    explicit_output_res.sort(key = lambda x: -x['prediction']['output_prob'])
                    prediction["explicit_outputs"] = [x['prediction'] for x in explicit_output_res]
                preds_file.write(json.dumps(prediction) + "\n")
            preds_file.flush()
            if args.add_metrics:
                collated = collate_scores(predictions)
                all_metrics_aggregated[input_file] = collated['metrics_aggregated']
    if args.add_metrics:
        save_json(os.path.join(args.output_dir, "metrics.json"), all_metrics_aggregated)


if __name__ == "__main__":
    args = get_args()
    main(args)