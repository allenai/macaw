from datetime import datetime
import json
import math
import os
import sys

import streamlit as st
from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

sys.path.append(os.path.join(os.getcwd()))

from macaw.utils import SLOT_FROM_LC, GENERATOR_OPTIONS_DEFAULT, decompose_slots, get_raw_response, \
    load_model, make_input_from_example, run_model, run_model_with_outputs


## Start demo with "streamlit run macaw/demo.py"

# CONFIGURATION
MODEL_NAME_OR_PATH = "allenai/macaw-large"  # Name or path to model
CUDA_DEVICES = []   # List of available CUDA devices if any, e.g., [0] or [0, 2]
LOG_FILE = "macaw_demo.log"  # Where to save a log
REST_API_PORT = 8502 # Which port to use for API, set to None for no API


###### Model loading
# If model hasn't loaded yet, this will load it (a single time, shared between requests)
if not hasattr(st, 'MODEL'):
    if MODEL_NAME_OR_PATH is None:  # For testing
        st.MODEL = None
        st.TOKENIZER = None
        st.CUDA_DEVICE = None
    else:
        st.MODEL = "Loading"
        print(f"{datetime.now()} Loading model...")
        model_dict = load_model(MODEL_NAME_OR_PATH, CUDA_DEVICES)
        st.MODEL, st.TOKENIZER, st.CUDA_DEVICE = model_dict['model'], model_dict['tokenizer'], model_dict['cuda_device']
        print(f"{datetime.now()} Model loaded!")

######

# Run model in free generation mode
def run_model_demo(input_string, **generator_options):
    return run_model(st.MODEL, st.TOKENIZER, st.CUDA_DEVICE, input_string, generator_options)


# Run model in forced generation mode, capturing each token probability
def run_model_with_outputs_demo(input_string, output_strings):
    return run_model_with_outputs(st.MODEL, st.TOKENIZER, st.CUDA_DEVICE, input_string, output_strings)


def render_output_slots(state, index):
    output_slots = state.output_slots[index]
    if state.beam_scores and len(state.beam_scores) > index:
        beam_score = math.exp(state.beam_scores[index])
        beam_score = f"(beam score = {beam_score:.4f})"
        st.write(f"### Output rank {index + 1}: ", beam_score)
    else:
        st.write(f"### Output rank {index + 1}: ")
    str_out = ""
    for slot, value in output_slots.items():
        if slot in SLOT_FROM_LC:
            str_out += "**" + SLOT_FROM_LC[slot] + ":** " + value + "  \n"
    st.write(str_out)


def render_explicit_output(state, index):
    explicit_output = state.explicit_outputs[index]
    prob = explicit_output.get('output_prob', -1.0)
    str_out = f"   {index+1}. ** {state.explicit_output_angle}:** {explicit_output['output_text']}  "
    str_out += f"({prob:.4f})"
    st.write(str_out)


def main():
    state = _get_state()
    pages = {
        "Main": main_page,
        "Generator settings": debug_page,
    }

    query_params = st.experimental_get_query_params()
    if 'input' in query_params:
        state.input = query_params['input'][0]

    st.sidebar.title("Pages")
    page = st.sidebar.radio("Select page", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page](state)

    if state.num_beams is None:
        initialize_generator_settings(state)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()


def initialize_generator_settings(state):
    state.num_beams = GENERATOR_OPTIONS_DEFAULT['num_beams']
    state.num_return_sequences = GENERATOR_OPTIONS_DEFAULT['num_return_sequences']
    state.do_sample = GENERATOR_OPTIONS_DEFAULT['do_sample']
    state.top_k = GENERATOR_OPTIONS_DEFAULT['top_k']
    state.top_p = GENERATOR_OPTIONS_DEFAULT['top_p']
    state.temperature = GENERATOR_OPTIONS_DEFAULT['temperature']
    state.length_penalty = GENERATOR_OPTIONS_DEFAULT['length_penalty']
    state.repetition_penalty = GENERATOR_OPTIONS_DEFAULT['repetition_penalty']


