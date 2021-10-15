import json
import math
import random
import re


# Default generation options
GENERATOR_OPTIONS_DEFAULT = {"min_length": 1, "max_length": 128, "num_beams": 1, "num_return_sequences": 1,
                             "do_sample": False, "top_k": 50, "top_p": 1.0, "temperature": 1.0,
                             "length_penalty": 1.0, "repetition_penalty": 1.0}
DEFAULT_SLOT_FORMAT = {
    "slot": "$SLOT$",
    "assign": " = ",
    "separator": " ; ",
    "missing_value": "N/A"
}

SLOT_SHORTFORMS = {"Q": "Question", "C": "Context", "A": "Answer", "E": "Explanation", "M": "MCOptions"}
SLOT_FROM_LC = {x.lower(): x for x in SLOT_SHORTFORMS.values()}
SLOT_KEY_FROM_LC = {v.lower(): k for k, v in SLOT_SHORTFORMS.items()}


def save_jsonl(file_name, data):
    with open(file_name, 'w') as file:
        for d in data:
            file.write(json.dumps(d))
            file.write("\n")


def load_jsonl(file_name):
    with open(file_name, 'r') as file:
        return [json.loads(line.strip()) for line in file]


def save_json(file_name, data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data))


# Load model and tokenizer, also return the cuda device used for input to model
def load_model(model_name_or_path, cuda_devices = None):
    from transformers import T5Tokenizer, T5ForConditionalGeneration

    cuda_devices = cuda_devices or []
    tokenizer = T5Tokenizer.from_pretrained(model_name_or_path)
    model = T5ForConditionalGeneration.from_pretrained(model_name_or_path)
    device_map = None
    if len(cuda_devices) > 1:
        # Split layers across the multiple GPUs, put extras in later devices to leave a bit extra on first one
        num_layers = model.config.num_layers
        n_gpu = len(cuda_devices)
        layers_per_gpu = num_layers // n_gpu
        has_one_extra = n_gpu - (num_layers - layers_per_gpu * n_gpu)
        device_map = {}
        current = 0
        for device in cuda_devices:
            next = current + layers_per_gpu
            if len(device_map) >= has_one_extra:
                next += 1
            device_map[device] = list(range(current, next))
            current = next
    if len(cuda_devices) > 0:
        device = f"cuda:{cuda_devices[0]}"
    else:
        device = "cpu"

    if device_map is not None:
        model.parallelize(device_map)
    else:
        model.to(device)
    return {"model": model, "tokenizer": tokenizer, "cuda_device": device}


# Run model in free generation mode
def run_model(model, tokenizer, cuda_device, input_string, generator_options):
    import torch
    with torch.no_grad():
        input_string = input_string
        input_ids = tokenizer.encode(input_string, return_tensors="pt").to(cuda_device)
        res = model.generate(input_ids, **generator_options)
        output_strings = tokenizer.batch_decode(res, skip_special_tokens=True)
        res = {"input_raw": input_string, "output_raw_list": output_strings}
    return res


# Run model in forced generation mode, capturing each token probability
def run_model_with_outputs(model, tokenizer, cuda_device, input_string, output_strings):
    import torch
    with torch.no_grad():
        input_string = input_string
        input_ids = tokenizer.encode(input_string, return_tensors="pt").to(cuda_device)
        all_res = []
        for output_string, output_text in output_strings:
            output_ids = tokenizer.encode(output_string, return_tensors="pt").to(cuda_device)
            res = model(input_ids, labels=output_ids, return_dict=True)
            res_softmax = torch.softmax(res.logits[0], dim=1)
            raw_probs = [x[y.item()].item() for x,y in list(zip(res_softmax, output_ids[0]))]
            output_prob = 1
            for raw_prob in raw_probs:
                output_prob *= raw_prob
            loss = res.loss.item()
            all_res.append({
                "input_raw": input_string,
                "output_raw": output_string,
                "output_text": output_text,
                "loss": loss,
                "score": math.exp(-loss),
                "output_prob": output_prob,
                "output_token_probs": raw_probs,
                "output_tokens": tokenizer.convert_ids_to_tokens(output_ids[0])
            })
    return all_res


