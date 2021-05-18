# Macaw

## Introduction

Macaw (<b>M</b>ulti-<b>a</b>ngle <b>c</b>(q)uestion <b>a</b>ns<b>w</b>ering) is a ready-to-use model capable of general 
question answering, showing robustness outside the domains it was 
trained on. It has been trained in "multi-angle" fashion, which means it can handle a flexible set of input
and output "slots" (like question, answer, explanation) .

Macaw was built on top of [T5](https://github.com/google-research/text-to-text-transfer-transformer) and 
comes in three sizes corresponding to T5-11B, T5-3B, T5-large.

### Minimal usage example

Here is a basic example showing use of the smallest model based on T5-large (not generally recommended, but has much 
smaller footprint), where given a question we want to return an answer and suggested multiple-choice answer options.

```buildoutcfg
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("allenai/macaw-large")
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/macaw-large")
input_string = "$answer$ ; $mcoptions$ ; $question$ = What is the color of a cloudy sky?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)

>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['$answer$ = gray ; $mcoptions$ = (A) blue (B) white (C) grey (D) white']
```

(note there's no guarantee the different slots are fully coherent, as in the gray/grey case here)

### Supported slots

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

### Examples

Some suggestive examples from the Macaw (11B) model, for different angles:

  * (Q→A) Q: James went camping in the woods, but forgot to bring a hammer to bang the tent pegs in. What else might he use? <br> 
  → A: rocks

  * (Q→A) Q: If plastic was an insulator, then would a plastic spoon conduct electricity? <br>
  → A: no

  * (Q→AE) Q: Which force pulls objects to the ground? <br>
  → A: gravity <br>
  → E: Gravitational force causes objects that have mass to be pulled down on a planet.

  * (A→QE) A: elephant <br>
  → Q: Which animal has the largest ears? <br>
  → E: The ears of an elephant are the largest.

  * (A→QM) A: car battery <br>
  → Q: Which of these items is necessary for a car to start? <br>
  → M: (A) car battery (B) windshield wiper blade (C) car radio (D) car radio antenna


## Demo

See [here](http://github.com/macaw/demo/README.md) for instructions and code to run an interactive version of Macaw.

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
       * [ARC](https://allenai.org/data/arc): QMC→AE, AQC→M, CQME→A, QME→A, QE→A, QMC→A, QC→AE, QM→AE, QMAC→E, QMA→E
       * [ARC-DA](https://allenai.org/data/arc-da): QC→AE, Q→AE, QC→A, Q→A, CQE→A, QE→A, AE→Q, AC→Q, QA→E, AQC→E
   
## Available models

Macaw models in three different sizes can be accessed from the Hugging Face model hub:

   * [macaw-11b](https://huggingface.co/allenai/macaw-11b)  (11 billion parameters)
   * [macaw-3b](https://huggingface.co/allenai/macaw-3b)  (3 billion parameters)
   * [macaw-large](https://huggingface.co/allenai/macaw-3b)  (770 million parameters)

For a sense of the degradation in performance for the smaller sizes, here are baseline scores on the ARC Challenge and 
ARC Easy multiple-choice development questions. Included are variants with and without IR context from a large science 
corpus (corresponding to angles QMC->A and QM->A respectively).

|Model | ARC Challenge | ARC Challenge (no IR) | ARC Easy | ARC Easy (no IR)|
|---|---|---|---|---|
|Macaw (11B) | 76.9 | 74.6 | 91.2 | 84.9|
|Macaw-3B | 68.2 | 67.9 | 87.9 |  77.7|
|Macaw-large | 57.2 | 50.5 | 82.5 | 63.9|

## Disclaimer

As a model capable of generating free form text, the output of the model is not guaranteed to be free of
offensive material, so appropriate caution is advised when using the model.

## Citation

If you use Macaw in your work, please reference the related [paper] using

```buildoutcfg
@article{...}
```