def debug_page(state):
    st.title("Debug page")
    st.write("**Generator settings:** (see [here](https://huggingface.co/transformers/main_classes/model.html?highlight=generate#transformers.generation_utils.GenerationMixin.generate) for details)")
    state.num_beams = st.slider("Num beams", min_value=1, max_value=10, value=state.num_beams or 1, step=1)
    state.num_return_sequences = st.slider("Num return sequences", min_value=1, max_value=10, value=state.num_return_sequences or 1, step=1)
    state.do_sample = st.checkbox("Do Sample", value=state.do_sample or False)
    state.top_k = st.slider("Top K", min_value=1, max_value=100, value=state.top_k or 50, step=1)
    state.top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=state.top_p or 1.0)
    state.temperature = st.slider("Temperature", min_value=0.0, max_value=10.0, value=state.temperature or 1.0)
    state.length_penalty = st.slider("Length penalty", min_value=0.0, max_value=10.0, value=state.length_penalty or 1.0)
    state.repetition_penalty = st.slider("Repetition penalty", min_value=0.0, max_value=10.0, value=state.repetition_penalty or 1.0)

    st.write("---")

    st.write("Raw input:")
    st.text(state.raw_input)
    st.write("Raw output:")
    if state.raw_output:
        for raw_output in state.raw_output:
            st.text(raw_output)
    st.write("Token probabilities:")
    if state.token_probs:
        for token_probs in state.token_probs:
            st.text(token_probs)

    # st.write("Full state:",state._state['data'])
    st.write("st server started:", hasattr(st, 'already_started_server'))
    if  hasattr(st, 'already_started_server'):
        st.write("st server started value:", st.already_started_server)