# Split apart a string, like "$answer$ = foo ; $explanation$ = bar" into a dictionary of slots
# and values, like {"answer": "foo", "explanation": "bar"}
def decompose_slots(input_string, fmt=None):
    fmt = fmt or DEFAULT_SLOT_FORMAT
    input_string = input_string.strip()
    no_slot = "PREFIX"
    slot_re = re.compile('(?i)'+re.escape(fmt['slot']).replace("SLOT", "(\\w*?)"))
    assign_re = re.escape(fmt['assign']).replace('\\ ','\\s*')
    separator_re = re.escape(fmt['separator']).replace('\\ ','\\s*')
    strip_re = re.compile(f"^({assign_re})?(.*?)({separator_re})?$")
    slot_pos = []
    for m in slot_re.finditer(input_string):
        slot_pos.append((m.span(), m.group(1)))
    if len(slot_pos) == 0:
        return {no_slot: input_string}
    if slot_pos[0][0][0] > 0:
        slot_pos = [((0,-1), no_slot)] + slot_pos
    res = {}
    for idx, (pos, slot_name) in enumerate(slot_pos):
        if idx == len(slot_pos) - 1:
            value = input_string[pos[1]+1:]
        else:
            value = input_string[pos[1]+1:slot_pos[idx+1][0][0]-1]
        m = strip_re.match(value)
        if m is not None:
            value = m.group(2)
        value = value.strip()
        if slot_name in res:
            value = res[slot_name] + " ~AND~ " + value
        res[slot_name] = value
    return res


def normalize_whitespace(input_string):
    return re.sub('\\s+', ' ', input_string).strip()


# Construct model input string from input/output slots and values, where output slots have an empty value, e.g.,
# fields = {"Q": "What is foo?", "A": ""} or
# fields = {"question": "What is foo?", ...} and angle = [["question"], ["angle"]] produces
# ("$answer$ ; $question$ = What is foo?", {"Question": "What is foo?"}, "Q->A")
def make_input_string(fields, angle=None, fmt=None):
    fmt = fmt or DEFAULT_SLOT_FORMAT
    input_slots = []
    input_slots_nice = {}
    output_slots = []
    angle_in = ""
    angle_out = ""
    if angle is None:
        slots = fields
    else:
        slots = {s:v for s,v in fields.items() if s in angle[0]}
        slots.update({s: "" for s in angle[1]})
    for slot, value in slots.items():
        slot_full = SLOT_SHORTFORMS.get(slot, slot).lower()
        slot_short = SLOT_KEY_FROM_LC.get(slot_full, slot_full[0].upper())
        slot_name = fmt['slot'].replace("SLOT", slot_full)
        if value.strip() == "":
            output_slots.append(slot_name)
            angle_out += slot_short
        else:
            input_slots_nice[SLOT_SHORTFORMS.get(slot, slot)] = value
            input_slots.append(f"{slot_name}{fmt['assign']}{value}")
            angle_in += slot_short
    return fmt['separator'].join(output_slots + input_slots), input_slots_nice, angle_in+"->"+angle_out


# Decompose a multi-line input where first character can reference a slot followed, optionally, by colon and value
demo_input_regex=re.compile("(?mi)^ *(([A-Z])(:| *$))? *(.*)")
def decompose_input(string):
    res = {}
    key = "NONE"
    for match in demo_input_regex.finditer(string):
        key = match.group(2) or key
        key = key.upper()
        old = res.get(key,"")
        new = normalize_whitespace(old + " " + match.group(4))
        res[key] = new
    if "C" in res:
        context = res['C']
        del res['C']
        res['C'] = context  # put context in last
    return res


def make_input_from_example(example):
    slots = decompose_slots(example)
    res_in = []
    res_out = []
    for slot, value in slots.items():
        slot_letter = slot[0].upper()  # Assumes short form is first letter capitalized
        if value.strip() == "":
            res_out.append(slot_letter)
        else:
            res_in.append(f"{slot_letter}: {value}")
    return "\n".join(res_in + res_out)


