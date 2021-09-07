# Macaw

## Introduction

Macaw (<b>M</b>ulti-<b>a</b>ngle <b>c</b>(q)uestion <b>a</b>ns<b>w</b>ering) is a ready-to-use model capable of general 
question answering, showing robustness outside the domains it was 
trained on. It has been trained in "multi-angle" fashion, which means it can handle a flexible set of input
and output "slots" (like question, answer, explanation) .

Macaw was built on top of [T5](https://github.com/google-research/text-to-text-transfer-transformer) and 
comes in different sizes:  [macaw-11b](https://huggingface.co/allenai/macaw-11b), [macaw-3b](https://huggingface.co/allenai/macaw-3b), 
and [macaw-large](https://huggingface.co/allenai/macaw-large), as well as an answer-focused version featured on 
various leaderboards: [macaw-answer-11b](https://huggingface.co/allenai/macaw-answer-11b) (see [below](#training-data)).

### Examples

Some suggestive examples from the Macaw (11B) model, for different angles:

  * (Q→A) <i>Given a question, what's the answer?</i> <br>
  **Q: James went camping in the woods, but forgot to bring a hammer to bang the tent pegs in. What else might he use? <br> 
  → A: rocks**
  
  * (QM→A) <i>Given a question and answer choices, what's the answer?</i> <br>
  **Q: James went camping in the woods, but forgot to bring a hammer to bang the tent pegs in. What else might he use? <br> 
           M: (A) a leaf (B) a log (C) a worm <br>
  → A: a log**

  * (Q→AE) <i>Given a question, what's the answer and an explanation?</i><br>
  **Q: Which force pulls objects to the ground? <br>
  → A: gravity <br>
  → E: Gravitational force causes objects that have mass to be pulled down on a planet.**

  * (A→QE) <i>Given an answer, what's a plausible question and explanation?</i><br>
  **A: elephant <br>
  → Q: Which animal has the largest ears? <br>
  → E: The ears of an elephant are the largest.**

  * (C→QA) <i>Given a context, what's a plausible question and answer?</i><br>
  **C: A car needs a battery to start. <br>
  → Q: What is required for a car to start? <br>
  → A: battery**
  
For many more examples of the basic Q→A angle, see [examples.md](examples.md).

## Usage examples

Macaw can easily be used in the Hugging Face [transformers](https://github.com/huggingface/transformers) 
library, as shown here for the 
smallest model (the smallest model is not generally recommended, but has much 
smaller footprint), where given a question we want to return an answer and 
suggested multiple-choice answer options.

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("allenai/macaw-large")
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/macaw-large")
input_string = "$answer$ ; $mcoptions$ ; $question$ = What is the color of a cloudy sky?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)

>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['$answer$ = gray ; $mcoptions$ = (A) blue (B) white (C) grey (D) white']
```

(run `pip install -r requirements.txt` if any dependencies are missing). Note there's no guarantee the different 
slots are fully coherent, as in gray/grey (and duplicate "white") here,
more so for the macaw-large model vs the larger ones.

The code in `macaw/utils.py` includes some convenience wrappers, such as `load_model` and 
`run_macaw`, here are some examples
loading the macaw-11b model onto two GPUs (need around 48GB total GPU memory for the 
largest model to work):

```
from macaw.utils import load_model, run_macaw
model_dict = load_model("allenai/macaw-11b", cuda_devices=[0,1])
res1 = run_macaw("Q: Which force pulls objects to the ground?\nA\nE", model_dict)
# Alternate input syntax
res2 = run_macaw({"Q:":"Which force causes a compass needle to point north?", "A":""}, model_dict)
# Add sampling options for the output
res3 = run_macaw("Q: Which force pulls objects to the ground?\nA\nE", model_dict, {"do_sample": True, "temperature": 2.0})

>>> [print(res["output_slots_list"][0]) for res in [res1, res2, res3]]
{'answer': 'gravity', 'explanation': 'Gravitational force causes objects that have mass to be pulled down on a planet.'}
{'answer': 'magnetism'}
{'answer': 'gravitional force', 'explanation': 'Gravitational force causes objects that have mass to be pulled down on a planet.'}
```

For batch evaluation of instances at various angles, see [`macaw/batch_eval.py`](macaw/batch_eval.py) for pointers.

## Supported slots

Here are the slots available in Macaw, generally applicable for both input and output:

| Slot name | Description | Example | 
|---|---|---|
|question (Q) | Question text | What is the color of a cloudy sky? |
|answer (A) | Answer text | The sky is blue |
|mcoptions (M) | Multiple-choice answer options |  (A) blue (B) white (C) grey |
|context (C) | Potentially relevant context (noisy IR) | The sky looks blue to us because... |
|explanation (E) | Sentences explaining the answer | A cloudy sky is usually gray in color... |

An angle is a specific set of input/output slots, for instance QM->AE is the task of producing answer and explanation,
given a question and multiple-choice options. Macaw is trained on a wide variety of angles and handles unseen angles
as well, one exception is that the context (C) only appears as an input slot in the training data.

  
## The Challenge300 dataset of probing questions

The **Challenge300** dataset of 300 diverse probing examples can be found in 
[challenge300-probes-v1.jsonl](challenge300-probes-v1.jsonl). The basic Q→A output
from Macaw (at different sizes), as well as outputs from [GPT3](https://arxiv.org/pdf/2005.14165.pdf), 
[Jurassic-1](https://www.ai21.com/blog/announcing-ai21-studio-and-jurassic-1) and 
[alternate T5 models](https://www.aclweb.org/anthology/2020.emnlp-main.437/) trained on NaturalQuestions, can be seen in
[examples.md](examples.md).

## Demo

See [DEMO.md](DEMO.md) for instructions and code to host an interactive version of Macaw.

## Training data

Macaw was trained in two steps from the text-to-text transformer 
model [T5](https://github.com/google-research/text-to-text-transfer-transformer):

   1. Multi-angle version of [UnifiedQA](https://github.com/allenai/unifiedqa) by fine-tuning T5
   on the following 7 datasets and associated angles:
       * [BoolQ](https://github.com/google-research-datasets/boolean-questions), 
       [SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer), 
       [NarrativeQA](https://github.com/deepmind/narrativeqa): QC→A, AC→Q
       * [ARC](https://allenai.org/data/arc), [OBQA](https://allenai.org/data/open-book-qa): 
       QMC→A, QC→A, QM→A,QAC→M, MAC→Q, AC→QM
       * [RACE](https://www.cs.cmu.edu/~glai1/data/race/), 
       [MCTest](https://mattr1.github.io/mctest/): QMC→A, QC→A, QAC→M,MAC→Q
       
   2. Further fine-tuning of Multi-Angle UnifiedQA on multiple-choice and direct-answer elementary science questions, 
   along with (up to 5) explanation sentences from [WorldTreeV2](http://cognitiveai.org/explanationbank/): 
       * [ARC](https://allenai.org/data/arc): QMC→AE, AQC→M, QMEC→A, QME→A, QE→A, QMC→A, QC→AE, QM→AE, QMAC→E, QMA→E
       * [ARC-DA](https://allenai.org/data/arc-da): QC→AE, Q→AE, QC→A, Q→A, QEC→A, QE→A, AE→Q, AC→Q, QA→E, AQC→E
       
   3. A specialized answer-focused model, <b>macaw-answer-11b</b> (called "UnifiedQA + ARC MC/DA + IR" on the 
   leaderboards for [ARC](https://leaderboard.allenai.org/arc/submissions/public), 
   [ARC-Easy](https://leaderboard.allenai.org/arc_easy/submissions/public), and 
   [ARC-DA](https://leaderboard.allenai.org/genie-arcda/submissions/public))
   was trained on a smaller set of angles, not including explanations:
       * ARC: QMC→A, QAC→M, QC→A, QM→A, MAC→Q, AC→QM, M→QA
       * ARC-DA: QC→A, Q→A, AC→Q, C→QA
       
   
## Available models

The Macaw models can be accessed from the Hugging Face model hub:

   * [macaw-11b](https://huggingface.co/allenai/macaw-11b)  (11 billion parameters)
   * [macaw-3b](https://huggingface.co/allenai/macaw-3b)  (3 billion parameters)
   * [macaw-large](https://huggingface.co/allenai/macaw-large)  (770 million parameters)
   * [macaw-answer-11b](https://huggingface.co/allenai/macaw-answer-11b)  (11 billion parameters)

For a sense of the degradation in performance for the smaller sizes, here are baseline scores on the ARC Challenge and 
ARC Easy multiple-choice <b>development</b> questions. Included are variants with and without IR context from a large science 
corpus (corresponding to angles QMC→A and QM→A respectively).

|Model | ARC Challenge | ARC Challenge (no IR) | ARC Easy | ARC Easy (no IR)|
|---|---|---|---|---|
|Macaw (11B) | 76.9 | 74.6 | 91.2 | 84.9|
|Macaw-3B | 68.2 | 67.9 | 87.9 |  77.7|
|Macaw-large | 57.2 | 50.5 | 82.5 | 63.9|
|Macaw-answer (11B) | 79.9 | 75.2 | 90.5 | 85.8|

## Disclaimer

As a model capable of generating free form text, the output of the model is not guaranteed to be free of
offensive material, so appropriate caution is advised when using the model.

## Citation

If you use Macaw in your work, please reference the related [paper](https://arxiv.org/abs/2109.02593) using

```
@article{Tafjord2021Macaw,
  title={General-Purpose Question-Answering with {M}acaw},
  author={Oyvind Tafjord and Peter Clark},
  journal={ArXiv},
  year={2021},
  volume={abs/2109.02593}
}
```