EXAMPLES = [
    {"type":"DA-NoIR","id":"ARCEZ_ACTAAP_2011_5_12","angle":"Q->AE","input":"$answer$ ; $explanation$ ; $question$ = There are many different processes that take place in plant and animal cells. Cellular respiration is one of those processes. What is the purpose of cellular respiration?","output":"$explanation$ = Food contains carbohydrates. Cellular respiration is when a cell converts from oxygen and carbohydrates into carbon dioxide, water, and energy. Releasing energy is a kind of function. ; $answer$ = get energy for cells"},
    {"type":"DA-NoIR","id":"ARCEZ_CSZ20680","angle":"EQ->A","input":"$answer$ ; $explanation$ = A comet is often made of ice. If an object orbits a celestial object then that object is probably a celestial object as well. ; $question$ = An object composed mainly of ice is orbiting the Sun in an elliptical path. This object is most likely","output":"$answer$ = comet"},
    {"type":"DA-NoIR","id":"ARCEZ_MEAP_2005_8_43","angle":"QE->A","input":"$answer$ ; $question$ = Astronauts weigh more on Earth than they do on the moon because ; $explanation$ = The earth has more mass than the moon. As the force of gravity increases, the weight of objects will increase. As mass of a celestial body increases, the force of gravity on that planet will increase.","output":"$answer$ = the moon has lower gravity"},
    {"type":"DA-NoIR","id":"ARCEZ_Mercury_7040863","angle":"Q->AE","input":"$answer$ ; $explanation$ ; $question$ = What system helps the body defend itself against disease while maintaining the levels of body fluids?","output":"$explanation$ = N\/A ; $answer$ = lymphatic"},
    {"type":"DA-NoIR","id":"ARCCH_Mercury_SC_401663","angle":"Q->AE","input":"$answer$ ; $explanation$ ; $question$ = A student can conserve resources by placing which objects in a compost pile?","output":"$answer$ = paper towels ; $explanation$ = Recycling nonrenewable resources has a positive impact on the conservation of those resources. A compost pile is used for recycling plants."},
    {"type":"DA-NoIR","id":"ARCCH_Mercury_SC_408859","angle":"Q->AE","input":"$answer$ ; $explanation$ ; $question$ = American alligators are common in Florida wetlands. They are known to eat frogs, turtles, fish, mice, and birds. What role does an American alligator fill in its ecosystem?","output":"$explanation$ = Consumers eat other organisms. In the food chain process an animal has the role of consumer which eats producers for food. Alligators eat birds. A role in the ecosystem is a role in the food chain process. ; $answer$ = consumer"},
    {"type":"DA-NoIR","id":"ARCCH_Mercury_180443","angle":"QE->A","input":"$answer$ ; $question$ = Which phase of the Moon occurs after a waxing gibbous? ; $explanation$ = A full moon occurs after a waxing gibbous moon.","output":"$answer$ = full moon"},
    {"type":"MC","id":"ARCCH_Mercury_7032743","angle":"QM->AE","input":"$answer$ ; $explanation$ ; $question$ = Which characteristic of a cheetah is more likely to be learned rather than inherited? ; $mcoptions$ = (A) speed (B) a spotted coat (C) hunting strategies (D) claws that do not retract","output":"$explanation$ = Hunting is a kind of skill. Skills are learned characteristics. ; $answer$ = hunting strategies"},
    {"type":"MC","id":"ARCCH_AIMS_2009_4_29","angle":"EMQC->A","input":"$answer$ ; $explanation$ = Humans move waste to a landfill for disposal. If a human discards an object then that object will become waste. Landfills have a negative impact on the environment. ; $mcoptions$ = (A) The electricity needed to keep food cold can be expensive. (B) If the electricity goes out, the food will spoil and make you sick. (C) Storing food longer reduces grocery store trips and gasoline use. (D) Old refrigerators contain chemicals and take up space in landfills. ; $question$ = A refrigerator uses electricity to create a cold place to store food. What negative impact does refrigerator use have on the environment? ; $context$ = A refrigerator that keeps food cold. Electricity used to power refrigerators used to store food samples for testing. Then, if you lose electricity for a short time, you can use these big \"ice cubes\" to keep food cold in your freezer or refrigerator. Laboratory-use refrigerators and cold rooms must not be used to store foods for consumption. Do not store food in a place used to store radioactive material such as a freezer or refrigerator. At The Grocery Store (1) Follow \"sell by\" and \"use by\" dates (2) Frozen food should be solid, refrigerated foods should be cold; Use food stored in the refrigerator quickly. Place NO FOOD labels on refrigerators used to store chemicals. Freeze water in plastic containers, if the electricity goes off you can use the ice to keep food cold in the refrigerator. A refrigerator uses electricity to create a cold place to store food.","output":"$answer$ = Old refrigerators contain chemicals and take up space in landfills."},
    {"type":"MC","id":"ARCCH_Mercury_SC_415491","angle":"QMC->AE","input":"$answer$ ; $explanation$ ; $question$ = Earth orbits the Sun once a year. About how many times does the moon orbit Earth in a year? ; $mcoptions$ = (A) 1 (B) 7 (C) 13 (D) 28 ; $context$ = The Moon takes about 28 days to orbit once around the Earth. Specifically, given that the Earth takes one year to orbit the sun, the time that it takes Venus to orbit the sun is 1.618 to the -1 years. This means that the distance between Earth and the Sun varies throughout the year and that the distance from the Earth to the Moon varies over each time it orbits us, which takes about 28 days. The moon's orbit around the earth once in about 28 days changes what portion of the moon is lighted by the sun and how much of that portion can be seen from the earth--the phases of the moon. In addition to orbiting around the Earth with respect to the background stars in a period of about 27 days 8 hours, the moon is part of the Earth-Moon duo orbiting the sun almost 1\/13th of a year; Even though the Earth passes through the comet's orbit each year, the comet itself orbits the Sun once about every 6 1\/2 years. Right now the Moon orbits the Earth roughly 12-13 times in a year; TRIVI A 1) How much farther from Earth does the moon's orbit move every year? The moon orbits Earth about 13 times per year. that the Earth orbits the Sun once each year, and that the Moon takes approximately 28 days to orbit the Earth.","output":"$answer$ = 13 ; $explanation$ = The moon orbiting the Earth occurs approximately 13 times per year."},
    {"type":"MC","id":"ARCCH_Mercury_7218750","angle":"QMC->AE","input":"$answer$ ; $explanation$ ; $question$ = Which type of water reservoir could always provide freshwater? ; $mcoptions$ = (A) inland lakes (B) river deltas (C) mountain glaciers (D) tropical seas ; $context$ = These sources have adversely affected both the coastal ponds region, other coastal embayments and inland freshwater lakes and ponds, including drinking water reservoirs. They are mainly inland birds found around freshwater lakes and reservoir. Cooling water is provided by Lake Bastrop, a 900 on freshwater reservoir. Cooling water is provided by Lake LBJ, a freshwater reservoir created by Wirtz Dam. or (b) into any waters of a lake or pond which are not inland freshwaters. Lake Assad, the Al Assad Reservoir, is the largest inland water body in Syria and provides its most important freshwater fishery. Glaciers are \"frozen freshwater reservoirs which release water during the drier summer months,\" Richard S. Williams Jr. of USGS wrote in a report. Know six different freshwater, sea-water or tropical fish and know what types of foods they  eat. The Director would first review the information that the new facility provided to validate the source water body type in which the cooling water intake structure is located (freshwater stream or river, lake or reservoir, estuary or tidal river, or ocean). Freshwater inland lakes and reservoirs provide our nation with 70% of its drinking water and supply water for industry, irrigation, and hydropower.","output":"$explanation$ = The majority of freshwater is found in in glaciers. ; $answer$ = mountain glaciers"},
    {"type":"MC","id":"ARCEZ_Mercury_182665","angle":"QMC->AE","input":"$answer$ ; $explanation$ ; $question$ = Which characteristic is exclusive to chordates? ; $mcoptions$ = (A) digestive tract with two openings (B) dorsal hollow nerve tube (C) closed circulatory system (D) bony internal skeleton ; $context$ = dorsal hollow nerve tube Phylum Chordata Subphylum Urochordata This is one group of invertebrate chordates that provides clues to the origin of vertebrates. Chordates are also characterized by a hollow, dorsal nerve cord. The result is a dorsal, hollow nerve cord unique to chordates. In addition, you can now understand why we refer to a hollow dorsal nerve tube when we talk about the characteristics of chordates. Hemichordates also have a dorsal, hollow nerve cord probably equivalent to the dorsal, hollow nerve cord partially characteristic of the chordates. They share some of the fundamental characteristics of the chordates, which we'll review later, such as a dorsal hollow nerve cord and gill slits. These structures are openings of the upper digestive tube in chordates. Most chordates have an internal skeleton against which muscles work. Other chordate features Chordates also have a closed circulatory system, and most, but not all, chordates have a heart . The nerve cord of chordates develops dorsally in the body as a hollow tube above the notochord.","output":"$answer$ = dorsal hollow nerve tube ; $explanation$ = N\/A"},
    {"type":"DA-IR-QStem","id":"ARCCH_Mercury_412551","angle":"QC->AE","input":"$answer$ ; $explanation$ ; $question$ = Screech owls have two color variations: red and grey. What advantage does the grey screech owl have over the red screech owl in a habitat that is made up of trees with dark-colored bark? ; $context$ = Eastern screech owls have all red or grey feathers. Eastern Screech Owls have also been called the common screech Owl, Ghost Owl, Dusk Owl, Little-eared Owl, Spirit Owl, Little Dukelet, Texas Screech-Owl, whickering Owl, little grey Owl, mottled Owl, the red Owl, the mouse Owl, the cat Owl, the shivering Owl, and the little horned Owl. Screech Owls are noted for occuring in two distinct color phases, red and gray. The screech owl has two color phases, gray and red. There are actually two color forms of the Eastern Screech-Owl: red and gray. Team Colors The Screech Owls' colors are blue, with white and red trim. Otus, a gray phase screech-owl, and Tess, a red phase screech-owl, have been educating groups for years. Among them were screech owls of both color phases: red and gray. Eastern Screech Owl An encyclopedic biology of the Red Screech Owl. Thus, like many scops-owls and Eastern Screech-Owl O. asio, some owlet-nightjars have red and gray color morphs.","output":"$explanation$ = N\/A ; $answer$ = hiding"},
    {"type":"DA-IR-QStem","id":"ARCEZ_CSZ20680","angle":"QC->AE","input":"$answer$ ; $explanation$ ; $question$ = An object composed mainly of ice is orbiting the Sun in an elliptical path. This object is most likely ; $context$ = They are composed mostly of ice and dust, and are typically in very elliptical orbits around the Sun. The elliptical path of objects orbiting the sun comes about because of gravity. The object known as 2000 CR105 is one of the \"Trans-Neptunian Objects\" that orbit our sun on elliptical paths beyond Neptune's orbit. Answer: A comet is a small celestial body, composed mainly of ice and dust, in an elliptical orbit about the Sun. The object known as 2000 CR105 is one of the \"Trans Neptunian Objects (TNOs)\" that orbit our sun on elliptical paths beyond Neptune's orbit. Comets are chunks of rock and ice that orbit the Sun in elliptical Paths. ELLIPTICAL An object in an elliptical solar orbit. That point on the path of a sun-orbiting object most distant from the center of the sun. Comet - Comets are objects which orbit the Sun in very long elliptical orbits. Escape orbit Normally we think of orbits as circular or elliptical paths that planets and other objects follow around the Sun (or any other massive body).","output":"$answer$ = a comet ; $explanation$ = A comet is often made of ice. If an object orbits a celestial object then that object is probably a celestial object as well."},
    {"type":"DA-IR-QStem","id":"ARCEZ_MCAS_2013_5_17","angle":"QC->AE","input":"$answer$ ; $explanation$ ; $question$ = One type of animal hatches from an egg, breathes through gills when it is young, and mainly lives on land as an adult. Into which group is this animal classified? ; $context$ = the larva of tadpole living in water and breathing with gills develops into an adult animal which leaves the aquatic environment and breathes with lungs like a land animal. Tadpoles metamorphose from gilled animals into air-breathing adults that are able to live on land. when the larva or tadpole living in water and breathing with gills develops into an adult, it leaves  the aquatic environment and breathes with lungs like a land animal. The animals living here breathe through their gills, or skin. These eggs hatch and the emerging larva have gills through which they &quot;breathe&quot; oxygen from the water. AMPHIBIAN Amphibians (meaning \"double life\") are vertebrate animals that live in the water during their early life (breathing through gills), but usually live on land as adults (and breathe with lungs). AMPHIBIAN (pronounced am-FIB-ee-in) Amphibians (meaning \"double life\") are vertebrate animals that live in the water during their early life (breathing through gills), but usually live on land as adults (and breathe with lungs). The eggs hatch into larvae, breathe through gills, and are herbivorous. Its tadpole stage is passed inside the egg, from which it emerges to live as an adult without gills and without lungs -- breathing through its skin. An animal (such as frog, toad or salamander) that lives in the water and breathes through gills during its early life and which breathes by its lungs and through its skin as an adult and usually spends at least part of its time on land. X1014317280-00081-18174<\/DOCNO> Glossary amphibian &#150;","output":"$answer$ = amphibians ; $explanation$ = Amphibians hatch from eggs. Young amphibians breathe through gills. Adult amphibians live on land. An amphibian is a kind of animal."},
    {"type":"DA-IR-QStem","id":"ARCEZ_MEAP_2005_8_43","angle":"QC->AE","input":"$answer$ ; $explanation$ ; $question$ = Astronauts weigh more on Earth than they do on the moon because ; $context$ = You weigh more on Earth than on the Moon because: a. On the moon the astronauts weigh less than they do on earth, why do you  think this is so ? The fingernail-sized moon rock, weighing barely more than a gram, was brought back to Earth by Apollo 17 astronauts in 1972. An object weighs more on the earth than it does on the moon because the earth has more mass than the moon.) On the Moon, the astronauts weighed about six times less than they did on the Earth. You do weigh more on Earth than you would on the moon. An astronaut walking on the Moon weighs one-sixth as much as on Earth because the net gravitational force on Earth is six times greater. On Earth, the suit weighs in at about 250 pounds, which for the astronauts would equate to wrapping themselves in something that weighs more than they do. For comparison, the astronauts on the Moon weighed 1\/6 what they weighed on Earth. (yes,y,yup,yeah,ooh yes) Do things weigh more or less on the Moon than they do on Earth?","output":"$explanation$ = The earth has more mass than the moon. As the force of gravity increases, the weight of objects will increase. As mass of a celestial body increases, the force of gravity on that planet will increase. ; $answer$ = the moon has less gravity than earth"},
    {"type":"DA-IR-QStem","id":"ARCEZ_Mercury_178728","angle":"EQC->A","input":"$answer$ ; $explanation$ = As some subatomic particles split, nuclear energy will be released. ; $question$ = When some subatomic particles split from each other, energy is released. What kind of energy is this? ; $context$ = A subatomic particle of energy charge. From this and other discoveries, scientists rapidly built up the theory that every kind of atom is made up of the same subatomic particles ( see Nuclear Energy ). That means that every single electron and subatomic particle of energy effects every other electron and subatomic particle of energy. This material decays spontaneously and releases subatomic particles and electromagnetic energy . radioactive An unstable isotope that decays spontaneously and releases subatomic particles or units of energy. When chlorophyll P680 absorbs sunlight, what subatomic particle actually has a change in energy content? The detector is designed to stop as many as possible of the subatomic particles created from energy released by colliding proton\/antiproton beams. When the nuclei change in  structure, energy and\/or subatomic particles are given off. When the particles are made to collide an electron and its anti-particle, the positron, annihilate each other releasing a high energy burst. At the subatomic level these subatomic particles are not made of energy, but they are themselves energy.","output":"$answer$ = nuclear"},
    {"type":"DA-IR-QStem","id":"ARCEZ_MCAS_2002_8_2","angle":"AC->Q","input":"$question$ ; $answer$ = primary consumers ; $context$ = Animals eat plants, and some eat other animals in the food chain. Animals that eat only plants are herbivores and, on the food chain, are called primary consumers. Food chain - consists of a series of animals that eat plants and other animals Food web - a food web consists of many food chains within an ecosystem. a. Plant and animal remains are the source of organic matter in the decomposer food chain; This sequence starts with a plant-eating animal which is the source of food for the animal(s) above it in the food chain. While being food for animals higher in the food chain, these animals may eat other animals or plants to survive. A series of animals feeding on other animals or plants and protists is called a food chain . Animals low on the food chain eat plants. Carbon-14 moves up the food chain as animals eat plants and as predators eat other animals. Other food chains are based on decomposers--organisms that feed on dead plants and animals.","output":"$question$ = In a food chain, living organisms that eat plants and are a food source for other animals are called"},
    {"type":"DA-IR-QStem","id":"ARCEZ_MEAP_2005_8_43","angle":"QAC->E","input":"$explanation$ ; $question$ = Astronauts weigh more on Earth than they do on the moon because ; $answer$ = the moon has less gravity than earth ; $context$ = You weigh more on Earth than on the Moon because: a. On the moon the astronauts weigh less than they do on earth, why do you  think this is so ? The fingernail-sized moon rock, weighing barely more than a gram, was brought back to Earth by Apollo 17 astronauts in 1972. An object weighs more on the earth than it does on the moon because the earth has more mass than the moon.) On the Moon, the astronauts weighed about six times less than they did on the Earth. You do weigh more on Earth than you would on the moon. An astronaut walking on the Moon weighs one-sixth as much as on Earth because the net gravitational force on Earth is six times greater. On Earth, the suit weighs in at about 250 pounds, which for the astronauts would equate to wrapping themselves in something that weighs more than they do. For comparison, the astronauts on the Moon weighed 1\/6 what they weighed on Earth. (yes,y,yup,yeah,ooh yes) Do things weigh more or less on the Moon than they do on Earth?","output":"$explanation$ = The earth has more mass than the moon. As the force of gravity increases, the weight of objects will increase. As mass of a celestial body increases, the force of gravity on that planet will increase."}
]