def compute_answer(model, tokenizer, cuda_device, raw_input, generator_options, output_strings=None):
    res = run_model(model, tokenizer, cuda_device, raw_input, generator_options)
    res['generator_options'] = generator_options
    if output_strings is not None:
        res['explicit_outputs'] = run_model_with_outputs(raw_input, output_strings)
        res['explicit_outputs'].sort(key=lambda x: -x['score'])
    return res


# Basic heuristics for splitting multiple-choice options
def split_mc_question(question, min_choices=2):
    choice_sets = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"],
                   ["1", "2", "3", "4", "5"],
                   ["G", "H", "J", "K"],
                   ['a', 'b', 'c', 'd', 'e']]
    patterns = [r'\(#\)', r'#\)', r'#\.']
    for pattern in patterns:
        for choice_set in choice_sets:
            regex = pattern.replace("#", "([" + "".join(choice_set) + "])")
            labels = [m.group(1) for m in re.finditer(regex, question)]
            if len(labels) >= min_choices and labels == choice_set[:len(labels)]:
                splits = [s.strip() for s in re.split(regex, question)]
                return {"stem": splits[0],
                        "choices": [{"text": splits[i + 1],
                                     "label": splits[i]} for i in range(1, len(splits) - 1, 2)]}
    return None


def get_raw_response(state_dict, compute_answer_fn=None, model_dict=None):
    if 'input' not in state_dict and 'input_fields' not in state_dict:
        return {}
    if 'input' in state_dict:
        input_string = state_dict['input']
        input_fields = decompose_input(input_string)
    else:
        input_fields = state_dict['input_fields']
    explicit_outputs = None
    # Custom handling of "X" field for "explicit" output values
    if "X" in input_fields:
        explicit_outputs = split_mc_question(input_fields["X"])
        if explicit_outputs is None:
            explicit_outputs = [input_fields["X"]]
        else:
            explicit_outputs = [x['text'] for x in explicit_outputs['choices']]
        del input_fields["X"]
    raw_input, input_slots, angle = make_input_string(input_fields)
    output_strings = None
    if explicit_outputs is not None:
        angle_out = angle.split("->")[1]
        angle_out = angle_out[0] if len(angle_out) > 0 else "A"
        output_strings = [(make_input_string({angle_out: x})[0], x) for x in explicit_outputs]

    generator_options = GENERATOR_OPTIONS_DEFAULT.copy()
    for key, init_val in generator_options.items():
        if key in state_dict:
            val = state_dict[key]
            if isinstance(val, str):
                if isinstance(init_val, bool):
                    val = int(val) > 0
                elif isinstance(init_val, int):
                    val = int(val)
                else:
                    val = float(val)
            generator_options[key] = val

    if compute_answer_fn is not None:
        random_tickle = 1
        # Trick to make sure streamlit doesn't cache responses if sampling is used in generator settings
        if generator_options['do_sample']:
            random_tickle = random.random()
        res_raw = compute_answer_fn(raw_input, generator_options, random_tickle, output_strings)
    else:
        assert model_dict is not None
        res_raw = compute_answer(model_dict['model'], model_dict['tokenizer'], model_dict['cuda_device'],
                                 raw_input, generator_options, output_strings)
    res = res_raw.copy()
    res['requested_angle'] = angle
    res['input_slots'] = input_slots
    res['output_slots_list'] = [decompose_slots(output) for output in res['output_raw_list']]
    if explicit_outputs is not None:
        res['explicit_output_angle'] = SLOT_SHORTFORMS.get(angle_out, angle_out)
    return res


# Example:
# >> model_dict = load_model("allenai/macaw-large")
# >> res = run_macaw("Q: James went camping in the woods, but forgot to bring a hammer to bang the tent pegs in. What else might he use?\nA", model_dict)
# >> res['output_slots_list'][0]
# {'answer': 'a rock'}
def run_macaw(input, model_dict, generator_options=None):
    state_dict = {}
    if isinstance(input, str):
        state_dict['input'] = input
    else:
        state_dict['input_fields'] = input
    if generator_options is not None:
        state_dict.update(generator_options)
    res = get_raw_response(state_dict, model_dict=model_dict)
    return res




