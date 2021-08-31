# Macaw demo

For convenience, we provide the minimally documented file [`macaw/demo.py`](macaw/demo.py) with self-contained code 
for starting a local demo to interact with Macaw models in 
a browser (or through a REST API). It uses the [streamlit](https://streamlit.io/) framework, but the code
can easily be modified for other use cases.

To configure the demo, simply modify the variables near the top of the file, e.g.,

```
# CONFIGURATION
MODEL_NAME_OR_PATH = "allenai/macaw-large"  # Name or path to model
CUDA_DEVICES = []   # List of available CUDA devices if any, e.g., [0, 2]
```

This defines which model to use (downloaded to local cache from the Hugging Face model hub, or point to
a local directory where model is stored) as well as any
GPU devices available (recommended for good performance for the models larger than Macaw-large).

Also make sure the dependencies are installed (e.g., run `pip install -r requirements.txt`, ideally in a
dedicated virtual environment), and the demo is started
by running `streamlit run macaw/demo.py`. It might take a few minutes for the model to load and be ready, and
then the demo can be accessed in a browser by going to http://localhost:8501/.

The input format in the demo expects each slot to be given on separate lines, prefixed by the slot capital
letter, with output slots given without value. E.g., a request for angle QM->AE is given as:

```
Q: Which characteristic of a cheetah is more likely to be learned rather than inherited?
M: (A) speed (B) a spotted coat (C) hunting strategies (D) claws that do not retract
A
E
```

which, for the Macaw-large model, should give the output:

```
Answer: hunting strategies
Explanation: Skills are learned characteristics. Hunting is a kind of skill.
```

The demo also supports a special mode for scoring different answer options, this only works when there is a single
output slot, and makes the most sense when the answer options are also present as multiple-choice options. This
is indicated by the special "X" slot, an example would be:

```
Q: What material is magnetic?
M: (A) iron (B) copper (C) paper
X: (A) iron (B) copper (C) paper
A
```
which (again for Macaw-large) should produce the output:

```
Output rank 1:
Answer: iron

Explicit outputs ranked:
Answer: iron (0.9998)
Answer: copper (0.0002)
Answer: paper (0.0000)
```
which has both the original generated answer, as well as the 3 explicit answers along with the products of the 
associated output token probabilities. 

The demo also has a second page accessed by selecting "Generator settings" in the side bar, where the
generator parameters (like beam size and number of results) can be adjusted.


## Memory requirements

Running the main Macaw (11B) model requires around 100GB of CPU RAM to load properly (to temporarily store
two copies of the 44GB worth of weights), and 48GB of GPU RAM to run on 
a GPU. It's possible to squeeze onto a single 48GB GPU, but normally you would need to split across multiple GPUs
by specifying a list of more than one device in the `CUDA_DEVICES` variable.

(It's technically possible to load the 11B model with ~50GB of CPU RAM and 48GB of GPU RAM by carefully loading
an empty model, moving it to the GPU, load the weights, move weights to GPU, delete from CPU)

## REST API

The demo code also includes a REST api available at port 8502 (by default), it takes an input string in same format, along with
optional generator options. A couple of examples using curl (with newlines inserted for readability), using the
(inferior) Macaw-large model:

```
$ curl --data-urlencode $'input=Q: What material is magnetic?\nM: (A) iron (B) copper (C) paper\nA' -G http://localhost:8502/api
{"generator_options":{"do_sample":false,"length_penalty":1.0,"max_length":128,"min_length":1,"num_beams":1,"num_return_sequences":1,  
      "repetition_penalty":1.0,"temperature":1.0,"top_k":50,"top_p":1.0},
  "input_raw":"$answer$ ; $question$ = What material is magnetic? ; $mcoptions$ = (A) iron (B) copper (C) paper",
  "input_slots":{"MCOptions":"(A) iron (B) copper (C) paper","Question":"What material is magnetic?"},
  "output_raw_list":["$answer$ = iron"],
  "output_slots_list":[{"answer":"iron"}],"requested_angle":"QM->A"}
```

Include "X" options for explicit output scoring:
```
$ curl --data-urlencode $'input=Q: What material is magnetic?\nM: (A) iron (B) copper (C) paper\nX: (A) iron (B) copper (C) paper\nA' -G http://localhost:8502/api
{"explicit_output_angle":"Answer",
 "explicit_outputs":[
    {"input_raw":"$answer$ ; $question$ = What material is magnetic? ; $mcoptions$ = (A) iron (B) copper (C) paper",
     "loss":3.015684887941461e-05,"output_prob":0.9997889405240201,
     "output_raw":"$answer$ = iron","output_text":"iron",
     "output_token_probs":[1.0,1.0,1.0,1.0,1.0,0.99979168176651,0.9999972581863403],
     "output_tokens":["\u2581$","ans","wer","$","\u2581=","\u2581iron","</s>"],"score":0.9999698436058337},
    {"input_raw":"$answer$ ; $question$ = What material is magnetic? ; $mcoptions$ = (A) iron (B) copper (C) paper",
     "loss":1.2147718667984009,"output_prob":0.0002027770735510033,
     "output_raw":"$answer$ = copper","output_text":"copper",
     "output_token_probs":[1.0,1.0,1.0,1.0,1.0,0.00020277731528040022,0.9999988079071045],
     "output_tokens":["\u2581$","ans","wer","$","\u2581=","\u2581copper","</s>"],"score":0.29677771142124026},
   {"input_raw":"$answer$ ; $question$ = What material is magnetic? ; $mcoptions$ = (A) iron (B) copper (C) paper",
    "loss":1.836950659751892,"output_prob":2.6034949917854637e-06,
    "output_raw":"$answer$ = paper","output_text":"paper",
    "output_token_probs":[1.0,1.0,1.0,1.0,1.0,2.603500888653798e-06,0.9999977350234985],
    "output_tokens":["\u2581$","ans","wer","$","\u2581=","\u2581paper","</s>"],"score":0.15930245360755435}],
  "generator_options":{"do_sample":false,"length_penalty":1.0,"max_length":128,"min_length":1,"num_beams":1,"num_return_sequences":1,
      "repetition_penalty":1.0,"temperature":1.0,"top_k":50,"top_p":1.0},
   "input_raw":"$answer$ ; $question$ = What material is magnetic? ; $mcoptions$ = (A) iron (B) copper (C) paper",
   "input_slots":{"MCOptions":"(A) iron (B) copper (C) paper","Question":"What material is magnetic?"},
   "output_raw_list":["$answer$ = iron"],
   "output_slots_list":[{"answer":"iron"}],"requested_angle":"QM->A"}
```

Change some of the generator options (now `output_slots_list` has two elements, the second one isn't very good though):
```
$curl --data-urlencode $'input=Q: What material is magnetic?\nM: (A) iron (B) copper (C) paper\nA' --data 'num_beams=4' --data 'num_return_sequences=2' -G http://localhost:8502/api
{"generator_options":{"do_sample":false,"length_penalty":1.0,"max_length":128,"min_length":1,"num_beams":4,"num_return_sequences":2,
    "repetition_penalty":1.0,"temperature":1.0,"top_k":50,"top_p":1.0},
  "input_raw":"$answer$ ; $question$ = What material is magnetic? ; $mcoptions$ = (A) iron (B) copper (C) paper",
  "input_slots":{"MCOptions":"(A) iron (B) copper (C) paper","Question":"What material is magnetic?"},
  "output_raw_list":["$answer$ = iron","$answer$ = iron (B) copper"],
  "output_slots_list":[{"answer":"iron"},{"answer":"iron (B) copper"}],"requested_angle":"QM->A"}
```