MAX_LEN_EXAMPLE_TEXT = 30
EXAMPLES_PRETTY = [""]
for e in EXAMPLES:
    prefix = f"[{e['angle']}] ({e['type']})"
    slots = decompose_slots(e['input'])
    for field in ['question', 'explanation', 'answer', 'context']:
        if field in slots and slots[field] != '':
            value = slots[field]
            if len(value) > MAX_LEN_EXAMPLE_TEXT:
                value = value[:MAX_LEN_EXAMPLE_TEXT-3] + "..."
            prefix += f" {field[0].upper()}: {value}"
            break
    EXAMPLES_PRETTY.append(f"{prefix} ({e['id']})")


def main_page(state):
    st.title("Macaw demo")
    st.write("Macaw (**M**ulti-**A**ngle **c**(q)uestion **a**ns**w**ering) - for details, see "
             "[github.com/allenai/macaw](https://github.com/allenai/macaw).")
    state.example = st.selectbox("Select example:", EXAMPLES_PRETTY, EXAMPLES_PRETTY.index(state.example) if state.example else 0)

    state.input = st.text_area("Give input by starting each line with a slot initial followed by colon. "
                               "Requested output slots are given on separate lines. "
                               "(C=Context, Q=Question, M=MCOptions, A=Answer, E=Explanation)", state.input or "",
                               height=150)

    if st.button("Get response!"):
        st.experimental_set_query_params(**{"input": state.input})
        get_response(state)

    # st.write("## Top output:")
    if state.output_slots and len(state.output_slots) > 0:
        render_output_slots(state, 0)

    if state.output_slots and len(state.output_slots) > 1:
        for index, output_slots in enumerate(state.output_slots[1:]):
            render_output_slots(state, index + 1)

    if state.explicit_outputs and len(state.explicit_outputs) > 0:
        st.write("### Explicit outputs ranked:")
        for index, explicit_output in enumerate(state.explicit_outputs):
            render_explicit_output(state, index)

    st.write("### Input:")
    if state.input_slots:
        st.write("**Requested angle:**", state.angle)
        for slot, value in state.input_slots.items():
            st.write("**"+slot+":**", value)

    if st.button("Clear all"):
        state.clear()


@st.cache
def compute_answer(raw_input, generator_options, random_tickle=1, output_strings=None):
    return_probs = {}
    if MODEL_NAME_OR_PATH is not None:
        res = run_model_demo(raw_input, **return_probs, **generator_options)
    else:
        res = {"input_raw": raw_input,
               "output_raw_list": [EXAMPLES[0]['output']]}
    res['generator_options'] = generator_options
    if output_strings is not None:
        res['explicit_outputs'] = run_model_with_outputs_demo(raw_input, output_strings)
        res['explicit_outputs'].sort(key=lambda x: -x['score'])
    log_data = res.copy()
    log_data['time'] = str(datetime.now())
    with open(LOG_FILE, 'a') as file:
        file.write(json.dumps(log_data)+"\n")
    return res


def api_compute(state_dict):
    return get_raw_response(state_dict, compute_answer_fn=compute_answer)


def get_response(state):
    state_dict = state._state["data"]
    output = get_raw_response(state_dict, compute_answer_fn=compute_answer)
    if 'input_raw' not in output:
        return None
    state.raw_input = output['input_raw']
    state.angle = output['requested_angle']
    state.raw_output = output['output_raw_list']
    state.input_slots = output['input_slots']
    state.output_slots = output['output_slots_list']
    state.beam_scores = output.get('beam_scores')
    state.token_probs = output.get('token_probs')
    state.explicit_outputs = output.get('explicit_outputs')
    state.explicit_output_angle = output.get('explicit_output_angle')


def side_effect_setters(state, item, value):
    if item == 'example':
        index = EXAMPLES_PRETTY.index(value)
        if index > 0:
            ex = EXAMPLES[index-1]
            state["data"]["input"] = make_input_from_example(ex['input'])


# Code borrowed from https://gist.github.com/okld/0aba4869ba6fdc8d49132e6974e2e662, in newer
# streamlit versions, better approaches are available
class _SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        side_effect_setters(self._state, item, value)
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        side_effect_setters(self._state, item, value)
        self._state["data"][item] = value

    def rerun(self):
        self._state["session"].request_rerun(None)

    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun(None)

    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False

        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun(None)

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")

    return session_info.session


def _get_state(hash_funcs=None):
    session = _get_session()

    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = _SessionState(session, hash_funcs)

    return session._custom_session_state


#### Setting up Flask app for REST api. This is very hacky!

if REST_API_PORT is not None and (not hasattr(st, 'already_started_server') or st.already_started_server != "Started"):
    # Use the fact that Python modules (like st) only load once to
    # keep track of whether this function already ran.
    st.already_started_server = "Started"

    from flask import Flask, request

    app = Flask("MultiAngle")
    @app.route('/api')
    def compute():
        state_dict = request.args.copy()
        return api_compute(state_dict)

    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=REST_API_PORT)
    # The following should be before app.run, but for some reason it causes things to hang
    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')
    #app.run(host='0.0.0.0', port=REST_API_PORT)

####


if __name__ == "__main__":
    main()
