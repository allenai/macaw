# Model outputs for diverse probing questions

We show the output for different sizes of Macaw (for the Q->A angle) on the 300 questions in the 
Challenge300 [probe dataset](challenge300-probes-v1.jsonl). For comparison, we also include output for
the models developed 
by [Roberts et al](https://www.aclweb.org/anthology/2020.emnlp-main.437/), based
on T5 with salient span masking and trained on NaturalQuestions, available
in the [Hugging Face model repository](https://huggingface.co/google/t5-xxl-ssm-nq). We also include the output
from the largest [GPT3 model](https://arxiv.org/pdf/2005.14165.pdf) (Davinci with 175 billion parameters), 
and [Jurassic-1](https://www.ai21.com/blog/announcing-ai21-studio-and-jurassic-1) (Jumbo model with 178 billion parameters),
both evaluated zero-shot with a simple prompt "Q: \<question text\>\nA:" and zero temperature.

For the largest models we include scores given by a human evaluator, the overall scores are:
   * Macaw-11B: 74.7%
   * Macaw-answer-11B: 76.0%
   * GPT3-davinci: 65.6%
   * Jurassic-1-jumbo: 64.8%
   * T5-XXL-SSM-NQ: 57.5%
   
A TSV file with the same data can be found in [challenge300-outputs.tsv](challenge300-outputs.tsv).

Categories: [Commonsense](#commonsense) | [Comparison](#comparison) | [Entity substitution](#entity-substitution) | [Entity tracking](#entity-tracking) | [Estimation](#estimation) | [Example generation](#example-generation) | [Explanation](#explanation) | [False presupposition](#false-presupposition) | [General knowledge](#general-knowledge) | [Generation](#generation) | [History](#history) | [Human behavior](#human-behavior) | [Hypothetical](#hypothetical) | [Math](#math) | [Meta-reasoning](#meta-reasoning) | [Riddle](#riddle) | [Science](#science) | [Spatial](#spatial) | [Steps](#steps) | [Story understanding](#story-understanding) | [Temporal](#temporal) | [Winograd](#Winograd)

## Commonsense

Q1: <b>If I put some cheese in the fridge, will it melt?</b>
   * Macaw-11B: <b>no, because it will be solid</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>no</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>No, it will become cold and hard.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No. Cheese is a dairy product, and dairy products do not melt.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>will not melt</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>will not melt</b>
   * T5-XL-SSM-NQ: <b>will it solidify</b>
   * T5-large-SSM-NQ: <b>20 minutes</b>
   * T5-small-SSM-NQ: <b>If I Were There</b>

Q2: <b>How could one divert an asteroid heading directly for the Earth?</b>
   * Macaw-11B: <b>launch a space shuttle into orbit around it</b> (credit: 0)
   * Macaw-3B: <b>destroying it</b>
   * Macaw-large: <b>use a gravity diversion</b>
   * Macaw-answer-11B: <b>create a spacecraft to intercept and deflect the asteroid</b> (credit: 1)
   * GPT3-davinci: <b>The most effective way to divert an asteroid is to nudge it slightly off course with a spacecraft. This can be done by using a spacecraft to push on the asteroid, or by using a spacecraft to push on the Earth, which in turn pushes on the asteroid.
Asteroids are small enough that they are affected</b> (credit: 1)
   * Jurassic-1-jumbo: <b>By hitting it with an ion beam.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>gravity</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Space debris</b>
   * T5-XL-SSM-NQ: <b>using a spaceship</b>
   * T5-large-SSM-NQ: <b>Earth-direction shield</b>
   * T5-small-SSM-NQ: <b>A simple explanation</b>

Q3: <b>How can I build a tent if I only have a tarpaulin, a tent peg, and a piece of rope?</b>
   * Macaw-11B: <b>make a frame</b> (credit: 0)
   * Macaw-3B: <b>i can use the rope to tie the tarp to the tent pegs</b>
   * Macaw-large: <b>use two pieces of wood</b>
   * Macaw-answer-11B: <b>make a frame</b> (credit: 0.5)
   * GPT3-davinci: <b>You can build a tent by making a frame with the rope and the tent peg, and then covering it with the tarpaulin.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>First, tie the rope to the tent peg. Then, tie the rope to the tarpaulin. Finally, tie the rope to the tent peg again.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>three simple steps</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>"Rain gutter"</b>
   * T5-XL-SSM-NQ: <b>mechanized way</b>
   * T5-large-SSM-NQ: <b>A simple tarpaulin or canvas</b>
   * T5-small-SSM-NQ: <b>insulation</b>

Q4: <b>How can I make a tent using a tarpaulin, a tent peg, and a piece of rope?</b>
   * Macaw-11B: <b>tie the tarpaulin to the tent pegs</b> (credit: 0)
   * Macaw-3B: <b>tie them together</b>
   * Macaw-large: <b>attach a few pieces of wood together and you have a shelter</b>
   * Macaw-answer-11B: <b>tie the tarpaulin to the rope</b> (credit: 0)
   * GPT3-davinci: <b>You can make a tent using a tarpaulin, a tent peg, and a piece of rope.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>First, tie the rope to the tent peg. Then, tie the rope to the tarpaulin. Finally, put the tent peg into the ground.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>three lines</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>make a simple shelter</b>
   * T5-XL-SSM-NQ: <b>simple way</b>
   * T5-large-SSM-NQ: <b>"Peg"</b>
   * T5-small-SSM-NQ: <b>insulation</b>

Q5: <b>I would like to go running, but my ankle is injured. What should I do?</b>
   * Macaw-11B: <b>ice it</b> (credit: 1)
   * Macaw-3B: <b>rest</b>
   * Macaw-large: <b>rest and ice my ankle</b>
   * Macaw-answer-11B: <b>ice it</b> (credit: 1)
   * GPT3-davinci: <b>If you have a minor injury, you can still go running. Just take it easy and don't overdo it. If you have a major injury, you should probably take a break from running.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Running on an injured ankle is a bad idea. It can lead to further injury, and prolong your recovery.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>ice</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>rest</b>
   * T5-XL-SSM-NQ: <b>rest</b>
   * T5-large-SSM-NQ: <b>stretch</b>
   * T5-small-SSM-NQ: <b>with exaggerated physical activity</b>

Q6: <b>If I went hiking for the day, how much water should I bring with me?</b>
   * Macaw-11B: <b>2 liters</b> (credit: 1)
   * Macaw-3B: <b>2 liters</b>
   * Macaw-large: <b>2 liters</b>
   * Macaw-answer-11B: <b>1 liter</b> (credit: 1)
   * GPT3-davinci: <b>It depends on the length of your hike, the temperature, and your level of activity. If you are hiking in the desert, you will need more water than if you are hiking in the mountains. If you are hiking in the summer, you will need more water than if you are hiking in the winter. If you</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>The amount of water you should bring with you depends on the length of your hike, the weather conditions, and your physical condition.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>at least 2 L</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>1 litre per person</b>
   * T5-XL-SSM-NQ: <b>1 litre</b>
   * T5-large-SSM-NQ: <b>2 litres</b>
   * T5-small-SSM-NQ: <b>$2,350</b>

Q7: <b>The judge killed the suspect. Who did the police arrest?</b>
   * Macaw-11B: <b>the judge</b> (credit: 1)
   * Macaw-3B: <b>the judge</b>
   * Macaw-large: <b>the suspect</b>
   * Macaw-answer-11B: <b>the judge</b> (credit: 1)
   * GPT3-davinci: <b>The judge.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The judge.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>his partner</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Jones</b>
   * T5-XL-SSM-NQ: <b>Billy</b>
   * T5-large-SSM-NQ: <b>Richard Ramirez</b>
   * T5-small-SSM-NQ: <b>Deb</b>

Q8: <b>The suspect killed the judge. Who did the police arrest?</b>
   * Macaw-11B: <b>the suspect</b> (credit: 1)
   * Macaw-3B: <b>the suspect</b>
   * Macaw-large: <b>the suspect</b>
   * Macaw-answer-11B: <b>the suspect's wife</b> (credit: 0)
   * GPT3-davinci: <b>The suspect's brother.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The suspect killed the judge.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>John Doe</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Thomas McAllister</b>
   * T5-XL-SSM-NQ: <b>Robert Durst</b>
   * T5-large-SSM-NQ: <b>Richard Ramirez</b>
   * T5-small-SSM-NQ: <b>Deb</b>

Q9: <b>The man killed the murderer. Who did the police arrest?</b>
   * Macaw-11B: <b>the man who killed the murderer</b> (credit: 1)
   * Macaw-3B: <b>the murderer</b>
   * Macaw-large: <b>the man</b>
   * Macaw-answer-11B: <b>the man who killed the murderer</b> (credit: 1)
   * GPT3-davinci: <b>The man's brother.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The murderer.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>the man</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>Ramirez</b>
   * T5-XL-SSM-NQ: <b>the other man</b>
   * T5-large-SSM-NQ: <b>Robert William Fisher</b>
   * T5-small-SSM-NQ: <b>8 a.m. Paris time</b>

Q10: <b>The murderer killed the man. Who did the police arrest?</b>
   * Macaw-11B: <b>the murderer</b> (credit: 1)
   * Macaw-3B: <b>the murderer</b>
   * Macaw-large: <b>the man</b>
   * Macaw-answer-11B: <b>the murderer</b> (credit: 1)
   * GPT3-davinci: <b>The murderer.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The murderer.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>John</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Jones</b>
   * T5-XL-SSM-NQ: <b>John Wayne Gacy</b>
   * T5-large-SSM-NQ: <b>Robert William Fisher</b>
   * T5-small-SSM-NQ: <b>8 a.m. Paris time</b>

Q11: <b>The dax killed the murderer. Who did the police arrest?</b>
   * Macaw-11B: <b>the dax</b> (credit: 1)
   * Macaw-3B: <b>the murderer</b>
   * Macaw-large: <b>the dax</b>
   * Macaw-answer-11B: <b>the dog</b> (credit: 0)
   * GPT3-davinci: <b>The dax.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The dax killed the murderer.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>O'Brien</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Lucas</b>
   * T5-XL-SSM-NQ: <b>O'Brien</b>
   * T5-large-SSM-NQ: <b>Norman</b>
   * T5-small-SSM-NQ: <b>13</b>

Q12: <b>What happens if I drop a  glass on a bed of feathers?</b>
   * Macaw-11B: <b>the glass shatters</b> (credit: 0)
   * Macaw-3B: <b>the feathers will stay in place</b>
   * Macaw-large: <b>the glass breaks</b>
   * Macaw-answer-11B: <b>the glass will break</b> (credit: 0)
   * GPT3-davinci: <b>The glass will break, the feathers will go up in the air.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>The glass shatters, the feathers fly, and the bed collapses.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>no harm done</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>it will not break</b>
   * T5-XL-SSM-NQ: <b>will it crumple</b>
   * T5-large-SSM-NQ: <b>stays put</b>
   * T5-small-SSM-NQ: <b>blowout</b>

Q13: <b>What is made of metal?</b>
   * Macaw-11B: <b>a car</b> (credit: 1)
   * Macaw-3B: <b>coins</b>
   * Macaw-large: <b>metals</b>
   * Macaw-answer-11B: <b>car</b> (credit: 1)
   * GPT3-davinci: <b>The metal is made of metal.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A metal is a chemical element that is a good conductor of heat and electricity.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>an iron rod</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>car parts</b>
   * T5-XL-SSM-NQ: <b>metal objects</b>
   * T5-large-SSM-NQ: <b>Bridges</b>
   * T5-small-SSM-NQ: <b>Mining</b>

Q14: <b>What is made of metal, besides a car?</b>
   * Macaw-11B: <b>a door</b> (credit: 1)
   * Macaw-3B: <b>a bicycle</b>
   * Macaw-large: <b>a boat</b>
   * Macaw-answer-11B: <b>a dog</b> (credit: 0)
   * GPT3-davinci: <b>A coffin.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A car.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>a metal detector</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>canoes</b>
   * T5-XL-SSM-NQ: <b>a metal can</b>
   * T5-large-SSM-NQ: <b>hardware</b>
   * T5-small-SSM-NQ: <b>a metal mine or aluminum</b>

Q15: <b>What is made of metal, besides a car and a door?</b>
   * Macaw-11B: <b>a bicycle</b> (credit: 1)
   * Macaw-3B: <b>a bicycle</b>
   * Macaw-large: <b>a door</b>
   * Macaw-answer-11B: <b>a dog's collar</b> (credit: 0)
   * GPT3-davinci: <b>A coffin.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A metal door.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>a spoon</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>canoes</b>
   * T5-XL-SSM-NQ: <b>a metal frame</b>
   * T5-large-SSM-NQ: <b>other durable means of transport</b>
   * T5-small-SSM-NQ: <b>metal-to-layers</b>

Q16: <b>What is made of metal, besides a car, a door, and a bicycle?</b>
   * Macaw-11B: <b>a spoon</b> (credit: 1)
   * Macaw-3B: <b>a bicycle</b>
   * Macaw-large: <b>a door</b>
   * Macaw-answer-11B: <b>a refrigerator</b> (credit: 1)
   * GPT3-davinci: <b>A coffin.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A metal door, a bicycle, and a car.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>a spoon</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>most durable materials</b>
   * T5-XL-SSM-NQ: <b>a fork</b>
   * T5-large-SSM-NQ: <b>other durable means of transport</b>
   * T5-small-SSM-NQ: <b>Formed by a vehicle</b>

Q17: <b>You are a defense lawyer and you have to go to court today. Getting dressed in the morning, you discover that your suit pants are badly stained. However, your bathing suit is clean and very stylish. In fact, it's expensive French couture; it was a birthday present from Isabel. You decide that you should wear what?</b>
   * Macaw-11B: <b>the bathing suit</b> (credit: 0)
   * Macaw-3B: <b>your bathing suit</b>
   * Macaw-large: <b>a white T-shirt and black boxer shorts</b>
   * Macaw-answer-11B: <b>bathing suit</b> (credit: 0)
   * GPT3-davinci: <b>The bathing suit.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The bathing suit. It's French couture.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>bathing suit</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the bathing suit</b>
   * T5-XL-SSM-NQ: <b>a suit</b>
   * T5-large-SSM-NQ: <b>Jeans</b>
   * T5-small-SSM-NQ: <b>Chanel's crest</b>

Q18: <b>You poured yourself a glass of cranberry juice, but then absentmindedly, you poured about a teaspoon of grape juice into it. It looks OK. You try sniffing it, but you have a bad cold, so you can't smell anything. You are very thirsty. So you drink it. What happens next?</b>
   * Macaw-11B: <b>you get sick</b> (credit: 0)
   * Macaw-3B: <b>it tastes like grape juice</b>
   * Macaw-large: <b>your body breaks down the grapes in your drink</b>
   * Macaw-answer-11B: <b>you get sick</b> (credit: 0)
   * GPT3-davinci: <b>You will probably die.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>You die. The grape juice contains enough poison to kill you.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>you get a headache</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>a bad headache</b>
   * T5-XL-SSM-NQ: <b>The juice is tart</b>
   * T5-large-SSM-NQ: <b>You have a cold</b>
   * T5-small-SSM-NQ: <b>a tuberculosis</b>

Q19: <b>If you break a glass bottle that holds toy soldiers, the toy soldiers will probably what?</b>
   * Macaw-11B: <b>fall out</b> (credit: 1)
   * Macaw-3B: <b>break</b>
   * Macaw-large: <b>break apart</b>
   * Macaw-answer-11B: <b>fall out</b> (credit: 1)
   * GPT3-davinci: <b>Fall out.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Break the bottle.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>fall out</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>spill</b>
   * T5-XL-SSM-NQ: <b>will fall out</b>
   * T5-large-SSM-NQ: <b>explode</b>
   * T5-small-SSM-NQ: <b>For a glass bottle</b>

Q20: <b>You order a bowl of cold tomato soup in a restaurant. It looks delicious, but they forgot to bring you a spoon. You try to drink it using your eyeglasses. What happens?</b>
   * Macaw-11B: <b>it spills</b> (credit: 0.5)
   * Macaw-3B: <b>you get stung</b>
   * Macaw-large: <b>the soup is too hot to drink</b>
   * Macaw-answer-11B: <b>it spills</b> (credit: 0.5)
   * GPT3-davinci: <b>You get a headache.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The soup gets in your glasses.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a spoonful of sugar</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>splashes all over your shirt</b>
   * T5-XL-SSM-NQ: <b>swill</b>
   * T5-large-SSM-NQ: <b>you are shocked</b>
   * T5-small-SSM-NQ: <b>a brothel</b>

Q21: <b>Can I cut a potato with a knife?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>Yes, but it's not recommended.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Yes, you can cut a potato with a knife.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Yes</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>with my fingers</b>
   * T5-XL-SSM-NQ: <b>Can I use a knife</b>
   * T5-large-SSM-NQ: <b>Yes</b>
   * T5-small-SSM-NQ: <b>to cut a hand</b>

Q22: <b>Can I cut a steel beam with a knife?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>Yes, but it will take a long time.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>No, steel is too hard.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>No</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>no</b>
   * T5-XL-SSM-NQ: <b>with a hacksaw</b>
   * T5-large-SSM-NQ: <b>Yes</b>
   * T5-small-SSM-NQ: <b>hack a knife</b>

Q23: <b>Can I cut a brick with a knife?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>Yes, but it's not easy.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Yes, but it takes a lot of force.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>No</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>with some effort</b>
   * T5-XL-SSM-NQ: <b>Can I hack a brick with a knife</b>
   * T5-large-SSM-NQ: <b>a knife</b>
   * T5-small-SSM-NQ: <b>hand</b>

Q24: <b>What can't I cut with a knife?</b>
   * Macaw-11B: <b>bones</b> (credit: 1)
   * Macaw-3B: <b>bones</b>
   * Macaw-large: <b>metal</b>
   * Macaw-answer-11B: <b>metal</b> (credit: 1)
   * GPT3-davinci: <b>You can't cut anything that's alive.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Your finger.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>glass</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>bone</b>
   * T5-XL-SSM-NQ: <b>easily penetrated by hand</b>
   * T5-large-SSM-NQ: <b>metal</b>
   * T5-small-SSM-NQ: <b>hack a knife</b>

Q25: <b>Can I cut a bone with a knife?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>Yes, but it's not recommended.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Yes, you can cut a bone with a knife.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>A knife can cut through bone</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>bone saw</b>
   * T5-XL-SSM-NQ: <b>with the tapper</b>
   * T5-large-SSM-NQ: <b>Yes</b>
   * T5-small-SSM-NQ: <b>Knife</b>

Q26: <b>Does a coral snake have legs?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>No, a coral snake is a legless reptile.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, a coral snake does not have legs.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>four</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>slender, legless</b>
   * T5-XL-SSM-NQ: <b>have both legs</b>
   * T5-large-SSM-NQ: <b>many</b>
   * T5-small-SSM-NQ: <b>southernmost silt</b>

Q27: <b>Does a king cobra have legs?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>No, a king cobra is a legless snake.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, a king cobra does not have legs.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>8</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>talons</b>
   * T5-XL-SSM-NQ: <b>have both legs</b>
   * T5-large-SSM-NQ: <b>lower back legs</b>
   * T5-small-SSM-NQ: <b>between a king and a man</b>

Q28: <b>Do snakes have legs?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>No, snakes are legless.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, snakes do not have legs.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>four</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>not</b>
   * T5-XL-SSM-NQ: <b>snakes</b>
   * T5-large-SSM-NQ: <b>do not have legs</b>
   * T5-small-SSM-NQ: <b>mute Norma Romano</b>

Q29: <b>How does a snake move around?</b>
   * Macaw-11B: <b>by slithering on all fours</b> (credit: 0)
   * Macaw-3B: <b>slithering</b>
   * Macaw-large: <b>bouncing on its back legs</b>
   * Macaw-answer-11B: <b>by wriggling</b> (credit: 1)
   * GPT3-davinci: <b>Snakes move by using their muscles to push against the ground. They can move in any direction, but they cannot move backwards.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Snakes move by slithering.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>hiss</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>by wriggling</b>
   * T5-XL-SSM-NQ: <b>uncoiled</b>
   * T5-large-SSM-NQ: <b>its antlers</b>
   * T5-small-SSM-NQ: <b>Through a tensor fasciae latae muscle</b>

Q30: <b>Can you sit and stand at the same time?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>No.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Yes, you can sit and stand at the same time.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b></b> (credit: 0)
   * T5-11B-SSM-NQ: <b>can't</b>
   * T5-XL-SSM-NQ: <b>a tripod</b>
   * T5-large-SSM-NQ: <b>isovolumic movement</b>
   * T5-small-SSM-NQ: <b>'early Polley</b>

Q31: <b>Can you walk and run at the same time?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>Yes, you can.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Yes, you can. In fact, most runners do.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>can't</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>alternating gait</b>
   * T5-XL-SSM-NQ: <b>Can't</b>
   * T5-large-SSM-NQ: <b>walking</b>
   * T5-small-SSM-NQ: <b>walking with the start</b>

Q32: <b>Joe is sitting. Can Joe now stand while remaining seated?</b>
   * Macaw-11B: <b>no</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>no, he must sit still</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>No. Joe is not allowed to stand while remaining seated.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No. Joe must stand first, then sit.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>both yes and no</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>can't</b>
   * T5-XL-SSM-NQ: <b>can walk</b>
   * T5-large-SSM-NQ: <b>standing</b>
   * T5-small-SSM-NQ: <b>sit all citizens</b>

Q33: <b>Joe is walking. Can Joe now run while still walking?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>walk</b>
   * Macaw-answer-11B: <b>no, he can't run while walking</b> (credit: 1)
   * GPT3-davinci: <b>No. Joe must stop walking and start running.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No. Joe cannot run while still walking.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>simultaneously</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>running</b>
   * T5-XL-SSM-NQ: <b>can walk, can run</b>
   * T5-large-SSM-NQ: <b>Joe</b>
   * T5-small-SSM-NQ: <b>a song</b>

Q34: <b>Malcolm Harrison was a farmer in Virginia who died more than 200 years ago. He had a dozen horses on his farm. How many horses will still be alive today?</b>
   * Macaw-11B: <b>1</b> (credit: 0)
   * Macaw-3B: <b>six</b>
   * Macaw-large: <b>12</b>
   * Macaw-answer-11B: <b>zero</b> (credit: 1)
   * GPT3-davinci: <b>None.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>None. All horses are descended from one mare, which lived about 50,000 years ago.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>two</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>two</b>
   * T5-XL-SSM-NQ: <b>one</b>
   * T5-large-SSM-NQ: <b>100</b>
   * T5-small-SSM-NQ: <b>100</b>

Q35: <b>Mary owns a canary named Paul. Did Paul has any ancestors who were alive in the year 1750?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>No.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>No, Paul is a canary, not a human.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>Paul</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>probably not</b>
   * T5-XL-SSM-NQ: <b>any living relatives</b>
   * T5-large-SSM-NQ: <b>any of his siblings</b>
   * T5-small-SSM-NQ: <b>Andrew (John Dye)</b>

Q36: <b>Can a female eagle and a male alligator have a baby together?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>No, because alligators are reptiles and eagles are birds.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, because eagles and alligators are from different families.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Yes</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>can have offspring</b>
   * T5-XL-SSM-NQ: <b>can't</b>
   * T5-large-SSM-NQ: <b>alligators</b>
   * T5-small-SSM-NQ: <b>between a male and a male</b>

Q37: <b>When Ed was born, his father was in Boston and his mother was in Los Angeles. Where was Ed born?</b>
   * Macaw-11B: <b>los angeles</b> (credit: 1)
   * Macaw-3B: <b>los angeles</b>
   * Macaw-large: <b>california</b>
   * Macaw-answer-11B: <b>Los Angeles</b> (credit: 1)
   * GPT3-davinci: <b>Ed was born in Los Angeles.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Ed was born in Boston.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>Los Angeles</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>Los Angeles</b>
   * T5-XL-SSM-NQ: <b>Los Angeles</b>
   * T5-large-SSM-NQ: <b>Los Angeles</b>
   * T5-small-SSM-NQ: <b>Chicago</b>

Q38: <b>If a person cuts off one of his fingers, then can the person grow a new finger?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>Yes, the person can grow a new finger.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>No, because Allah (subhana wa ta'ala) has decreed that He will not grow a new finger.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>in some cases</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>will grow back</b>
   * T5-XL-SSM-NQ: <b>can grow new fingers</b>
   * T5-large-SSM-NQ: <b>from the bone</b>
   * T5-small-SSM-NQ: <b>About twice a hand</b>

## Comparison

Q39: <b>How do pandas and parrots differ?</b>
   * Macaw-11B: <b>pandas have black and white fur, parrots have bright colors and are feathered</b> (credit: 1)
   * Macaw-3B: <b>parrots have feathers</b>
   * Macaw-large: <b>able to swim</b>
   * Macaw-answer-11B: <b>pandas have thicker fur and are larger than parrots</b> (credit: 1)
   * GPT3-davinci: <b>Pandas are black and white, and parrots are green and blue.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Pandas eat bamboo, and parrots eat seeds.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>in their bills</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>diet</b>
   * T5-XL-SSM-NQ: <b>heirlooms</b>
   * T5-large-SSM-NQ: <b>main difference being in size</b>
   * T5-small-SSM-NQ: <b>pancreatic cancer</b>

Q40: <b>What is the difference between a noun and a verb?</b>
   * Macaw-11B: <b>a verb describes an action while a noun is used to describe something</b> (credit: 1)
   * Macaw-3B: <b>a noun is a kind of object while a verb is a kind of action</b>
   * Macaw-large: <b>nouns can be used to describe things</b>
   * Macaw-answer-11B: <b>a verb expresses action, a noun describes things</b> (credit: 1)
   * GPT3-davinci: <b>A noun is a person, place, or thing. A verb is a person, place, or thing.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A noun names a person, place, thing, or idea. A verb names an action or state of being.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>usually spelling</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>action</b>
   * T5-XL-SSM-NQ: <b>morphemes</b>
   * T5-large-SSM-NQ: <b>The noun is a modifier</b>
   * T5-small-SSM-NQ: <b>the noun</b>

## Entity substitution

Q41: <b>James went camping in the woods, but forgot to bring a hammer to bang the tent pegs in. What else might he use?</b>
   * Macaw-11B: <b>rocks</b> (credit: 1)
   * Macaw-3B: <b>a stick</b>
   * Macaw-large: <b>a chisel</b>
   * Macaw-answer-11B: <b>rocks</b> (credit: 1)
   * GPT3-davinci: <b>His head.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A rock.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a rock</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>a rock</b>
   * T5-XL-SSM-NQ: <b>a sledgehammer</b>
   * T5-large-SSM-NQ: <b>a woodpecker</b>
   * T5-small-SSM-NQ: <b>a carousel tribute</b>

Q42: <b>How would you remove ice from the car window without an ice scraper?</b>
   * Macaw-11B: <b>scrape it with a knife</b> (credit: 1)
   * Macaw-3B: <b>use a hair dryer</b>
   * Macaw-large: <b>use a swab</b>
   * Macaw-answer-11B: <b>scrape it with a knife</b> (credit: 1)
   * GPT3-davinci: <b>Use a piece of ice.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Use a credit card.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a credit card</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>by hand</b>
   * T5-XL-SSM-NQ: <b>a cold glass</b>
   * T5-large-SSM-NQ: <b>a mirror</b>
   * T5-small-SSM-NQ: <b>to remove ice</b>

Q43: <b>How would you bang in tent pegs without a hammer?</b>
   * Macaw-11B: <b>use a rock</b> (credit: 1)
   * Macaw-3B: <b>a stick</b>
   * Macaw-large: <b>use a chisel</b>
   * Macaw-answer-11B: <b>use a rock</b> (credit: 1)
   * GPT3-davinci: <b>Use a rock.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You bang them in with a tent peg.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a maul</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>with your bare hands</b>
   * T5-XL-SSM-NQ: <b>pound them in with a mallet</b>
   * T5-large-SSM-NQ: <b>hang a hook</b>
   * T5-small-SSM-NQ: <b>a scarlet horn</b>

Q44: <b>Mary wanted to heat up some water, but her stove was broken. What else might she use instead to heat the water?</b>
   * Macaw-11B: <b>a campfire</b> (credit: 1)
   * Macaw-3B: <b>a campfire</b>
   * Macaw-large: <b>an electric fire</b>
   * Macaw-answer-11B: <b>microwave</b> (credit: 1)
   * GPT3-davinci: <b>Mary could use a microwave to heat the water.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Mary could use a solar oven.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>microwave oven</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>an electric kettle</b>
   * T5-XL-SSM-NQ: <b>a frying pan</b>
   * T5-large-SSM-NQ: <b>a bowl</b>
   * T5-small-SSM-NQ: <b>salt</b>

## Entity tracking

Q45: <b>John was in the bedroom. John put a coin in a bag. Then John took the bag to the kitchen. Then John took the coin out of the bag. John took the bag to the garden. Where was the coin at the start?</b>
   * Macaw-11B: <b>bedroom</b> (credit: 1)
   * Macaw-3B: <b>bedroom</b>
   * Macaw-large: <b>in the bedroom</b>
   * Macaw-answer-11B: <b>bedroom</b> (credit: 1)
   * GPT3-davinci: <b>In the bag.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>In the bedroom.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>in the bag</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>in the bedroom</b>
   * T5-XL-SSM-NQ: <b>bedroom</b>
   * T5-large-SSM-NQ: <b>the bedroom</b>
   * T5-small-SSM-NQ: <b>a car</b>

Q46: <b>John was in the bedroom. John put a coin in a bag. Then John took the bag to the kitchen. Then John took the coin out of the bag. John took the bag to the garden. Where was the coin at the end?</b>
   * Macaw-11B: <b>in the kitchen</b> (credit: 1)
   * Macaw-3B: <b>in the kitchen</b>
   * Macaw-large: <b>in the kitchen</b>
   * Macaw-answer-11B: <b>in the bag</b> (credit: 0)
   * GPT3-davinci: <b>In the bag.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>In the bag.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>in the kitchen</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>in the garden</b>
   * T5-XL-SSM-NQ: <b>in a bag</b>
   * T5-large-SSM-NQ: <b>the bathroom floor</b>
   * T5-small-SSM-NQ: <b>a car</b>

Q47: <b>John was in the bedroom. John put a coin in a bag. Then John took the bag to the kitchen. Then John took the coin out of the bag. John took the bag to the garden. Where was the bag at the end?</b>
   * Macaw-11B: <b>in the kitchen</b> (credit: 0)
   * Macaw-3B: <b>in the kitchen</b>
   * Macaw-large: <b>in the kitchen</b>
   * Macaw-answer-11B: <b>kitchen</b> (credit: 0)
   * GPT3-davinci: <b>In the garden.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>In the kitchen.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>in the garden</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>in the garden</b>
   * T5-XL-SSM-NQ: <b>in the garden</b>
   * T5-large-SSM-NQ: <b>the back of the room</b>
   * T5-small-SSM-NQ: <b>a car accident</b>

Q48: <b>Imagine an empty cup. Now put a coin in the cup. Now put another coin in the cup. Now put a pen in the cup. How many coins are in the cup now?</b>
   * Macaw-11B: <b>3</b> (credit: 0)
   * Macaw-3B: <b>three</b>
   * Macaw-large: <b>three</b>
   * Macaw-answer-11B: <b>2</b> (credit: 1)
   * GPT3-davinci: <b>One.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>2 coins and a pen.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>three</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>three</b>
   * T5-XL-SSM-NQ: <b>two</b>
   * T5-large-SSM-NQ: <b>four</b>
   * T5-small-SSM-NQ: <b>one</b>

Q49: <b>Imagine an empty cup. Now put a coin in the cup. Now take the coin out of the cup. How many coins are in the cup now?</b>
   * Macaw-11B: <b>1</b> (credit: 0)
   * Macaw-3B: <b>one</b>
   * Macaw-large: <b>one</b>
   * Macaw-answer-11B: <b>1</b> (credit: 0)
   * GPT3-davinci: <b>None.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>None. The cup is empty.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>two</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>one</b>
   * T5-XL-SSM-NQ: <b>two</b>
   * T5-large-SSM-NQ: <b>four</b>
   * T5-small-SSM-NQ: <b>Two</b>

Q50: <b>My house is red. I painted my house white. What color is my house now?</b>
   * Macaw-11B: <b>it is now white</b> (credit: 1)
   * Macaw-3B: <b>white</b>
   * Macaw-large: <b>white</b>
   * Macaw-answer-11B: <b>white</b> (credit: 1)
   * GPT3-davinci: <b>It's still red.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Red.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>white</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>red</b>
   * T5-XL-SSM-NQ: <b>mid-garter color</b>
   * T5-large-SSM-NQ: <b>red</b>
   * T5-small-SSM-NQ: <b>The Hoosier</b>

Q51: <b>My house is blue. I painted my house red. What color was my house before I painted it?</b>
   * Macaw-11B: <b>blue</b> (credit: 1)
   * Macaw-3B: <b>blue</b>
   * Macaw-large: <b>black</b>
   * Macaw-answer-11B: <b>blue</b> (credit: 1)
   * GPT3-davinci: <b>It was blue.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Your house was blue.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>blue</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>blue</b>
   * T5-XL-SSM-NQ: <b>white</b>
   * T5-large-SSM-NQ: <b>white</b>
   * T5-small-SSM-NQ: <b>The Homophonic</b>

Q52: <b>My house is red. My neighbor's house is blue. I painted my house white. What color is my house now?</b>
   * Macaw-11B: <b>it's the same color as my neighbor's house</b> (credit: 0)
   * Macaw-3B: <b>white</b>
   * Macaw-large: <b>white</b>
   * Macaw-answer-11B: <b>neither red nor blue</b> (credit: 0)
   * GPT3-davinci: <b>It's still red.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Your house is now purple.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>white</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>blue</b>
   * T5-XL-SSM-NQ: <b>yellow</b>
   * T5-large-SSM-NQ: <b>red</b>
   * T5-small-SSM-NQ: <b>None</b>

Q53: <b>My house is red. I painted my neighbor's house white. What color is my house now?</b>
   * Macaw-11B: <b>half red, half white</b> (credit: 0)
   * Macaw-3B: <b>white</b>
   * Macaw-large: <b>red</b>
   * Macaw-answer-11B: <b>red</b> (credit: 1)
   * GPT3-davinci: <b>It's still red.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Your house is now purple.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>white</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>white</b>
   * T5-XL-SSM-NQ: <b>white</b>
   * T5-large-SSM-NQ: <b>white</b>
   * T5-small-SSM-NQ: <b>None</b>

Q54: <b>I bought a ticket to Hawaii. Where is the ticket now?</b>
   * Macaw-11B: <b>in my wallet</b> (credit: 1)
   * Macaw-3B: <b>in my wallet</b>
   * Macaw-large: <b>in a drawer in my closet</b>
   * Macaw-answer-11B: <b>in my wallet</b> (credit: 1)
   * GPT3-davinci: <b>The ticket is in your hands.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The ticket is with the airline.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>in a safe place</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>in my wallet</b>
   * T5-XL-SSM-NQ: <b>in a drawer</b>
   * T5-large-SSM-NQ: <b>The Internet</b>
   * T5-small-SSM-NQ: <b>have a good trip</b>

Q55: <b>I bought a ticket to Hawaii. Where was the ticket before?</b>
   * Macaw-11B: <b>new york</b> (credit: 0)
   * Macaw-3B: <b>my wallet</b>
   * Macaw-large: <b>california</b>
   * Macaw-answer-11B: <b>the airport</b> (credit: 1)
   * GPT3-davinci: <b>The ticket was in the possession of the airline.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The ticket was in the computer.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Los Angeles</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>under the mat</b>
   * T5-XL-SSM-NQ: <b>San Francisco</b>
   * T5-large-SSM-NQ: <b>the Eiffel Tower</b>
   * T5-small-SSM-NQ: <b>Hawaii</b>

Q56: <b>I bought a ticket to Hawaii from a local travel agent. Where was the ticket before?</b>
   * Macaw-11B: <b>in a computer</b> (credit: 1)
   * Macaw-3B: <b>my wallet</b>
   * Macaw-large: <b>in the mail</b>
   * Macaw-answer-11B: <b>in a computer</b> (credit: 1)
   * GPT3-davinci: <b>The ticket was issued by a travel agency in Hawaii.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The ticket was most likely sold to you by a travel agent. The travel agent may have purchased the ticket from an airline or from an airline consolidator.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>at the travel agency</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>from a third party</b>
   * T5-XL-SSM-NQ: <b>a Honolulu travel agency</b>
   * T5-large-SSM-NQ: <b>Kay Bailey Hutchison</b>
   * T5-small-SSM-NQ: <b>Hawaii</b>

Q57: <b>Amy, Betty, Charlie, David, Ezra, Flip, and George go to a party; Betty and Charlie got bored; Ezra and Flip go out to get beer. The only people left are who?</b>
   * Macaw-11B: <b>Amy and David</b> (credit: 0)
   * Macaw-3B: <b>flip and george</b>
   * Macaw-large: <b>gilbert and john</b>
   * Macaw-answer-11B: <b>Amy and David</b> (credit: 0)
   * GPT3-davinci: <b>Amy and David.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Amy, Betty, David, and George.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>David</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Amy</b>
   * T5-XL-SSM-NQ: <b>George</b>
   * T5-large-SSM-NQ: <b>George</b>
   * T5-small-SSM-NQ: <b>Mrs. Svorski</b>

## Estimation

Q58: <b>How many banknotes can you fit in a school bus?</b>
   * Macaw-11B: <b>5000</b> (credit: 0)
   * Macaw-3B: <b>a hundred</b>
   * Macaw-large: <b>50</b>
   * Macaw-answer-11B: <b>a lot</b> (credit: 0)
   * GPT3-davinci: <b>About $1.5 million.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>$58.78</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>96,700</b>
   * T5-XL-SSM-NQ: <b>165,372</b>
   * T5-large-SSM-NQ: <b>Approximately 24</b>
   * T5-small-SSM-NQ: <b>a single banknote</b>

Q59: <b>How many banknotes can you fit in a wallet?</b>
   * Macaw-11B: <b>100</b> (credit: 1)
   * Macaw-3B: <b>10</b>
   * Macaw-large: <b>50</b>
   * Macaw-answer-11B: <b>about 20</b> (credit: 1)
   * GPT3-davinci: <b>Depends on the size of the wallet.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>10</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>ten</b>
   * T5-XL-SSM-NQ: <b>15</b>
   * T5-large-SSM-NQ: <b>up to 100</b>
   * T5-small-SSM-NQ: <b>325</b>

Q60: <b>How many banknotes can you fit in a thimble?</b>
   * Macaw-11B: <b>one</b> (credit: 1)
   * Macaw-3B: <b>one</b>
   * Macaw-large: <b>50</b>
   * Macaw-answer-11B: <b>one</b> (credit: 1)
   * GPT3-davinci: <b>None.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>None, because thimbles don't have pockets.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>ten</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>24</b>
   * T5-XL-SSM-NQ: <b>five</b>
   * T5-large-SSM-NQ: <b>five</b>
   * T5-small-SSM-NQ: <b>five</b>

Q61: <b>How many truckloads of earth does Mount Everest contain?</b>
   * Macaw-11B: <b>a million</b> (credit: 1)
   * Macaw-3B: <b>a million</b>
   * Macaw-large: <b>8 million</b>
   * Macaw-answer-11B: <b>a lot</b> (credit: 0)
   * GPT3-davinci: <b>About 1.5 million truckloads.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>1.5 million truckloads.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>185 million</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>about 6.5 million</b>
   * T5-XL-SSM-NQ: <b>2.3 million</b>
   * T5-large-SSM-NQ: <b>2.3 million tonnes</b>
   * T5-small-SSM-NQ: <b>about 7,000</b>

## Example generation

Q62: <b>If an observer is moving, then the entities he/she is observing will appear to move from his/her perspective. What is an example of this phenomenon?</b>
   * Macaw-11B: <b>a train passing by</b> (credit: 1)
   * Macaw-3B: <b>a bird flying overhead</b>
   * Macaw-large: <b>a hawk flying at night</b>
   * Macaw-answer-11B: <b>a train passing by</b> (credit: 1)
   * GPT3-davinci: <b>The example I gave in class was of a person standing on a train platform watching a train go by. The person on the platform will see the train moving past him/her, but the people on the train will see the platform moving past them.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The Earth is rotating on its axis, and the Sun is rotating around the Earth.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>moving shadow</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the Moon</b>
   * T5-XL-SSM-NQ: <b>unsteady state</b>
   * T5-large-SSM-NQ: <b>Pareidolia</b>
   * T5-small-SSM-NQ: <b>Observation</b>

Q63: <b>If you let go of an object, then gravity pulls it to the ground. What is an example of this phenomenon?</b>
   * Macaw-11B: <b>a free falling leaf</b> (credit: 1)
   * Macaw-3B: <b>a pebble falling</b>
   * Macaw-large: <b>a pull of gravity on a moving object</b>
   * Macaw-answer-11B: <b>a ball dropping</b> (credit: 1)
   * GPT3-davinci: <b>If you drop a ball, it falls to the ground.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>If you let go of an object, then gravity pulls it to the ground.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>apple</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>an apple falling from a tree</b>
   * T5-XL-SSM-NQ: <b>a falling star</b>
   * T5-large-SSM-NQ: <b>Released weight</b>
   * T5-small-SSM-NQ: <b>basins of the Earth</b>

## Explanation

Q64: <b>James went camping in the woods, but forgot to bring a hammer to bang the tent pegs in. Why might a rock be a useful substitute for the hammer?</b>
   * Macaw-11B: <b>it is hard</b> (credit: 1)
   * Macaw-3B: <b>rocks can be used to break down rocks</b>
   * Macaw-large: <b>the rock is smooth so it won't move</b>
   * Macaw-answer-11B: <b>it's hard</b> (credit: 1)
   * GPT3-davinci: <b>James could use the rock to break the tent pegs.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because rocks are hard.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to knock the tent pegs in</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>to break branches</b>
   * T5-XL-SSM-NQ: <b>to provide support</b>
   * T5-large-SSM-NQ: <b>easier to carry</b>
   * T5-small-SSM-NQ: <b>to scare off any predators</b>

Q65: <b>If I went hiking for the day, why is 2 liters of water the right amount to bring with me?</b>
   * Macaw-11B: <b>it's the amount that would keep you hydrated for 8 hours</b> (credit: 1)
   * Macaw-3B: <b>it's enough for a full day</b>
   * Macaw-large: <b>to keep me hydrated</b>
   * Macaw-answer-11B: <b>it's the recommended daily amount</b> (credit: 1)
   * GPT3-davinci: <b>The 2 liter figure is a good rule of thumb for a day hike. If you are going on a longer hike, you should bring more water. If you are going on a shorter hike, you can bring less.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The amount of water you should bring with you depends on the length of your hike, the weather conditions, and your level of fitness.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to avoid dehydration</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>hypovolemia</b>
   * T5-XL-SSM-NQ: <b>sufficing for a hike</b>
   * T5-large-SSM-NQ: <b>for each day's activity</b>
   * T5-small-SSM-NQ: <b>hiking</b>

Q66: <b>My design for a spaceship uses as little fuel as possible. Why is this a good design?</b>
   * Macaw-11B: <b>it saves money</b> (credit: 1)
   * Macaw-3B: <b>less fuel means less pollution</b>
   * Macaw-large: <b>to save the environment</b>
   * Macaw-answer-11B: <b>it saves money</b> (credit: 1)
   * GPT3-davinci: <b>Because it is a good design.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because fuel is heavy.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>minimizes wasted energy</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>minimizes fuel consumption</b>
   * T5-XL-SSM-NQ: <b>economical</b>
   * T5-large-SSM-NQ: <b>low-cost</b>
   * T5-small-SSM-NQ: <b>geothermal heat flux</b>

Q67: <b>Why does sanding remove the shine from polished granite?</b>
   * Macaw-11B: <b>it scratches the surface</b> (credit: 1)
   * Macaw-3B: <b>scratches the surface</b>
   * Macaw-large: <b>scratches</b>
   * Macaw-answer-11B: <b>it removes the top layer of stone</b> (credit: 1)
   * GPT3-davinci: <b>Sanding removes the polish from the surface of the stone. The polish is a very thin layer of wax that is applied to the stone to give it a shine. The sanding process removes this layer of wax.
Sanding is a necessary step in the polishing process. It is the first step in the pol</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Sanding removes the shine from polished granite because the abrasives remove a thin layer of the polished surface.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>surface roughness</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>to remove surface impurities</b>
   * T5-XL-SSM-NQ: <b>dulls the surface</b>
   * T5-large-SSM-NQ: <b>to reveal more depth</b>
   * T5-small-SSM-NQ: <b>polishing</b>

Q68: <b>Why does gravity cause a ball to roll downhill?</b>
   * Macaw-11B: <b>gravity</b> (credit: 0)
   * Macaw-3B: <b>gravity pulls the ball down</b>
   * Macaw-large: <b>gravity is on the ball</b>
   * Macaw-answer-11B: <b>gravity pulls the ball down the hill</b> (credit: 1)
   * GPT3-davinci: <b>Gravity causes the ball to roll downhill because the ball is trying to get to the lowest point.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because the Earth is round.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>gravity</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>because of gravity</b>
   * T5-XL-SSM-NQ: <b>gravity</b>
   * T5-large-SSM-NQ: <b>gravity</b>
   * T5-small-SSM-NQ: <b>due to low ratings</b>

Q69: <b>Why do houses have roofs?</b>
   * Macaw-11B: <b>to keep rain off</b> (credit: 1)
   * Macaw-3B: <b>to protect the occupants from the weather</b>
   * Macaw-large: <b>to protect the inside</b>
   * Macaw-answer-11B: <b>to keep rain and snow out</b> (credit: 1)
   * GPT3-davinci: <b>To keep the house where it is.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>So the rain doesn't fall inside.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to keep out the rain</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>protection from the weather</b>
   * T5-XL-SSM-NQ: <b>to provide shelter from the weather</b>
   * T5-large-SSM-NQ: <b>to prevent flooding</b>
   * T5-small-SSM-NQ: <b>considered lucky</b>

Q70: <b>Why do houses have walls?</b>
   * Macaw-11B: <b>to keep out weather</b> (credit: 1)
   * Macaw-3B: <b>to keep out animals</b>
   * Macaw-large: <b>to keep out animals</b>
   * Macaw-answer-11B: <b>to keep the heat in</b> (credit: 1)
   * GPT3-davinci: <b>To keep the air in.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>So neighbors can't look in.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to provide insulation</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>insulation</b>
   * T5-XL-SSM-NQ: <b>to keep out the pests</b>
   * T5-large-SSM-NQ: <b>to prevent theft</b>
   * T5-small-SSM-NQ: <b>because of a bubble</b>

Q71: <b>Why do houses have windows?</b>
   * Macaw-11B: <b>to let in light and air</b> (credit: 1)
   * Macaw-3B: <b>to let in light</b>
   * Macaw-large: <b>to let in light</b>
   * Macaw-answer-11B: <b>to let in light and air</b> (credit: 1)
   * GPT3-davinci: <b>So you can throw the dog out.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>So we can see the neighbors.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to let in light</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>venting and light</b>
   * T5-XL-SSM-NQ: <b>to allow light in</b>
   * T5-large-SSM-NQ: <b>to view the outside world</b>
   * T5-small-SSM-NQ: <b>to boil or steam rice</b>

Q72: <b>Why do houses have doors?</b>
   * Macaw-11B: <b>to keep out weather</b> (credit: 1)
   * Macaw-3B: <b>to keep out animals</b>
   * Macaw-large: <b>to let in light</b>
   * Macaw-answer-11B: <b>to keep out rain and snow</b> (credit: 1)
   * GPT3-davinci: <b>To keep the house from falling apart.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>So people can't look in.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to provide insulation</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>for security</b>
   * T5-XL-SSM-NQ: <b>to allow light in</b>
   * T5-large-SSM-NQ: <b>venting and light</b>
   * T5-small-SSM-NQ: <b>to their environment</b>

Q73: <b>Why does ice float?</b>
   * Macaw-11B: <b>because of the air trapped in the ice</b> (credit: 0)
   * Macaw-3B: <b>it is heavier than water</b>
   * Macaw-large: <b>less density</b>
   * Macaw-answer-11B: <b>because of its density</b> (credit: 1)
   * GPT3-davinci: <b>Ice floats because it is less dense than water.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because it's lighter than water.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>because of its high density</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>surface tension</b>
   * T5-XL-SSM-NQ: <b>Pressure flow</b>
   * T5-large-SSM-NQ: <b>weightlessness</b>
   * T5-small-SSM-NQ: <b>float through a basket</b>

Q74: <b>Why does ice sink?</b>
   * Macaw-11B: <b>because of the density of the ice</b> (credit: 0)
   * Macaw-3B: <b>it has less surface area than liquid water</b>
   * Macaw-large: <b>it is a liquid</b>
   * Macaw-answer-11B: <b>it's denser than air</b> (credit: 0.5)
   * GPT3-davinci: <b>Ice is less dense than water.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Ice is less dense than water.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>density</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>density</b>
   * T5-XL-SSM-NQ: <b>weight</b>
   * T5-large-SSM-NQ: <b>Convection</b>
   * T5-small-SSM-NQ: <b>the clarity of its water</b>

Q75: <b>Why does it rain a lot in Seattle?</b>
   * Macaw-11B: <b>ocean</b> (credit: 0.5)
   * Macaw-3B: <b>oceans</b>
   * Macaw-large: <b>clouds</b>
   * Macaw-answer-11B: <b>ocean</b> (credit: 0.5)
   * GPT3-davinci: <b>Because if it didn't, it would be called Phoenix.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because Seattle is so close to Canada.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>its proximity to the Pacific Ocean</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the proximity of Puget Sound</b>
   * T5-XL-SSM-NQ: <b>its proximity to the Great Lakes</b>
   * T5-large-SSM-NQ: <b>heavy precipitation</b>
   * T5-small-SSM-NQ: <b>Rain or snow</b>

Q76: <b>Why is Seattle wet?</b>
   * Macaw-11B: <b>ocean</b> (credit: 0.5)
   * Macaw-3B: <b>it is on the edge of a large ocean</b>
   * Macaw-large: <b>evaporation</b>
   * Macaw-answer-11B: <b>it rains a lot</b> (credit: 1)
   * GPT3-davinci: <b>It rains a lot.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because Seattle is on the west coast.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>its proximity to the Pacific Ocean</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the proximity of Puget Sound</b>
   * T5-XL-SSM-NQ: <b>its proximity to the Great Lakes</b>
   * T5-large-SSM-NQ: <b>heavy precipitation</b>
   * T5-small-SSM-NQ: <b>The Seattle Times</b>

Q77: <b>Why is a tally sheet useful to help count things?</b>
   * Macaw-11B: <b>it can be used to check for accuracy</b> (credit: 0.5)
   * Macaw-3B: <b>it is easy to see how many of each item there are</b>
   * Macaw-large: <b>to keep track of change</b>
   * Macaw-answer-11B: <b>it helps you keep track of the totals</b> (credit: 1)
   * GPT3-davinci: <b>A tally sheet is a way to keep track of how many things you have counted.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A tally sheet is a sheet of paper with columns and rows. Each row represents a different item, and each column represents a different characteristic.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>to keep track of items</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>make it easier to count</b>
   * T5-XL-SSM-NQ: <b>to keep track of things</b>
   * T5-large-SSM-NQ: <b>to measure things</b>
   * T5-small-SSM-NQ: <b>In a spreadsheet</b>

## False presupposition

Q78: <b>What year did Tom Hanks land on the moon?</b>
   * Macaw-11B: <b>no year</b> (credit: 1)
   * Macaw-3B: <b>1969</b>
   * Macaw-large: <b>1976</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>Apollo 13, 1995.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>2001. Tom Hanks landed on the moon in Apollo 13.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>20 July 1969</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Apollo 17</b>
   * T5-XL-SSM-NQ: <b>20 July 1969</b>
   * T5-large-SSM-NQ: <b>20 July 1969</b>
   * T5-small-SSM-NQ: <b>1969</b>

Q79: <b>How old was Mark Zuckerberg when he founded Google?</b>
   * Macaw-11B: <b>17</b> (credit: 0)
   * Macaw-3B: <b>16</b>
   * Macaw-large: <b>27</b>
   * Macaw-answer-11B: <b>17</b> (credit: 0)
   * GPT3-davinci: <b>19</b> (credit: 0)
   * Jurassic-1-jumbo: <b>12 years old.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>20</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>19</b>
   * T5-XL-SSM-NQ: <b>18</b>
   * T5-large-SSM-NQ: <b>17</b>
   * T5-small-SSM-NQ: <b>nine</b>

Q80: <b>How old was Mark Zuckerberg when he founded Amazon?</b>
   * Macaw-11B: <b>23</b> (credit: 0)
   * Macaw-3B: <b>18</b>
   * Macaw-large: <b>27</b>
   * Macaw-answer-11B: <b>20</b> (credit: 0)
   * GPT3-davinci: <b>19</b> (credit: 0)
   * Jurassic-1-jumbo: <b>12 years old.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>28</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>17</b>
   * T5-XL-SSM-NQ: <b>18</b>
   * T5-large-SSM-NQ: <b>17</b>
   * T5-small-SSM-NQ: <b>Zuckerberg</b>

Q81: <b>How old was Kermit the Frog when he founded Amazon?</b>
   * Macaw-11B: <b>0</b> (credit: 0)
   * Macaw-3B: <b>10 years old</b>
   * Macaw-large: <b>17</b>
   * Macaw-answer-11B: <b>0</b> (credit: 0)
   * GPT3-davinci: <b>Kermit the Frog was born in 1955, and Amazon was founded in 1994.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>2,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>29</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>54</b>
   * T5-XL-SSM-NQ: <b>36</b>
   * T5-large-SSM-NQ: <b>nine</b>
   * T5-small-SSM-NQ: <b>26</b>

Q82: <b>How old was foo when she founded baz?</b>
   * Macaw-11B: <b>18</b> (credit: 0)
   * Macaw-3B: <b>10 years old</b>
   * Macaw-large: <b>27</b>
   * Macaw-answer-11B: <b>18</b> (credit: 0)
   * GPT3-davinci: <b>foo was born in the year of the cow.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>foo was baz's founder.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>56</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>15</b>
   * T5-XL-SSM-NQ: <b>28</b>
   * T5-large-SSM-NQ: <b>13</b>
   * T5-small-SSM-NQ: <b>6</b>

Q83: <b>How can you sit and stand at the same time?</b>
   * Macaw-11B: <b>use a chair</b> (credit: 0)
   * Macaw-3B: <b>using a chair</b>
   * Macaw-large: <b>stand on a chair</b>
   * Macaw-answer-11B: <b>you can't</b> (credit: 1)
   * GPT3-davinci: <b>It's easy. You just sit down and stand up.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>You do it all the time.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>tripod position</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>A stool</b>
   * T5-XL-SSM-NQ: <b>tripod</b>
   * T5-large-SSM-NQ: <b>computer</b>
   * T5-small-SSM-NQ: <b>Quakers</b>

Q84: <b>How can you walk and run at the same time?</b>
   * Macaw-11B: <b>use different muscles</b> (credit: 0)
   * Macaw-3B: <b>use a treadmill</b>
   * Macaw-large: <b>walk in place of running</b>
   * Macaw-answer-11B: <b>use your arms</b> (credit: 0)
   * GPT3-davinci: <b>It's called a run-walk.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>You walk first, then run.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>locomotion</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>alternating gait</b>
   * T5-XL-SSM-NQ: <b>March</b>
   * T5-large-SSM-NQ: <b>walking and running</b>
   * T5-small-SSM-NQ: <b>walking with the year 20</b>

Q85: <b>Joe is walking. How can Joe now run while still walking?</b>
   * Macaw-11B: <b>he can walk faster</b> (credit: 0)
   * Macaw-3B: <b>he can change direction</b>
   * Macaw-large: <b>push the car</b>
   * Macaw-answer-11B: <b>increase his speed</b> (credit: 0)
   * GPT3-davinci: <b>Joe can run while walking by running while walking.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Joe can run while he is walking.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>simultaneously</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>running</b>
   * T5-XL-SSM-NQ: <b>Joe</b>
   * T5-large-SSM-NQ: <b>Joe can run</b>
   * T5-small-SSM-NQ: <b>about two feet</b>

Q86: <b>Sally's favorite cow died yesterday. When will the cow be alive again?</b>
   * Macaw-11B: <b>in a few days</b> (credit: 0)
   * Macaw-3B: <b>tomorrow</b>
   * Macaw-large: <b>a few days</b>
   * Macaw-answer-11B: <b>in seven years</b> (credit: 0)
   * GPT3-davinci: <b>When Sally's favorite cow is dead.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Sally's favorite cow died yesterday.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>in the spring</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>someday</b>
   * T5-XL-SSM-NQ: <b>tomorrow</b>
   * T5-large-SSM-NQ: <b>Christmas Day</b>
   * T5-small-SSM-NQ: <b>November 25, 2010</b>

## General knowledge

Q87: <b>Susie wants to make an omelette. What ingredients will she need?</b>
   * Macaw-11B: <b>eggs, milk, butter</b> (credit: 1)
   * Macaw-3B: <b>eggs</b>
   * Macaw-large: <b>eggs and cheese</b>
   * Macaw-answer-11B: <b>eggs, milk, butter, salt, pepper</b> (credit: 1)
   * GPT3-davinci: <b>Eggs, butter, milk, cheese, and salt.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>She will need eggs, milk, butter, and flour.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>eggs</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>Eggs</b>
   * T5-XL-SSM-NQ: <b>bacon</b>
   * T5-large-SSM-NQ: <b>some flour</b>
   * T5-small-SSM-NQ: <b>essential oil for food</b>

Q88: <b>Why are eggs needed for an omelette?</b>
   * Macaw-11B: <b>they provide the protein</b> (credit: 1)
   * Macaw-3B: <b>to make the mixture more creamy</b>
   * Macaw-large: <b>to form the omelette</b>
   * Macaw-answer-11B: <b>to add protein</b> (credit: 1)
   * GPT3-davinci: <b>To give it a good consistency.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because without them, it's just an egg.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>to provide protein</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>bind the filling ingredients together</b>
   * T5-XL-SSM-NQ: <b>to provide protein</b>
   * T5-large-SSM-NQ: <b>to prevent overcooking</b>
   * T5-small-SSM-NQ: <b>a jealous female demon</b>

Q89: <b>Why is milk needed for an omelette?</b>
   * Macaw-11B: <b>it helps the eggs cook</b> (credit: 1)
   * Macaw-3B: <b>it adds liquid</b>
   * Macaw-large: <b>to make the egg whites thicker</b>
   * Macaw-answer-11B: <b>it helps the eggs cook</b> (credit: 1)
   * GPT3-davinci: <b>To help you swallow it.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because otherwise, it would be an eggs-plosion.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>to make it fluffy</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>acid</b>
   * T5-XL-SSM-NQ: <b>to thin the egg</b>
   * T5-large-SSM-NQ: <b>to make it easier to swallow</b>
   * T5-small-SSM-NQ: <b>to scare off any predators</b>

Q90: <b>Why is butter needed for an omelette?</b>
   * Macaw-11B: <b>it adds flavor</b> (credit: 1)
   * Macaw-3B: <b>to make the eggs more fluffy</b>
   * Macaw-large: <b>it sets the eggs</b>
   * Macaw-answer-11B: <b>it adds flavor</b> (credit: 1)
   * GPT3-davinci: <b>To make it fluffy.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because otherwise, it would be an omelette.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>to prevent sticking</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>to prevent sticking</b>
   * T5-XL-SSM-NQ: <b>tobind the ingredients</b>
   * T5-large-SSM-NQ: <b>to prevent overcooking</b>
   * T5-small-SSM-NQ: <b>a pulse containing ice</b>

Q91: <b>Which kind of grass is best to grow in shady areas?</b>
   * Macaw-11B: <b>fescue</b> (credit: 1)
   * Macaw-3B: <b>blue grass</b>
   * Macaw-large: <b>dark green</b>
   * Macaw-answer-11B: <b>fescue</b> (credit: 1)
   * GPT3-davinci: <b>Tall fescue is a good choice for shady areas. It is a cool season grass that is very shade tolerant. It is also very drought tolerant. It is a deep rooted grass that will tolerate dry conditions. It is also a good choice for areas that are prone to erosion.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The best grass for shady areas is tall fescue. It grows well in shade, is drought tolerant, and is disease resistant.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Fescue</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>fescue</b>
   * T5-XL-SSM-NQ: <b>rough sedges</b>
   * T5-large-SSM-NQ: <b>Seashore Paspalum, Platinum TE</b>
   * T5-small-SSM-NQ: <b>Dendrochronolis</b>

Q92: <b>What is shiplap?</b>
   * Macaw-11B: <b>a kind of wood paneling</b> (credit: 1)
   * Macaw-3B: <b>a kind of construction material</b>
   * Macaw-large: <b>a covering around the edges of a book</b>
   * Macaw-answer-11B: <b>a type of cladding made of thin wood planks</b> (credit: 1)
   * GPT3-davinci: <b>Shiplap is a type of wood siding that is used on the exterior of houses. It is a very popular look in the South.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Shiplap is a type of wooden board that overlaps each other.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>horizontal boards</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>boards laid horizontally</b>
   * T5-XL-SSM-NQ: <b>paneling</b>
   * T5-large-SSM-NQ: <b>a type of canvas</b>
   * T5-small-SSM-NQ: <b>a langoustine</b>

Q93: <b>What does the idiom "kick the tires" mean?</b>
   * Macaw-11B: <b>test drive a car</b> (credit: 1)
   * Macaw-3B: <b>to make sure the tires are in good shape</b>
   * Macaw-large: <b>to change tires</b>
   * Macaw-answer-11B: <b>test the vehicle</b> (credit: 1)
   * GPT3-davinci: <b>To kick the tires means to check out something before you buy it.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>To "kick the tires" means to examine something closely, especially a car.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>test-drive a car</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>test the waters</b>
   * T5-XL-SSM-NQ: <b>a car is tested</b>
   * T5-large-SSM-NQ: <b>'to start the engine'</b>
   * T5-small-SSM-NQ: <b>"Kiss You Back"</b>

Q94: <b>What is the role of the spark plug in a combustion engine?</b>
   * Macaw-11B: <b>it causes the engine to start</b> (credit: 1)
   * Macaw-3B: <b>it ignites the fuel</b>
   * Macaw-large: <b>to provide a pathway for gas to enter the combustion chamber</b>
   * Macaw-answer-11B: <b>ignite the fuel</b> (credit: 1)
   * GPT3-davinci: <b>The spark plug is the device that ignites the fuel-air mixture in the cylinder.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The spark plug ignites the fuel-air mixture in the combustion chamber.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>ignite the fuel</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>start the engine</b>
   * T5-XL-SSM-NQ: <b>the initial spark</b>
   * T5-large-SSM-NQ: <b>start the engine</b>
   * T5-small-SSM-NQ: <b>the speed of the reaction</b>

Q95: <b>What are the parts in a car engine?</b>
   * Macaw-11B: <b>pistons, valves, and crankshaft</b> (credit: 1)
   * Macaw-3B: <b>pistons, valves, and crankshaft</b>
   * Macaw-large: <b>gas, oil, and cylinders</b>
   * Macaw-answer-11B: <b>piston, crankshaft, valves, intake and exhaust systems</b> (credit: 1)
   * GPT3-davinci: <b>The parts in a car engine are the engine block, the cylinder head, the cylinder block, the crankshaft, the connecting rod, the piston, the spark plug, the camshaft, the timing belt, the timing chain, the timing gears, the timing chain cover, the timing chain tensioner,</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The parts of a car engine are: cylinder block, cylinder head, crankshaft, connecting rods, pistons, camshaft, valves, timing gears, timing chain, oil pump, oil pan, intake manifold, exhaust manifold, and rocker arms.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>cylinder head(s)</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>cylinder head(s)</b>
   * T5-XL-SSM-NQ: <b>cylinder head(s)</b>
   * T5-large-SSM-NQ: <b>intake and exhaust passages</b>
   * T5-small-SSM-NQ: <b>to power engines</b>

Q96: <b>What is the role of the piston in a car engine?</b>
   * Macaw-11B: <b>it moves the connecting rod</b> (credit: 1)
   * Macaw-3B: <b>it moves the valves</b>
   * Macaw-large: <b>it is the vehicle that converts fuel into kinetic energy and heat energy</b>
   * Macaw-answer-11B: <b>to compress air in the cylinder</b> (credit: 1)
   * GPT3-davinci: <b>The piston is a cylindrical component that is used to convert the reciprocating motion of the engine's crankshaft into a rotary motion that drives the car's wheels.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The piston is the engine's "heart". It moves up and down in the cylinder, creating the power that propels the car.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>move the crank</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the power source</b>
   * T5-XL-SSM-NQ: <b>fire</b>
   * T5-large-SSM-NQ: <b>internal combustion</b>
   * T5-small-SSM-NQ: <b>to measure engine dynamic changes</b>

Q97: <b>What is the role of a carburetor in a car engine?</b>
   * Macaw-11B: <b>it converts fuel into fuel and air mixtures</b> (credit: 1)
   * Macaw-3B: <b>it provides fuel for the combustion chambers</b>
   * Macaw-large: <b>to remove excess fuel from the engine</b>
   * Macaw-answer-11B: <b>to mix air and fuel</b> (credit: 1)
   * GPT3-davinci: <b>It's a device that converts water into gasoline.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A carburetor is a device that mixes air and fuel together. The carburetor mixes the fuel and air together, and this mixture is then sent to the engine.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>atomizes fuel</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>fuel injection</b>
   * T5-XL-SSM-NQ: <b>to supply fuel</b>
   * T5-large-SSM-NQ: <b>a type of cylinder head</b>
   * T5-small-SSM-NQ: <b>head-level</b>

Q98: <b>What is the role of the valves in a car engine?</b>
   * Macaw-11B: <b>control the flow of gas</b> (credit: 1)
   * Macaw-3B: <b>to regulate the flow of air and fuel</b>
   * Macaw-large: <b>to adjust the pressure of the air</b>
   * Macaw-answer-11B: <b>to control the flow of air and fuel</b> (credit: 1)
   * GPT3-davinci: <b>Valves are used to control the flow of gases and fluids in and out of the engine.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The valves in your car engine open and close to allow air and fuel into the combustion chamber. The valves also control the flow of exhaust gases out of the combustion chamber.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to open and close</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>to regulate the flow of air</b>
   * T5-XL-SSM-NQ: <b>to charge the engine</b>
   * T5-large-SSM-NQ: <b>measure and regulate the speed</b>
   * T5-small-SSM-NQ: <b>to prevent engine knocking</b>

Q99: <b>What is the path of the gas through a car engine as it operates?</b>
   * Macaw-11B: <b>in, out, in, out</b> (credit: 0)
   * Macaw-3B: <b>in a straight line</b>
   * Macaw-large: <b>gas flows from the engine to the exhaust</b>
   * Macaw-answer-11B: <b>intake, compression, exhaust</b> (credit: 1)
   * GPT3-davinci: <b>The path of the gas through a car engine as it operates is as follows:
1. The gas enters the engine through the air filter.
2. The gas passes through the carburetor.
3. The gas passes through the intake manifold.
4. The gas passes through the cylinder head.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The gas enters the engine through the carburetor, where it is mixed with air. The mixture is then ignited by a spark from the spark plug. The burning mixture forces the pistons down, which turns the crankshaft. The crankshaft turns the camshaft, which turns the intake and exhaust valves. The valves open and close to let in air and fuel, and let out exhaust.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>in an endless loop</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>intake manifold</b>
   * T5-XL-SSM-NQ: <b>internal combustion</b>
   * T5-large-SSM-NQ: <b>intake and exhaust passages</b>
   * T5-small-SSM-NQ: <b>to operate power</b>

Q100: <b>Is it dangerous to inhale smoke from wildfires?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>Yes. Smoke from wildfires contains a complex mixture of gases and fine particles. The fine particles are so small that they can get deep into your lungs and even into your bloodstream. The smoke can irritate your eyes, nose, throat, and lungs. It can also worsen chronic heart and lung diseases.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Wildfire smoke contains fine particles and gases that can irritate your eyes, nose, throat and lungs.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>wildfire smoke is an irritant</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>can cause respiratory illness</b>
   * T5-XL-SSM-NQ: <b>is it safe to breathe?</b>
   * T5-large-SSM-NQ: <b>It is not recommended</b>
   * T5-small-SSM-NQ: <b>isopropyl group</b>

Q101: <b>Why are toxic gases bad for you?</b>
   * Macaw-11B: <b>they can cause cancer</b> (credit: 1)
   * Macaw-3B: <b>they cause damage to the lungs</b>
   * Macaw-large: <b>they pollute the air</b>
   * Macaw-answer-11B: <b>they are poisonous</b> (credit: 1)
   * GPT3-davinci: <b>Because they are toxic.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Toxic gases are dangerous because they displace oxygen.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>death</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>can cause death by asphyxiation</b>
   * T5-XL-SSM-NQ: <b>an environmental health risk</b>
   * T5-large-SSM-NQ: <b>overuse of chemicals</b>
   * T5-small-SSM-NQ: <b>to reduce theft</b>

Q102: <b>What is a tally sheet useful for?</b>
   * Macaw-11B: <b>keeping track of things</b> (credit: 1)
   * Macaw-3B: <b>keeping track of money</b>
   * Macaw-large: <b>keeping track of things</b>
   * Macaw-answer-11B: <b>keeping track of things</b> (credit: 1)
   * GPT3-davinci: <b>Tally sheets are used to keep track of the number of times a certain behavior occurs.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Tally sheets are very useful when counting inventory, counting votes, or counting anything.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>for keeping track of items</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>tabulating results of an experiment</b>
   * T5-XL-SSM-NQ: <b>recording financial transactions</b>
   * T5-large-SSM-NQ: <b>to track progress</b>
   * T5-small-SSM-NQ: <b>good news for the farmers</b>

Q103: <b>In what situation might a person have broken their arm?</b>
   * Macaw-11B: <b>a fall</b> (credit: 1)
   * Macaw-3B: <b>a car accident</b>
   * Macaw-large: <b>a car accident</b>
   * Macaw-answer-11B: <b>falling down stairs</b> (credit: 1)
   * GPT3-davinci: <b>A person might have broken their arm if they fell off a ladder.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A broken arm is an injury that occurs when a bone in the arm breaks.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>while playing rugby</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>A fall</b>
   * T5-XL-SSM-NQ: <b>in a car accident</b>
   * T5-large-SSM-NQ: <b>In a car accident</b>
   * T5-small-SSM-NQ: <b>undisclosed illness</b>

Q104: <b>What objects might be involved in a car crash?</b>
   * Macaw-11B: <b>other cars, trees, telephone poles</b> (credit: 1)
   * Macaw-3B: <b>rocks</b>
   * Macaw-large: <b>sand</b>
   * Macaw-answer-11B: <b>trees, telephone poles, telephones, power lines, buildings, etc.</b> (credit: 1)
   * GPT3-davinci: <b>The most common objects involved in car crashes are other cars, trees, and utility poles.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The objects involved in a car accident can include cars, trucks, motorcycles, bicycles, pedestrians, and stationary objects.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>other vehicles</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>pedestrians</b>
   * T5-XL-SSM-NQ: <b>a vehicle</b>
   * T5-large-SSM-NQ: <b>other vehicle</b>
   * T5-small-SSM-NQ: <b>frames a wheel well</b>

Q105: <b>How would a tree be involved in a car crash?</b>
   * Macaw-11B: <b>it could fall on a car</b> (credit: 1)
   * Macaw-3B: <b>it would break</b>
   * Macaw-large: <b>it would be crushed</b>
   * Macaw-answer-11B: <b>it could fall on the car</b> (credit: 1)
   * GPT3-davinci: <b>The tree was hit by a car.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A tree can be involved in a crash when a driver loses control of the vehicle and crashes into a tree.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a barrier</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>struck by a vehicle</b>
   * T5-XL-SSM-NQ: <b>fallen branch</b>
   * T5-large-SSM-NQ: <b>could be damaged</b>
   * T5-small-SSM-NQ: <b>Any abnormal electric current</b>

Q106: <b>How might a telephone pole be involved in a car crash?</b>
   * Macaw-11B: <b>it could be hit by a car</b> (credit: 1)
   * Macaw-3B: <b>it might break</b>
   * Macaw-large: <b>a person on a cell phone calls the police for help and they arrive at the scene of the crash</b>
   * Macaw-answer-11B: <b>it could be pushed over</b> (credit: 1)
   * GPT3-davinci: <b>A telephone pole is involved in a car crash when a driver runs into it.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A telephone pole might be involved in a car crash if a driver swerves to avoid hitting it and ends up crashing into another vehicle.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>support a vehicle</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>struck by a vehicle</b>
   * T5-XL-SSM-NQ: <b>Impaired driving</b>
   * T5-large-SSM-NQ: <b>poles</b>
   * T5-small-SSM-NQ: <b>passing a telephone pole</b>

Q107: <b>Why might a car hit a telephone pole?</b>
   * Macaw-11B: <b>it was in the way</b> (credit: 1)
   * Macaw-3B: <b>the pole is made of a hard material</b>
   * Macaw-large: <b>the wire is closer to the car</b>
   * Macaw-answer-11B: <b>driver lost control</b> (credit: 1)
   * GPT3-davinci: <b>Because it was parked too close to it.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because the driver was distracted by his cellphone.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to prevent collisions</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>striking a utility pole</b>
   * T5-XL-SSM-NQ: <b>to reduce friction</b>
   * T5-large-SSM-NQ: <b>causing a collision</b>
   * T5-small-SSM-NQ: <b>to traffic with cars</b>

Q108: <b>What might cause a car to hit a telephone pole?</b>
   * Macaw-11B: <b>a drunk driver</b> (credit: 1)
   * Macaw-3B: <b>a deer running in the road</b>
   * Macaw-large: <b>a car braking suddenly</b>
   * Macaw-answer-11B: <b>swerving</b> (credit: 1)
   * GPT3-davinci: <b>A telephone pole might cause a car to hit a telephone pole.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>A car hitting a telephone pole is a common occurrence. The pole is usually hit when the driver is distracted, speeding, or intoxicated.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a sudden stop</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>road debris</b>
   * T5-XL-SSM-NQ: <b>a missed brake</b>
   * T5-large-SSM-NQ: <b>a vehicle moving forward</b>
   * T5-small-SSM-NQ: <b>the phone hacking problem</b>

Q109: <b>Why might a car driver be drunk?</b>
   * Macaw-11B: <b>to escape from a bad situation</b> (credit: 1)
   * Macaw-3B: <b>intoxicated</b>
   * Macaw-large: <b>if they drink too much, they will get behind the wheel faster</b>
   * Macaw-answer-11B: <b>to get high</b> (credit: 1)
   * GPT3-davinci: <b>Because he's driving a drunk.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because he drank too much.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to reduce cognitive errors</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>to avoid or mitigate the effects of alcohol</b>
   * T5-XL-SSM-NQ: <b>drunk driving</b>
   * T5-large-SSM-NQ: <b>unresponsive driving</b>
   * T5-small-SSM-NQ: <b>to avoid drunk driving fatalities</b>

Q110: <b>How might making poor decisions result in a car crash?</b>
   * Macaw-11B: <b>speeding</b> (credit: 1)
   * Macaw-3B: <b>a driver might not see an object in time to avoid it</b>
   * Macaw-large: <b>you could end up in a coma</b>
   * Macaw-answer-11B: <b>speeding</b> (credit: 1)
   * GPT3-davinci: <b>If you are driving while intoxicated, you are more likely to make poor decisions that could result in a car crash.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Making poor decisions while driving can result in a car crash.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>inattention</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>speeding</b>
   * T5-XL-SSM-NQ: <b>negligent driving</b>
   * T5-large-SSM-NQ: <b>leading to a car crash</b>
   * T5-small-SSM-NQ: <b>A simple explanation of driving behaviour</b>

Q111: <b>Why does speeding cause car accidents?</b>
   * Macaw-11B: <b>it causes the car to swerve</b> (credit: 1)
   * Macaw-3B: <b>the force of the impact can cause the car to swerve</b>
   * Macaw-large: <b>you are not paying attention to the road</b>
   * Macaw-answer-11B: <b>it reduces reaction time</b> (credit: 1)
   * GPT3-davinci: <b>Because you can't turn time into space.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Speeding is a factor in many car accidents. Speeding reduces a driver's reaction time, increases the distance required to stop a vehicle, and makes it more difficult for a driver to regain control of a vehicle.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>increased chance of injury</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>increased reaction time</b>
   * T5-XL-SSM-NQ: <b>The speeding problem</b>
   * T5-large-SSM-NQ: <b>increased speed</b>
   * T5-small-SSM-NQ: <b>to prevent intraoperative corneal injuries</b>

Q112: <b>How might speeding cause a car accident?</b>
   * Macaw-11B: <b>lose control of the car</b> (credit: 1)
   * Macaw-3B: <b>causing the car to lose control</b>
   * Macaw-large: <b>you could be seriously injured</b>
   * Macaw-answer-11B: <b>driver loses control of vehicle</b> (credit: 1)
   * GPT3-davinci: <b>Speeding is a factor in many car accidents. Speeding increases the likelihood of a car accident because it increases the force of impact. The faster a car is going, the more damage it will do to another car or object when it collides with it.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Speeding is a factor in many car accidents. Speeding reduces a driver's reaction time, increases the distance required to stop a vehicle, and makes it more difficult for a driver to swerve out of the way of danger.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>causes increased vulnerability to road conditions</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>increased risk of collision</b>
   * T5-XL-SSM-NQ: <b>in a low-speed car</b>
   * T5-large-SSM-NQ: <b>can lead to an accident</b>
   * T5-small-SSM-NQ: <b>They are not alone</b>

Q113: <b>What is involved in driving?</b>
   * Macaw-11B: <b>concentration, observation, control</b> (credit: 1)
   * Macaw-3B: <b>the brain</b>
   * Macaw-large: <b>risk</b>
   * Macaw-answer-11B: <b>concentration, observation, and control</b> (credit: 1)
   * GPT3-davinci: <b>Driving is a very simple process. You just need to be able to see and hear. You need to be able to see the road and the other cars around you. You need to be able to hear the sounds of the car and the sounds of the road. You need to be able to see the signs and the</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Driving is the act of controlling a vehicle.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>applying the brakes</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>driving</b>
   * T5-XL-SSM-NQ: <b>operating a vehicle</b>
   * T5-large-SSM-NQ: <b>a vehicle</b>
   * T5-small-SSM-NQ: <b>traffic calming</b>

Q114: <b>What does driving a car involve?</b>
   * Macaw-11B: <b>steering</b> (credit: 0.5)
   * Macaw-3B: <b>controlling the vehicle</b>
   * Macaw-large: <b>kinetic energy</b>
   * Macaw-answer-11B: <b>steering, braking, shifting gears, accelerating, navigating</b> (credit: 1)
   * GPT3-davinci: <b>Driving a car involves the use of a steering wheel, accelerator, and brake pedal.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Driving a car involves controlling a vehicle, usually with four wheels, powered by an engine, and able to carry a small number of people.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>applying the brakes</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>the operation of a motor vehicle</b>
   * T5-XL-SSM-NQ: <b>many factors</b>
   * T5-large-SSM-NQ: <b>motor vehicle</b>
   * T5-small-SSM-NQ: <b>for the maintenance of public vehicles</b>

Q115: <b>What is the purpose of driving a car?</b>
   * Macaw-11B: <b>transport people</b> (credit: 1)
   * Macaw-3B: <b>to move</b>
   * Macaw-large: <b>transport people</b>
   * Macaw-answer-11B: <b>to get from point A to point B</b> (credit: 1)
   * GPT3-davinci: <b>To get from one place to another.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>To transport people or goods from one place to another.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>transportation</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>transportation</b>
   * T5-XL-SSM-NQ: <b>to carry people</b>
   * T5-large-SSM-NQ: <b>transport</b>
   * T5-small-SSM-NQ: <b>to maintain muscle control</b>

Q116: <b>How many years will it take to build truly intelligent machines?</b>
   * Macaw-11B: <b>hundreds of years</b> (credit: 1)
   * Macaw-3B: <b>100 years</b>
   * Macaw-large: <b>1 billion years</b>
   * Macaw-answer-11B: <b>decades</b> (credit: 1)
   * GPT3-davinci: <b>I don't know. I don't think anyone knows.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>50 years.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>probably not in our lifetime</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>decades</b>
   * T5-XL-SSM-NQ: <b>decades</b>
   * T5-large-SSM-NQ: <b>2050</b>
   * T5-small-SSM-NQ: <b>five</b>

Q117: <b>Why will it take hundreds of years to build truly intelligent machines?</b>
   * Macaw-11B: <b>the brain is very complex</b> (credit: 1)
   * Macaw-3B: <b>the technology is still being developed</b>
   * Macaw-large: <b>they require so much technology</b>
   * Macaw-answer-11B: <b>they are not yet capable of learning</b> (credit: 0.5)
   * GPT3-davinci: <b>Because we don't know how to build them.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because intelligence is the most complex thing in the universe.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>the Three Laws of AI</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>complexity</b>
   * T5-XL-SSM-NQ: <b>The hard problem with AI</b>
   * T5-large-SSM-NQ: <b>This is why artificial intelligence is so complex</b>
   * T5-small-SSM-NQ: <b>one to three</b>

Q118: <b>Why are truly intelligent machines very complex?</b>
   * Macaw-11B: <b>they have to be</b> (credit: 0)
   * Macaw-3B: <b>to make the most of the available resources</b>
   * Macaw-large: <b>they are made of parts that are connected</b>
   * Macaw-answer-11B: <b>they need to be able to learn</b> (credit: 1)
   * GPT3-davinci: <b>Because they have to be.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because they have so many moving parts.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>many cognitive abilities</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the nature of the problem</b>
   * T5-XL-SSM-NQ: <b>because of their inherent complexity</b>
   * T5-large-SSM-NQ: <b>the foundations of AI</b>
   * T5-small-SSM-NQ: <b>about a brain</b>

Q119: <b>John is counting sheep. What equipment might be useful for John?</b>
   * Macaw-11B: <b>a telescope</b> (credit: 0)
   * Macaw-3B: <b>a tape measure</b>
   * Macaw-large: <b>a hand lens</b>
   * Macaw-answer-11B: <b>a calculator</b> (credit: 1)
   * GPT3-davinci: <b>John might want to use a sheep counter.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A sheep counter.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a digital counter</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>a digital counting machine</b>
   * T5-XL-SSM-NQ: <b>a counter</b>
   * T5-large-SSM-NQ: <b>a GPS tracker</b>
   * T5-small-SSM-NQ: <b>a GPS tracker</b>

Q120: <b>What would be a good design for a spaceship?</b>
   * Macaw-11B: <b>one that could travel fast and be easily repaired</b> (credit: 1)
   * Macaw-3B: <b>a sphere</b>
   * Macaw-large: <b>a star similar to our Sun</b>
   * Macaw-answer-11B: <b>a ship that can move on its own</b> (credit: 0.5)
   * GPT3-davinci: <b>A good design for a spaceship would be a spaceship that can travel to other planets.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A spaceship should be designed so that its occupants can breathe.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a planetary probe</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Orion</b>
   * T5-XL-SSM-NQ: <b>a simple spaceship</b>
   * T5-large-SSM-NQ: <b>high-tech propulsion</b>
   * T5-small-SSM-NQ: <b>to evangelize the Rubinoos</b>

Q121: <b>How do you remove the shine from polished granite?</b>
   * Macaw-11B: <b>sand it</b> (credit: 1)
   * Macaw-3B: <b>sand it</b>
   * Macaw-large: <b>use a soft cloth</b>
   * Macaw-answer-11B: <b>sandpaper</b> (credit: 1)
   * GPT3-davinci: <b>Polished granite is a very hard surface and is very difficult to scratch. However, if you do scratch it, you can remove the shine by using a pumice stone.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The shine on polished granite is from polishing. To remove the shine, you need to polish the granite again.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>dulling paste</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>sandblasting</b>
   * T5-XL-SSM-NQ: <b>dulling</b>
   * T5-large-SSM-NQ: <b>a wax or clay base</b>
   * T5-small-SSM-NQ: <b>si tacuisses, philosophus mansisses</b>

Q122: <b>How does an internal combustion engine work?</b>
   * Macaw-11B: <b>it converts fuel into kinetic energy and heat</b> (credit: 1)
   * Macaw-3B: <b>it burns fuel</b>
   * Macaw-large: <b>it converts fuel into kinetic energy and heat energy</b>
   * Macaw-answer-11B: <b>it converts chemical energy into mechanical energy</b> (credit: 1)
   * GPT3-davinci: <b>It's a very complicated process, but basically you take a bunch of gasoline, put it in a cylinder, and light it on fire.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>An internal combustion engine is a heat engine that burns fuel to create heat, which expands and moves a piston. The piston is connected to a crankshaft, which turns a flywheel, which turns a transmission, which turns the wheels.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>heat energy</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>burns fossil fuels</b>
   * T5-XL-SSM-NQ: <b>ignitron</b>
   * T5-large-SSM-NQ: <b>fires up</b>
   * T5-small-SSM-NQ: <b>work in the interior</b>

Q123: <b>How does an internal combustion engine convert fuel into kinetic energy and heat and cooled exhaust gas?</b>
   * Macaw-11B: <b>by combusting</b> (credit: 1)
   * Macaw-3B: <b>combustion</b>
   * Macaw-large: <b>combustion</b>
   * Macaw-answer-11B: <b>chemical energy</b> (credit: 0)
   * GPT3-davinci: <b>The internal combustion engine is a heat engine that uses the heat of a combustion reaction to drive a piston. The heat of the combustion reaction is used to heat the air in the cylinder, which expands and pushes the piston. The piston is connected to a crankshaft, which converts the linear motion of the piston into</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The fuel is mixed with air in the combustion chamber. The mixture is ignited by a spark. The combustion of the fuel-air mixture releases energy in the form of heat. The hot gases expand and force the piston down. The piston is connected to the crankshaft, which converts the linear motion of the piston into rotary motion. The rotary motion is transferred to the wheels of the vehicle. The hot gases are cooled in the exhaust system</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>The internal combustion engine</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>combustion</b>
   * T5-XL-SSM-NQ: <b>heat</b>
   * T5-large-SSM-NQ: <b>combustion</b>
   * T5-small-SSM-NQ: <b>indirectly using a liquid gas supply</b>

Q124: <b>What are the parts of an internal combustion engine?</b>
   * Macaw-11B: <b>piston, cylinder, valves, and head</b> (credit: 1)
   * Macaw-3B: <b>pistons, valves, exhaust manifold, exhaust manifold, intake manifold, exhaust manifold, intake manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, intake manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust manifold, exhaust man</b>
   * Macaw-large: <b>gas, oil, and filter</b>
   * Macaw-answer-11B: <b>piston, cylinder, valves, and crankshaft</b> (credit: 1)
   * GPT3-davinci: <b>The parts of an internal combustion engine are the cylinder, piston, connecting rod, crankshaft, flywheel, camshaft, valves, spark plugs, and carburetor.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The parts of an internal combustion engine are: cylinder block, cylinder head, crankshaft, connecting rod, piston, piston rings, camshaft, valves, pushrods, rocker arms, timing chain, timing gears, timing chain cover, oil pump, oil pan, oil pump pickup, oil pump drive, oil pump cover, oil pan gasket,</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>cylinders</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>piston</b>
   * T5-XL-SSM-NQ: <b>crankcase</b>
   * T5-large-SSM-NQ: <b>Fuel</b>
   * T5-small-SSM-NQ: <b>Internal combustion</b>

Q125: <b>What is the purpose of the piston in an internal combustion engine?</b>
   * Macaw-11B: <b>to compress fuel and air in the cylinder</b> (credit: 1)
   * Macaw-3B: <b>to move the crankshaft</b>
   * Macaw-large: <b>to move the engine forward</b>
   * Macaw-answer-11B: <b>to compress air and fuel</b> (credit: 1)
   * GPT3-davinci: <b>The piston is the part of the engine that moves up and down. It is connected to the crankshaft, which is the part of the engine that turns. The piston is what makes the engine move.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The piston is the heart of the engine. It converts the explosive force of the ignited fuel-air mixture in the cylinder into mechanical energy.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to seal the engine's cylinders</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>actuate the reciprocating piston</b>
   * T5-XL-SSM-NQ: <b>to deliver energy</b>
   * T5-large-SSM-NQ: <b>to operate the engine</b>
   * T5-small-SSM-NQ: <b>origins are unknown</b>

Q126: <b>What is the purpose of the cylinder in an internal combustion engine?</b>
   * Macaw-11B: <b>to compress fuel and air</b> (credit: 1)
   * Macaw-3B: <b>to burn fuel</b>
   * Macaw-large: <b>to provide a means of increasing the efficiency of the engine</b>
   * Macaw-answer-11B: <b>to contain the burning mixture</b> (credit: 1)
   * GPT3-davinci: <b>The cylinder is the part of the engine that contains the combustion process.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The cylinder is the part of the engine where the combustion of fuel takes place.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to contain the combustion</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the combustion process</b>
   * T5-XL-SSM-NQ: <b>fire</b>
   * T5-large-SSM-NQ: <b>to operate the engine</b>
   * T5-small-SSM-NQ: <b>to measure visual acuity</b>

Q127: <b>What is the purpose of the valves in an internal combustion engine?</b>
   * Macaw-11B: <b>to control the flow of gas</b> (credit: 1)
   * Macaw-3B: <b>to regulate the flow of air and fuel</b>
   * Macaw-large: <b>to adjust the air pressure</b>
   * Macaw-answer-11B: <b>to control the flow of air and fuel</b> (credit: 1)
   * GPT3-davinci: <b>The valves are used to control the flow of air and fuel into the engine.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The valves in an internal combustion engine control the flow of air into and out of the combustion chamber.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to prevent engine knocking</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>to admit air</b>
   * T5-XL-SSM-NQ: <b>to supply air</b>
   * T5-large-SSM-NQ: <b>measure and regulate the speed</b>
   * T5-small-SSM-NQ: <b>to detect motion and orientation</b>

Q128: <b>What is the purpose of the head in an internal combustion engine?</b>
   * Macaw-11B: <b>to control the flow of gas</b> (credit: 1)
   * Macaw-3B: <b>to direct the flow of air and fuel to the rest of the engine</b>
   * Macaw-large: <b>to control the engine</b>
   * Macaw-answer-11B: <b>to cool the cylinders</b> (credit: 1)
   * GPT3-davinci: <b>To get rid of the exhaust.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The head is bolted to the block and contains the valves, spark plugs, and combustion chambers.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to provide a smooth running surface</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the cylinder head(s)</b>
   * T5-XL-SSM-NQ: <b>to conduct heat</b>
   * T5-large-SSM-NQ: <b>measure and regulate the speed</b>
   * T5-small-SSM-NQ: <b>regulates speed</b>

Q129: <b>What is the piston in an internal combustion engine?</b>
   * Macaw-11B: <b>a part of an internal combustion engine that moves up and down to compress air</b> (credit: 1)
   * Macaw-3B: <b>a part of the engine that moves the valves</b>
   * Macaw-large: <b>the largest part of the engine is usually the largest part of the engine, usually the block</b>
   * Macaw-answer-11B: <b>the moving part of an internal combustion engine</b> (credit: 1)
   * GPT3-davinci: <b>The piston is a cylindrical component that is used to convert the linear motion of the piston rod into a rotating motion.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The piston is a cylindrical component that slides up and down in the cylinder.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>part of the cylinder head</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the moving part of an engine</b>
   * T5-XL-SSM-NQ: <b>cylinder head</b>
   * T5-large-SSM-NQ: <b>cylinder head</b>
   * T5-small-SSM-NQ: <b>The cylinder head(s)</b>

Q130: <b>What is the cylinder in an internal combustion engine?</b>
   * Macaw-11B: <b>the part of an engine that contains the pistons</b> (credit: 1)
   * Macaw-3B: <b>a container for fuel</b>
   * Macaw-large: <b>the smallest cylinder that can be found in an automobile engine</b>
   * Macaw-answer-11B: <b>the space where the gas is compressed</b> (credit: 1)
   * GPT3-davinci: <b>The cylinder is the part of the engine that contains the combustion chamber.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The cylinder is the space in the cylinder block where the pistons move up and down.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>the power unit</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the basic unit of combustion</b>
   * T5-XL-SSM-NQ: <b>cylinder head</b>
   * T5-large-SSM-NQ: <b>intake and exhaust passages</b>
   * T5-small-SSM-NQ: <b>cylinder head(s)</b>

Q131: <b>What is the valve in an internal combustion engine?</b>
   * Macaw-11B: <b>a part of an internal combustion engine that opens and closes to regulate the flow of gas</b> (credit: 1)
   * Macaw-3B: <b>a part of the engine that controls the flow of gas</b>
   * Macaw-large: <b>the safety valve</b>
   * Macaw-answer-11B: <b>opening and closing mechanism</b> (credit: 1)
   * GPT3-davinci: <b>The valve is a device that controls the flow of gases and liquids into and out of the engine.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The valve in an internal combustion engine is a device which controls the flow of air or fuel into the engine.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>intake and exhaust</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>valve springs</b>
   * T5-XL-SSM-NQ: <b>valve train</b>
   * T5-large-SSM-NQ: <b>intake and exhaust valves</b>
   * T5-small-SSM-NQ: <b>the mouthpiece</b>

Q132: <b>What is the head in an internal combustion engine?</b>
   * Macaw-11B: <b>the top part of an internal combustion engine that contains the valves</b> (credit: 1)
   * Macaw-3B: <b>the cylinder head</b>
   * Macaw-large: <b>the cylinder</b>
   * Macaw-answer-11B: <b>the upper part of the engine that contains the cylinders and valves</b> (credit: 1)
   * GPT3-davinci: <b>The head is the part of the engine that contains the valves.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The head is the top part of the engine.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>the cylinder head(s)</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the cylinder head(s)</b>
   * T5-XL-SSM-NQ: <b>thecylinder head</b>
   * T5-large-SSM-NQ: <b>the engine's head</b>
   * T5-small-SSM-NQ: <b>The husk</b>

Q133: <b>In an internal combustion engine, what does the piston do?</b>
   * Macaw-11B: <b>it pushes the fuel into the cylinders</b> (credit: 1)
   * Macaw-3B: <b>moves the valves</b>
   * Macaw-large: <b>moves the needle</b>
   * Macaw-answer-11B: <b>pushes the other parts of the engine</b> (credit: 1)
   * GPT3-davinci: <b>The piston moves up and down in the cylinder.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>It moves up and down.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>pushes against the cylinder wall</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>pushes the charge into the cylinder</b>
   * T5-XL-SSM-NQ: <b>fire</b>
   * T5-large-SSM-NQ: <b>heat the engine</b>
   * T5-small-SSM-NQ: <b>to measure visual acuity</b>

Q134: <b>What does the piston do in an internal combustion engine?</b>
   * Macaw-11B: <b>it pushes the fuel/air mixture down the cylinder</b> (credit: 1)
   * Macaw-3B: <b>moves the valves</b>
   * Macaw-large: <b>moves the engine</b>
   * Macaw-answer-11B: <b>pushes the other parts of the engine</b> (credit: 1)
   * GPT3-davinci: <b>The piston is a cylindrical metal rod that moves up and down inside the cylinder. It is connected to the crankshaft by a connecting rod. The piston is the part of the engine that does the actual work of converting the energy in the fuel into mechanical energy.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The piston is the part that moves up and down in the cylinder.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>pushes against the cylinder wall</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>actuates the reciprocating piston</b>
   * T5-XL-SSM-NQ: <b>deliver energy</b>
   * T5-large-SSM-NQ: <b>heat the engine</b>
   * T5-small-SSM-NQ: <b>to measure visual acuity</b>

Q135: <b>What are the parts of a house?</b>
   * Macaw-11B: <b>roof, walls, windows, doors</b> (credit: 1)
   * Macaw-3B: <b>walls</b>
   * Macaw-large: <b>the roof, the walls, the floors</b>
   * Macaw-answer-11B: <b>foundation, walls, roof, windows, doors</b> (credit: 1)
   * GPT3-davinci: <b>The parts of a house are the roof, the walls, the floor, the windows, the doors, the stairs, the chimney, the fireplace, the kitchen, the bathroom, the living room, the dining room, the bedroom, the attic, the basement, the garage, the porch, the yard, the</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The parts of a house are the roof, walls, floor, and foundation.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>foundation</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>foundation</b>
   * T5-XL-SSM-NQ: <b>foundation</b>
   * T5-large-SSM-NQ: <b>rooms</b>
   * T5-small-SSM-NQ: <b>one or more houses</b>

Q136: <b>What does the roof do in a house?</b>
   * Macaw-11B: <b>protects the house</b> (credit: 1)
   * Macaw-3B: <b>protects the occupants</b>
   * Macaw-large: <b>protects the house</b>
   * Macaw-answer-11B: <b>keeps rain and snow out</b> (credit: 1)
   * GPT3-davinci: <b>It protects the house from the rain.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The roof protects the house from rain, snow, wind, and sun.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>provides insulation</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>provides shelter</b>
   * T5-XL-SSM-NQ: <b>water protection and heat insulation</b>
   * T5-large-SSM-NQ: <b>a protective layer over the roof</b>
   * T5-small-SSM-NQ: <b>to reduce weight</b>

Q137: <b>What is the purpose of a roof in a house?</b>
   * Macaw-11B: <b>keep the rain out</b> (credit: 1)
   * Macaw-3B: <b>to protect the occupants from the weather</b>
   * Macaw-large: <b>provide protection</b>
   * Macaw-answer-11B: <b>keep rain and snow out</b> (credit: 1)
   * GPT3-davinci: <b>To protect the house from the rain.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The main purpose of a roof is to protect a house from rain, snow, wind, and sun.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to provide insulation</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>protection from the elements</b>
   * T5-XL-SSM-NQ: <b>to provide shelter</b>
   * T5-large-SSM-NQ: <b>insulation</b>
   * T5-small-SSM-NQ: <b>to regulate the home</b>

Q138: <b>What is the purpose of the walls in a house?</b>
   * Macaw-11B: <b>provide support</b> (credit: 1)
   * Macaw-3B: <b>to keep out animals</b>
   * Macaw-large: <b>to protect the house</b>
   * Macaw-answer-11B: <b>to keep the heat in</b> (credit: 1)
   * GPT3-davinci: <b>The walls in a house are there to protect the people inside from the elements.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The walls in a house serve many purposes. They separate the rooms, provide privacy, and hold up the roof.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>provide insulation</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>separating rooms</b>
   * T5-XL-SSM-NQ: <b>insulation</b>
   * T5-large-SSM-NQ: <b>insulation</b>
   * T5-small-SSM-NQ: <b>to regulate home life</b>

Q139: <b>What is the purpose of the windows in a house?</b>
   * Macaw-11B: <b>to let in light and air</b> (credit: 1)
   * Macaw-3B: <b>to let in light</b>
   * Macaw-large: <b>to let in light</b>
   * Macaw-answer-11B: <b>let in light and air</b> (credit: 1)
   * GPT3-davinci: <b>To let the sun in.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Windows are openings in a building envelope that allow light and air to enter.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to let in light and air</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>admit light and air</b>
   * T5-XL-SSM-NQ: <b>allow light to enter</b>
   * T5-large-SSM-NQ: <b>insulation</b>
   * T5-small-SSM-NQ: <b>to evangelize the home</b>

Q140: <b>What is the purpose of the doors in a house?</b>
   * Macaw-11B: <b>to let in air</b> (credit: 1)
   * Macaw-3B: <b>to provide access to rooms</b>
   * Macaw-large: <b>to let in light</b>
   * Macaw-answer-11B: <b>to allow people to enter and leave the house</b> (credit: 1)
   * GPT3-davinci: <b>To keep the heat in during the winter and the cool air in during the summer.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Doors are for privacy, security, and protection.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to provide insulation</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>entrance/exit</b>
   * T5-XL-SSM-NQ: <b>to provide insulation</b>
   * T5-large-SSM-NQ: <b>vestibules or accessory systems</b>
   * T5-small-SSM-NQ: <b>to open the house</b>

Q141: <b>Name an object that is attracted by a magnet.</b>
   * Macaw-11B: <b>iron nails</b> (credit: 1)
   * Macaw-3B: <b>metal</b>
   * Macaw-large: <b>iron nail</b>
   * Macaw-answer-11B: <b>iron filings</b> (credit: 1)
   * GPT3-davinci: <b>Iron</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A compass needle.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>steel</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>iron filings</b>
   * T5-XL-SSM-NQ: <b>magnetosextiles</b>
   * T5-large-SSM-NQ: <b>a wire</b>
   * T5-small-SSM-NQ: <b>mass</b>

Q142: <b>Name an object other than a nail that is attracted by a magnet.</b>
   * Macaw-11B: <b>a paper clip</b> (credit: 1)
   * Macaw-3B: <b>a hair</b>
   * Macaw-large: <b>nail</b>
   * Macaw-answer-11B: <b>iron filings</b> (credit: 1)
   * GPT3-davinci: <b>A compass.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A piece of iron.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>steel</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>copper</b>
   * T5-XL-SSM-NQ: <b>magnetoencephalograph</b>
   * T5-large-SSM-NQ: <b>other inanimate objects</b>
   * T5-small-SSM-NQ: <b>magnetite</b>

Q143: <b>Name an object other than a nail or a paper clip that is attracted by a magnet.</b>
   * Macaw-11B: <b>a refrigerator</b> (credit: 1)
   * Macaw-3B: <b>a hair</b>
   * Macaw-large: <b>a paper clip</b>
   * Macaw-answer-11B: <b>iron filings</b> (credit: 1)
   * GPT3-davinci: <b>A compass.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A piece of iron.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>cork</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>refrigerator magnets</b>
   * T5-XL-SSM-NQ: <b>magnetos</b>
   * T5-large-SSM-NQ: <b>other inanimate objects</b>
   * T5-small-SSM-NQ: <b>magnetite</b>

Q144: <b>Why was Aristotle's hometown more similar to California than New York?</b>
   * Macaw-11B: <b>climate</b> (credit: 1)
   * Macaw-3B: <b>lower elevation</b>
   * Macaw-large: <b>it's closer</b>
   * Macaw-answer-11B: <b>it was a desert</b> (credit: 1)
   * GPT3-davinci: <b>Because it was a small town with a lot of intellectuals.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because Aristotle was from California.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>because of its size</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>its mild climate</b>
   * T5-XL-SSM-NQ: <b>more deserted</b>
   * T5-large-SSM-NQ: <b>its proximity to California</b>
   * T5-small-SSM-NQ: <b>trade</b>

Q145: <b>Why would Aristotle have preferred a short-sleeved shirt over a warm jacket?</b>
   * Macaw-11B: <b>he was a warm-blooded person</b> (credit: 0)
   * Macaw-3B: <b>to conserve warmth</b>
   * Macaw-large: <b>he was cold-blooded</b>
   * Macaw-answer-11B: <b>he was a naturalist</b> (credit: 0)
   * GPT3-davinci: <b>Because he was a philosopher, and philosophers are always cold.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because he was Greek.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>it kept him cooler</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>more comfortable</b>
   * T5-XL-SSM-NQ: <b>a more comfortable temperature</b>
   * T5-large-SSM-NQ: <b>insulation</b>
   * T5-small-SSM-NQ: <b>to promote social policy</b>

Q146: <b>How would you make a table stronger?</b>
   * Macaw-11B: <b>add more supports</b> (credit: 1)
   * Macaw-3B: <b>add more legs</b>
   * Macaw-large: <b>use more nails</b>
   * Macaw-answer-11B: <b>add a center support</b> (credit: 1)
   * GPT3-davinci: <b>I would make the legs thicker.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Put a tablecloth on it.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>bracing</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>by adding legs</b>
   * T5-XL-SSM-NQ: <b>using a stronger material</b>
   * T5-large-SSM-NQ: <b>by using magnets</b>
   * T5-small-SSM-NQ: <b>for a better future</b>

Q147: <b>How would you make a rope stronger?</b>
   * Macaw-11B: <b>add strands</b> (credit: 1)
   * Macaw-3B: <b>add more fibers</b>
   * Macaw-large: <b>tie it up</b>
   * Macaw-answer-11B: <b>add strands</b> (credit: 1)
   * GPT3-davinci: <b>You could make it thicker, or you could make it longer.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Add more strands to it.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>strands of smaller diameter</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>by wrapping it in plastic</b>
   * T5-XL-SSM-NQ: <b>using a special chemical reaction</b>
   * T5-large-SSM-NQ: <b>Rope splicing</b>
   * T5-small-SSM-NQ: <b>more than 180 minutes</b>

Q148: <b>How would you make a blanket stronger?</b>
   * Macaw-11B: <b>add layers</b> (credit: 1)
   * Macaw-3B: <b>add more yarn</b>
   * Macaw-large: <b>use more yarn</b>
   * Macaw-answer-11B: <b>sew it</b> (credit: 0)
   * GPT3-davinci: <b>I would make it out of steel.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Add more yarn.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>adding stitched details</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>blanket stitching</b>
   * T5-XL-SSM-NQ: <b>using iron sulfide</b>
   * T5-large-SSM-NQ: <b>by gluing it together</b>
   * T5-small-SSM-NQ: <b>insulation</b>

Q149: <b>How would you make a marriage stronger?</b>
   * Macaw-11B: <b>communicate</b> (credit: 1)
   * Macaw-3B: <b>make it last longer</b>
   * Macaw-large: <b>strengthen the bond</b>
   * Macaw-answer-11B: <b>communicate</b> (credit: 1)
   * GPT3-davinci: <b>I would make sure that I was the one who was always right.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>By being kind to each other.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>communication</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>improving communication</b>
   * T5-XL-SSM-NQ: <b>by making it more Biblical</b>
   * T5-large-SSM-NQ: <b>strengthening its foundations</b>
   * T5-small-SSM-NQ: <b>gives marriage to another partner</b>

Q150: <b>How would you make an investment stronger?</b>
   * Macaw-11B: <b>diversify</b> (credit: 1)
   * Macaw-3B: <b>use a higher quality stock</b>
   * Macaw-large: <b>increase the amount of time you have</b>
   * Macaw-answer-11B: <b>diversify</b> (credit: 1)
   * GPT3-davinci: <b>I would make it more transparent. I would make it more accountable. I would make it more responsive to the needs of the people.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>By making it more liquid.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>diversification</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>diversification</b>
   * T5-XL-SSM-NQ: <b>Buy-ins</b>
   * T5-large-SSM-NQ: <b>by leveraging it</b>
   * T5-small-SSM-NQ: <b>about $1.18 trillion</b>

Q151: <b>How would you mkae a balloon stronger?</b>
   * Macaw-11B: <b>add air</b> (credit: 0)
   * Macaw-3B: <b>fill it with helium</b>
   * Macaw-large: <b>a stronger wire</b>
   * Macaw-answer-11B: <b>add air</b> (credit: 0)
   * GPT3-davinci: <b>You could make it out of a stronger material.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Put in more hot air.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>adding more balloons</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>by adding more air</b>
   * T5-XL-SSM-NQ: <b>to make it stronger</b>
   * T5-large-SSM-NQ: <b>by using force</b>
   * T5-small-SSM-NQ: <b>to identify a number</b>

Q152: <b>How would you make a road stronger?</b>
   * Macaw-11B: <b>add layers</b> (credit: 1)
   * Macaw-3B: <b>add concrete</b>
   * Macaw-large: <b>increase the amount of rocks in it</b>
   * Macaw-answer-11B: <b>add more layers</b> (credit: 1)
   * GPT3-davinci: <b>I would make it out of concrete.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Add more lanes.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>adding bitumen</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>using asphalt</b>
   * T5-XL-SSM-NQ: <b>by using cork</b>
   * T5-large-SSM-NQ: <b>strengthening</b>
   * T5-small-SSM-NQ: <b>strengthening its goals</b>

Q153: <b>How would you make a window stronger?</b>
   * Macaw-11B: <b>double pane</b> (credit: 1)
   * Macaw-3B: <b>add a frame</b>
   * Macaw-large: <b>use a heavier weight</b>
   * Macaw-answer-11B: <b>double pane</b> (credit: 1)
   * GPT3-davinci: <b>I would make it out of a stronger material.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Put a pane of glass in it.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>by adding a metal interlayer</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>using tempered glass</b>
   * T5-XL-SSM-NQ: <b>using a metal frame</b>
   * T5-large-SSM-NQ: <b>splicing</b>
   * T5-small-SSM-NQ: <b>strengthening its eye</b>

Q154: <b>How would you make a contract stronger?</b>
   * Macaw-11B: <b>add more clauses</b> (credit: 1)
   * Macaw-3B: <b>add more material</b>
   * Macaw-large: <b>make it more than one year</b>
   * Macaw-answer-11B: <b>have it notarized</b> (credit: 1)
   * GPT3-davinci: <b>I would make it so that the contract is only valid if the other party is still alive.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>By making it longer.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>unilateralism</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>by adding additional conditions</b>
   * T5-XL-SSM-NQ: <b>enforceability</b>
   * T5-large-SSM-NQ: <b>add-on clauses</b>
   * T5-small-SSM-NQ: <b>strengthening the match</b>

Q155: <b>What does colorless mean?</b>
   * Macaw-11B: <b>no hue</b> (credit: 1)
   * Macaw-3B: <b>without color</b>
   * Macaw-large: <b>no color</b>
   * Macaw-answer-11B: <b>without hue or hues</b> (credit: 1)
   * GPT3-davinci: <b>Colorless means that the card has no color in its mana cost.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Colorless diamonds are graded on a scale from D to Z, with D being the most colorless and Z being the most yellow.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>without color</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>having no color</b>
   * T5-XL-SSM-NQ: <b>colorless objects</b>
   * T5-large-SSM-NQ: <b>a deeper blue</b>
   * T5-small-SSM-NQ: <b>variety of color</b>

Q156: <b>Does oxygen have a hue?</b>
   * Macaw-11B: <b>no</b> (credit: 1)
   * Macaw-3B: <b>no</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>Yes, oxygen is a pale blue color.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Oxygen is colorless. However, oxygen gas is pale blue when cooled to -183\[Degree]C.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>colorless</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>colorless</b>
   * T5-XL-SSM-NQ: <b>blue</b>
   * T5-large-SSM-NQ: <b>cyan</b>
   * T5-small-SSM-NQ: <b>water</b>

## Generation

Q157: <b>Tell me a story about a car accident.</b>
   * Macaw-11B: <b>a friend was driving and got into an accident</b> (credit: 1)
   * Macaw-3B: <b>it was a terrible accident</b>
   * Macaw-large: <b>a girl in a car accident, her mother in a crash</b>
   * Macaw-answer-11B: <b>a friend was in a car accident and died</b> (credit: 1)
   * GPT3-davinci: <b>I was in a car accident once. I was driving and I hit a car.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>I was in a car accident.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Paul</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>"Peter"</b>
   * T5-XL-SSM-NQ: <b>"Flight"</b>
   * T5-large-SSM-NQ: <b>30 years ago</b>
   * T5-small-SSM-NQ: <b>collision</b>

## History

Q158: <b>What were the causes of World War II?</b>
   * Macaw-11B: <b>the rise of totalitarianism in europe and the pacific</b> (credit: 1)
   * Macaw-3B: <b>the rise of fascism</b>
   * Macaw-large: <b>atomic bombs</b>
   * Macaw-answer-11B: <b>the rise of fascism and the rise of nationalist movements</b> (credit: 1)
   * GPT3-davinci: <b>The causes of World War II were the rise of fascism in Germany, Italy, and Japan, the failure of the League of Nations to prevent World War I, the Treaty of Versailles, the Great Depression, and the rise of totalitarianism.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The causes of World War II were primarily the aggression of Germany, Italy, and Japan.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Italian fascism in the 1920s</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>Italian fascism in the 1920s</b>
   * T5-XL-SSM-NQ: <b>Italian fascism in the 1920s</b>
   * T5-large-SSM-NQ: <b>Italian fascism in the 1920s</b>
   * T5-small-SSM-NQ: <b>Italian fascism in the 1920s</b>

Q159: <b>What were the main problems with the League of Nations, formed in 1920?</b>
   * Macaw-11B: <b>it was not strong enough</b> (credit: 1)
   * Macaw-3B: <b>it was not a world government</b>
   * Macaw-large: <b>it was formed from members who did not have enough money to form a government</b>
   * Macaw-answer-11B: <b>it was not able to prevent wars</b> (credit: 1)
   * GPT3-davinci: <b>The League of Nations was a failure because it was not able to prevent World War II.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The League of Nations was an international organization created after World War I. It aimed to prevent future wars by settling disputes between countries through negotiation and diplomacy. The League of Nations was ineffective, however, because it lacked enforcement powers.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>its inability to control or prevent wars</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>too much power</b>
   * T5-XL-SSM-NQ: <b>the League's disorganization</b>
   * T5-large-SSM-NQ: <b>its currency</b>
   * T5-small-SSM-NQ: <b>Defense of states' rights</b>

## Human behavior

Q160: <b>How should I break up with my girlfriend?</b>
   * Macaw-11B: <b>in person</b> (credit: 1)
   * Macaw-3B: <b>tell her I love her</b>
   * Macaw-large: <b>call her</b>
   * Macaw-answer-11B: <b>in person</b> (credit: 1)
   * GPT3-davinci: <b>You should break up with your girlfriend the same way you would break up with your boyfriend.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Break up with her in person.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>delicately</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>nicely</b>
   * T5-XL-SSM-NQ: <b>Sexy or not</b>
   * T5-large-SSM-NQ: <b>not to continue dating</b>
   * T5-small-SSM-NQ: <b>kissing</b>

Q161: <b>I feel sad. What could I do to cheer myself up?</b>
   * Macaw-11B: <b>laugh</b> (credit: 1)
   * Macaw-3B: <b>laugh</b>
   * Macaw-large: <b>take a walk</b>
   * Macaw-answer-11B: <b>listen to music</b> (credit: 1)
   * GPT3-davinci: <b>I feel sad. What could I do to cheer myself up?</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Sadness is a normal emotion. It's part of being human.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>listening to upbeat music</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>reading a book</b>
   * T5-XL-SSM-NQ: <b>reading</b>
   * T5-large-SSM-NQ: <b>cheering</b>
   * T5-small-SSM-NQ: <b>tributes to Germany</b>

Q162: <b>Why is it hard to find good building contractors?</b>
   * Macaw-11B: <b>many bad ones</b> (credit: 1)
   * Macaw-3B: <b>they are hard to find</b>
   * Macaw-large: <b>low pay</b>
   * Macaw-answer-11B: <b>there are too many bad ones</b> (credit: 1)
   * GPT3-davinci: <b>It's hard to find good building contractors because they are busy. They are busy because they are good.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Finding a good building contractor is like finding a good doctor. You ask around, get recommendations, check credentials, and interview candidates.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>bad referrals</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>building contractors are self-employed</b>
   * T5-XL-SSM-NQ: <b>The contractor shortage</b>
   * T5-large-SSM-NQ: <b>numerous reasons</b>
   * T5-small-SSM-NQ: <b>to fund state benefits</b>

Q163: <b>Almanzo turned to Mr. Thompson and asked, "Did you lose a pocketbook?" Mr. Thompson jumped. He slapped a hand to his pocket and fairly shouted, "Yes, I have! Fifteen hundred dollars in it, too!". What did Mr. Thompson say next?</b>
   * Macaw-11B: <b>he had no money</b> (credit: 0)
   * Macaw-3B: <b>"It's in my pocket."</b>
   * Macaw-large: <b>he had fifteen hundred dollars in his pocket</b>
   * Macaw-answer-11B: <b>he had found it</b> (credit: 0)
   * GPT3-davinci: <b>"I'll give you a hundred dollars if you find it."</b> (credit: 1)
   * Jurassic-1-jumbo: <b>"I lost it at the fair!"</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>"Come on, man"</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>"It's all right"</b>
   * T5-XL-SSM-NQ: <b>"I'm sorry,' Ma'am"</b>
   * T5-large-SSM-NQ: <b>"Fifteen hundred dollars"</b>
   * T5-small-SSM-NQ: <b>"Leashed"</b>

Q164: <b>Almanzo turned to Mr. Thompson and asked, "Did you lose a pocketbook?" Mr. Thompson jumped. He slapped a hand to his pocket and fairly shouted, "Yes, I have! Fifteen hundred dollars in it, too!".  What did Almanzo say in reply?</b>
   * Macaw-11B: <b>he had no idea where it was</b> (credit: 0.5)
   * Macaw-3B: <b>"It's not your money, it's mine."</b>
   * Macaw-large: <b>he had no money in it</b>
   * Macaw-answer-11B: <b>he had found it</b> (credit: 1)
   * GPT3-davinci: <b>"Well, I'll be darned!"</b> (credit: 1)
   * Jurassic-1-jumbo: <b>"Well, Mr. Thompson," he said, "you'd better not lose that pocketbook again."</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>"Oh, really"</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>"Well, I guess so"</b>
   * T5-XL-SSM-NQ: <b>"Not</b>
   * T5-large-SSM-NQ: <b>"Nothin' but the Blues"</b>
   * T5-small-SSM-NQ: <b>"Fifth of May"</b>

## Hypothetical

Q165: <b>If plastic was a conductor, then would a plastic spoon conduct electricity?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>conductor</b>
   * Macaw-answer-11B: <b>no</b> (credit: 0)
   * GPT3-davinci: <b>Yes, but it would be a very poor conductor.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No. Plastic is a non-conductor of electricity.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>yes</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>would conduct electricity</b>
   * T5-XL-SSM-NQ: <b>hypothetically yes</b>
   * T5-large-SSM-NQ: <b>most likely not</b>
   * T5-small-SSM-NQ: <b>connect equipment enclosures to earth</b>

Q166: <b>If plastic was an insulator, then would a plastic spoon conduct electricity?</b>
   * Macaw-11B: <b>no</b> (credit: 1)
   * Macaw-3B: <b>no</b>
   * Macaw-large: <b>no</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>Yes, it would.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>No, plastic is an insulator.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>no</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>not conduct electricity</b>
   * T5-XL-SSM-NQ: <b>metal</b>
   * T5-large-SSM-NQ: <b>most likely not</b>
   * T5-small-SSM-NQ: <b>connect current</b>

Q167: <b>If dinosaurs were alive today, how would the world be different?</b>
   * Macaw-11B: <b>there would be more animals</b> (credit: 1)
   * Macaw-3B: <b>it would be warmer</b>
   * Macaw-large: <b>there would be less pollution</b>
   * Macaw-answer-11B: <b>there would be more dinosaurs</b> (credit: 1)
   * GPT3-davinci: <b>Dinosaurs would be a lot like humans. They would have a lot of the same problems we have. They would have to deal with the same things we have to deal with. They would have to deal with pollution, and they would have to deal with the fact that they're not the biggest animals on the planet anymore</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Dinosaurs were the dominant species on Earth for 165 million years. They ruled the land, sea and air. They dominated every ecosystem. They ruled the world.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>would be much more dangerous</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>many ways</b>
   * T5-XL-SSM-NQ: <b>Earth would be quite different</b>
   * T5-large-SSM-NQ: <b>much cleaner</b>
   * T5-small-SSM-NQ: <b>perhaps three hundred years</b>

Q168: <b>If an asteroid was heading directly for the Earth, what steps could we take to avert catastrophe?</b>
   * Macaw-11B: <b>warn the population</b> (credit: 1)
   * Macaw-3B: <b>build a spaceship</b>
   * Macaw-large: <b>we can take cover from the sun</b>
   * Macaw-answer-11B: <b>build a shield</b> (credit: 0.5)
   * GPT3-davinci: <b>The most likely scenario is that we would discover the asteroid early enough to deflect it. The most likely way to do that is to use a "kinetic impactor" -- a spacecraft that would slam into the asteroid at high speed.
A: The most likely scenario is that we would discover the asteroid early enough to</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The asteroid Apophis, which will pass within 19,000 miles of Earth in 2029, is the closest known asteroid to collide with Earth. But NASA scientists say there is no chance that Apophis will hit us.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>planetary defense</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>space-based lasers</b>
   * T5-XL-SSM-NQ: <b>take out the trash</b>
   * T5-large-SSM-NQ: <b>nuclear weapons testing</b>
   * T5-small-SSM-NQ: <b>deceive the Earth</b>

Q169: <b>If you put a plant in a dark room, how will its photosynthesis be affected?</b>
   * Macaw-11B: <b>it will slow down</b> (credit: 1)
   * Macaw-3B: <b>it will be affected negatively</b>
   * Macaw-large: <b>the plant will not be able to absorb light and will die</b>
   * Macaw-answer-11B: <b>it will not be able to make food</b> (credit: 1)
   * GPT3-davinci: <b>It will not be affected.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Photosynthesis is the process by which plants use sunlight to convert carbon dioxide and water into oxygen and glucose.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>decreased</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>stopped</b>
   * T5-XL-SSM-NQ: <b>decreased light</b>
   * T5-large-SSM-NQ: <b>it will have less light</b>
   * T5-small-SSM-NQ: <b>reaction</b>

Q170: <b>If a bird didn't have wings, how would it be affected?</b>
   * Macaw-11B: <b>it would be unable to fly</b> (credit: 1)
   * Macaw-3B: <b>it would be slower</b>
   * Macaw-large: <b>it would be affected by the lack of air</b>
   * Macaw-answer-11B: <b>it would be unable to fly</b> (credit: 1)
   * GPT3-davinci: <b>It would be a bad bird.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>It wouldn't be able to fly.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>flight</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>it would have trouble flying</b>
   * T5-XL-SSM-NQ: <b>no doubt would be flightless</b>
   * T5-large-SSM-NQ: <b>flight</b>
   * T5-small-SSM-NQ: <b>no longer fully flighted</b>

Q171: <b>If a car did not have any gas in it, how would it be affected?</b>
   * Macaw-11B: <b>it would not move</b> (credit: 1)
   * Macaw-3B: <b>it would not move</b>
   * Macaw-large: <b>it would make fewer revolutions</b>
   * Macaw-answer-11B: <b>it would not move</b> (credit: 1)
   * GPT3-davinci: <b>It would not be affected at all.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The car would not run.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>not moving</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>it would not run</b>
   * T5-XL-SSM-NQ: <b>no start</b>
   * T5-large-SSM-NQ: <b>braked</b>
   * T5-small-SSM-NQ: <b>on some models</b>

Q172: <b>If an electric car did not have any gas in it, how would it be affected?</b>
   * Macaw-11B: <b>it would not move</b> (credit: 0)
   * Macaw-3B: <b>it would not be as fast</b>
   * Macaw-large: <b>it would lose power</b>
   * Macaw-answer-11B: <b>it would not move</b> (credit: 0)
   * GPT3-davinci: <b>It would not be affected at all.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>It would not run.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>no longer charges</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>it would not run</b>
   * T5-XL-SSM-NQ: <b>degraded</b>
   * T5-large-SSM-NQ: <b>crash</b>
   * T5-small-SSM-NQ: <b>not sure what to do</b>

Q173: <b>If a bird did not have wings, would it be able to eat?</b>
   * Macaw-11B: <b>no, it would not be able to catch food</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>it would not be able to fly</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>No, it would starve to death.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, because a bird needs wings to fly.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>beak</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>could not fly</b>
   * T5-XL-SSM-NQ: <b>could</b>
   * T5-large-SSM-NQ: <b>flight</b>
   * T5-small-SSM-NQ: <b>no longer fully flighted</b>

Q174: <b>If there was no sun, how would life be affected?</b>
   * Macaw-11B: <b>no energy</b> (credit: 1)
   * Macaw-3B: <b>it would be cold</b>
   * Macaw-large: <b>there would be no food</b>
   * Macaw-answer-11B: <b>plants would die</b> (credit: 1)
   * GPT3-davinci: <b>The Earth would be a very different place. The temperature would be about -18 degrees Celsius (0 degrees Fahrenheit). There would be no photosynthesis, so no plants or animals. The Earth would be a frozen ball of ice.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Life would be very different. Plants and animals would not be able to make food.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>death</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>death</b>
   * T5-XL-SSM-NQ: <b>would be dark</b>
   * T5-large-SSM-NQ: <b>many other body processes</b>
   * T5-small-SSM-NQ: <b>had been friends</b>

Q175: <b>If my house did not have a roof, and it rained, what would happen to my bed upstairs?</b>
   * Macaw-11B: <b>it would get wet</b> (credit: 1)
   * Macaw-3B: <b>it would be soaked</b>
   * Macaw-large: <b>it would get wet</b>
   * Macaw-answer-11B: <b>it would get wet</b> (credit: 1)
   * GPT3-davinci: <b>You would get wet.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Your bed would float.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>water would get in</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>wet</b>
   * T5-XL-SSM-NQ: <b>water</b>
   * T5-large-SSM-NQ: <b>flood</b>
   * T5-small-SSM-NQ: <b>over the floorboards</b>

Q176: <b>If my house had a roof, and it rained, what would happen to my bed upstairs?</b>
   * Macaw-11B: <b>it would stay dry</b> (credit: 1)
   * Macaw-3B: <b>it would get wet</b>
   * Macaw-large: <b>it would get wet</b>
   * Macaw-answer-11B: <b>it would stay dry</b> (credit: 1)
   * GPT3-davinci: <b>You would get wet.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>It would float away.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>would stay dry</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>get wet</b>
   * T5-XL-SSM-NQ: <b>would be awash</b>
   * T5-large-SSM-NQ: <b>flood</b>
   * T5-small-SSM-NQ: <b>over the floorboards</b>

Q177: <b>If my house did not have a roof, and it rained, what would happen to my bed downstairs?</b>
   * Macaw-11B: <b>it would get wet</b> (credit: 1)
   * Macaw-3B: <b>it would be soaked</b>
   * Macaw-large: <b>it would get wet</b>
   * Macaw-answer-11B: <b>it would get wet</b> (credit: 1)
   * GPT3-davinci: <b>You would get wet.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Your bed would float.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>water would collect</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>wet</b>
   * T5-XL-SSM-NQ: <b>water</b>
   * T5-large-SSM-NQ: <b>be flooded</b>
   * T5-small-SSM-NQ: <b>over the floorboards</b>

Q178: <b>If an airplane runs out of fuel on the runway, what would happen?</b>
   * Macaw-11B: <b>the plane would crash</b> (credit: 0.5)
   * Macaw-3B: <b>it would crash</b>
   * Macaw-large: <b>the plane would land on the grass</b>
   * Macaw-answer-11B: <b>it would have to make an emergency landing</b> (credit: 0)
   * GPT3-davinci: <b>It would crash.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The airplane would crash.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>runaway airplane</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>the airplane will be forced to land</b>
   * T5-XL-SSM-NQ: <b>land</b>
   * T5-large-SSM-NQ: <b>no immediate reaction</b>
   * T5-small-SSM-NQ: <b>no specific meaning</b>

Q179: <b>If a stationary airplane runs out of fuel, what would happen?</b>
   * Macaw-11B: <b>it would fall to the ground</b> (credit: 0)
   * Macaw-3B: <b>it would crash</b>
   * Macaw-large: <b>the plane would land on the ocean floor</b>
   * Macaw-answer-11B: <b>it would fall to the ground</b> (credit: 0)
   * GPT3-davinci: <b>It would crash.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>It would fall from the sky.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>no longer be able to fly</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>die</b>
   * T5-XL-SSM-NQ: <b>land</b>
   * T5-large-SSM-NQ: <b>no engine power</b>
   * T5-small-SSM-NQ: <b>no wind</b>

Q180: <b>If a stationary airplane on the ground runs out of fuel, what would happen?</b>
   * Macaw-11B: <b>it would fall to the ground</b> (credit: 0)
   * Macaw-3B: <b>it would crash</b>
   * Macaw-large: <b>the plane would fly away</b>
   * Macaw-answer-11B: <b>it would stop</b> (credit: 0)
   * GPT3-davinci: <b>It would crash.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>It would fall over.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>no longer be able to fly</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>die</b>
   * T5-XL-SSM-NQ: <b>land itself</b>
   * T5-large-SSM-NQ: <b>no engine power</b>
   * T5-small-SSM-NQ: <b>no wind</b>

Q181: <b>If a car's battery is flat, how would the car be affected?</b>
   * Macaw-11B: <b>it would not start</b> (credit: 1)
   * Macaw-3B: <b>it would not start</b>
   * Macaw-large: <b>the car would lose power</b>
   * Macaw-answer-11B: <b>it would not start</b> (credit: 1)
   * GPT3-davinci: <b>The car would not be able to start.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A flat battery means the car won't start.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>not starting</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>no power</b>
   * T5-XL-SSM-NQ: <b>no start</b>
   * T5-large-SSM-NQ: <b>start moving forward</b>
   * T5-small-SSM-NQ: <b>any abnormal electric current</b>

Q182: <b>If a person had an infinite short-term memory, why wouldn't they need a tally sheet to count things?</b>
   * Macaw-11B: <b>they could remember everything</b> (credit: 1)
   * Macaw-3B: <b>they could remember all the numbers in their head</b>
   * Macaw-large: <b>there would be no mistakes</b>
   * Macaw-answer-11B: <b>they could remember everything</b> (credit: 1)
   * GPT3-davinci: <b>Because they would remember the number of things they had counted.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because they could remember everything.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>perfect memory</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>infinitely fast</b>
   * T5-XL-SSM-NQ: <b>a mental map</b>
   * T5-large-SSM-NQ: <b>no memory at all</b>
   * T5-small-SSM-NQ: <b>A set by a set</b>

Q183: <b>A plant is in a dark room. Will it be able to photosynthesize?</b>
   * Macaw-11B: <b>no, because there is no light</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>the leaves will absorb light</b>
   * Macaw-answer-11B: <b>no, it will not be able to photosynthesize</b> (credit: 1)
   * GPT3-davinci: <b>No.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, because plants need light for photosynthesis.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>in a light-free environment</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>in photosystem II</b>
   * T5-XL-SSM-NQ: <b>in the absence of light</b>
   * T5-large-SSM-NQ: <b>not be able to grow</b>
   * T5-small-SSM-NQ: <b>up to 100 percent plants</b>

Q184: <b>A plant is in a dark room. Will it still grow?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>the leaves will still grow</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>Yes, it will.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Yes, but very slowly.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>in a dim light</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>will not grow</b>
   * T5-XL-SSM-NQ: <b>in the absence of light</b>
   * T5-large-SSM-NQ: <b>still grow</b>
   * T5-small-SSM-NQ: <b>still around the floor</b>

Q185: <b>If a plant had no leaves, could it photosynthesize?</b>
   * Macaw-11B: <b>yes, through root systems</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>it would take in sunlight</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>No. Leaves are the site of photosynthesis.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No. Photosynthesis requires leaves.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>CAM</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>in some cases</b>
   * T5-XL-SSM-NQ: <b>could</b>
   * T5-large-SSM-NQ: <b>without chloroplasts</b>
   * T5-small-SSM-NQ: <b>2</b>

Q186: <b>If you pulled the leaves off a plant, how would it be affected?</b>
   * Macaw-11B: <b>it would die</b> (credit: 1)
   * Macaw-3B: <b>it would die</b>
   * Macaw-large: <b>the plant would die</b>
   * Macaw-answer-11B: <b>it would die</b> (credit: 1)
   * GPT3-davinci: <b>The plant would be affected in a negative way.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>If you pulled the leaves off a plant, the plant would die.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>plant death</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>stressed</b>
   * T5-XL-SSM-NQ: <b>no longer grown</b>
   * T5-large-SSM-NQ: <b>the vascular cambium</b>
   * T5-small-SSM-NQ: <b>to prevent backflow</b>

Q187: <b>If the leaves were pulled off a plant, the plant would not be able to do what?</b>
   * Macaw-11B: <b>make food</b> (credit: 1)
   * Macaw-3B: <b>photosynthesis</b>
   * Macaw-large: <b>make food</b>
   * Macaw-answer-11B: <b>photosynthesis</b> (credit: 1)
   * GPT3-davinci: <b>Grow</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Grow. The leaves provide food for the plants.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>photosynthesis</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>photosynthesis</b>
   * T5-XL-SSM-NQ: <b>photosynthesis</b>
   * T5-large-SSM-NQ: <b>produce new leaves</b>
   * T5-small-SSM-NQ: <b>to do the leaf</b>

Q188: <b>There is a windstorm in the city. How might houses in the city be affected?</b>
   * Macaw-11B: <b>roofs might be blown off</b> (credit: 1)
   * Macaw-3B: <b>roofs may be blown off</b>
   * Macaw-large: <b>blown outside</b>
   * Macaw-answer-11B: <b>roofs might be blown off</b> (credit: 1)
   * GPT3-davinci: <b>The windstorm will affect houses in the city.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The houses in the city might be affected.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>Damage from wind</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>blow away</b>
   * T5-XL-SSM-NQ: <b>flooding</b>
   * T5-large-SSM-NQ: <b>damaged roofs</b>
   * T5-small-SSM-NQ: <b>homeowners</b>

Q189: <b>There is a windstorm in the city. Why might the roofs of houses be blown off?</b>
   * Macaw-11B: <b>the roofs are not secured to the walls</b> (credit: 1)
   * Macaw-3B: <b>the roofs are made of a material that is brittle and can break</b>
   * Macaw-large: <b>the wind could blow the roof off</b>
   * Macaw-answer-11B: <b>the roofs are not secured to the walls</b> (credit: 1)
   * GPT3-davinci: <b>The roofs of houses are blown off because the wind is very strong.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The roofs of houses may be blown off because the windstorm is very strong.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a strong enough wind</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>damage to the structure</b>
   * T5-XL-SSM-NQ: <b>erosion by wind</b>
   * T5-large-SSM-NQ: <b>heavy winds</b>
   * T5-small-SSM-NQ: <b>no wind</b>

Q190: <b>How would you make a house conduct electricity?</b>
   * Macaw-11B: <b>paint it with a metal paint</b> (credit: 1)
   * Macaw-3B: <b>using copper</b>
   * Macaw-large: <b>wiring</b>
   * Macaw-answer-11B: <b>make it made of metal</b> (credit: 1)
   * GPT3-davinci: <b>I would make the house out of metal.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You would have to put wires in it.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>copper wiring</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>a metal like copper</b>
   * T5-XL-SSM-NQ: <b>geothermal heat exchanger</b>
   * T5-large-SSM-NQ: <b>well-insulated insulation</b>
   * T5-small-SSM-NQ: <b>connect equipment enclosures to earth</b>

Q191: <b>If a gas was colored blue, what would this imply?</b>
   * Macaw-11B: <b>it contains a lot of hydrogen</b> (credit: 0)
   * Macaw-3B: <b>it is a kind of gas</b>
   * Macaw-large: <b>it is a liquid</b>
   * Macaw-answer-11B: <b>it is a noble gas</b> (credit: 0)
   * GPT3-davinci: <b>It would imply that the gas was oxygen.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The gas is oxygen.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>its speed</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>a higher boiling point</b>
   * T5-XL-SSM-NQ: <b>low pressure</b>
   * T5-large-SSM-NQ: <b>good fortune</b>
   * T5-small-SSM-NQ: <b>yellow-orange</b>

Q192: <b>If oxygen were blue, what would happen?</b>
   * Macaw-11B: <b>plants would die</b> (credit: 0.5)
   * Macaw-3B: <b>it would make the air look blue</b>
   * Macaw-large: <b>the sky would be blue</b>
   * Macaw-answer-11B: <b>it would be harder to see</b> (credit: 0)
   * GPT3-davinci: <b>You would live a lot longer.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The sky would be blue.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>blue flames</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>death</b>
   * T5-XL-SSM-NQ: <b>death of plants</b>
   * T5-large-SSM-NQ: <b>it would be blue</b>
   * T5-small-SSM-NQ: <b>have stopped growing</b>

Q193: <b>If oxygen were blue, what would be a result?</b>
   * Macaw-11B: <b>the sky would be blue</b> (credit: 0.5)
   * Macaw-3B: <b>it would be a gas</b>
   * Macaw-large: <b>the sky would be blue</b>
   * Macaw-answer-11B: <b>it would be hard to see</b> (credit: 0)
   * GPT3-davinci: <b>The sky would be blue.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You would be blue.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>blue flame</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>death</b>
   * T5-XL-SSM-NQ: <b>yellow-orange</b>
   * T5-large-SSM-NQ: <b>yellow</b>
   * T5-small-SSM-NQ: <b>disme</b>

## Math

Q194: <b>What is 56 + 49?</b>
   * Macaw-11B: <b>87</b> (credit: 0)
   * Macaw-3B: <b>78</b>
   * Macaw-large: <b>79</b>
   * Macaw-answer-11B: <b>105</b> (credit: 1)
   * GPT3-davinci: <b>105</b> (credit: 1)
   * Jurassic-1-jumbo: <b>119</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>125</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>115</b>
   * T5-XL-SSM-NQ: <b>169</b>
   * T5-large-SSM-NQ: <b>56</b>
   * T5-small-SSM-NQ: <b>a decline in food availability</b>

Q195: <b>What is 241 + 7864?</b>
   * Macaw-11B: <b>12345</b> (credit: 0)
   * Macaw-3B: <b>7864</b>
   * Macaw-large: <b>7864</b>
   * Macaw-answer-11B: <b>10503</b> (credit: 0)
   * GPT3-davinci: <b>10,932</b> (credit: 0)
   * Jurassic-1-jumbo: <b>2,000</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>231,7864</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>241</b>
   * T5-XL-SSM-NQ: <b>241</b>
   * T5-large-SSM-NQ: <b>1264</b>
   * T5-small-SSM-NQ: <b>$269.6</b>

## Meta-reasoning

Q196: <b>What is an implication of a cat being an animal?</b>
   * Macaw-11B: <b>it has feelings</b> (credit: 1)
   * Macaw-3B: <b>it has organs</b>
   * Macaw-large: <b>it can carry its own body heat</b>
   * Macaw-answer-11B: <b>it is not a human</b> (credit: 0)
   * GPT3-davinci: <b>It is a living thing.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Cats have claws.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>having Feathers</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>not a robot</b>
   * T5-XL-SSM-NQ: <b>a member of a species</b>
   * T5-large-SSM-NQ: <b>status symbol</b>
   * T5-small-SSM-NQ: <b>the human's environment</b>

Q197: <b>What is an incorrect implication of a cat being an animal?</b>
   * Macaw-11B: <b>it is a human</b> (credit: 1)
   * Macaw-3B: <b>it is a kind of human</b>
   * Macaw-large: <b>it weighs a lot</b>
   * Macaw-answer-11B: <b>cats are not sentient</b> (credit: 1)
   * GPT3-davinci: <b>That it is a mammal.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>That it's an animal.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>mammals</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>not a plant</b>
   * T5-XL-SSM-NQ: <b>anthropomorphism</b>
   * T5-large-SSM-NQ: <b>a species of cat</b>
   * T5-small-SSM-NQ: <b>avoid or mitigate double animal behavior</b>

Q198: <b>What is an implication of something being colorless?</b>
   * Macaw-11B: <b>it is transparent</b> (credit: 1)
   * Macaw-3B: <b>it is not visible</b>
   * Macaw-large: <b>it is impossible to distinguish between white and black</b>
   * Macaw-answer-11B: <b>it lacks hue</b> (credit: 1)
   * GPT3-davinci: <b>It means that it doesn't have any color.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Colorless things have no color.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>invisibility</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>not having a color</b>
   * T5-XL-SSM-NQ: <b>colorless</b>
   * T5-large-SSM-NQ: <b>colorless</b>
   * T5-small-SSM-NQ: <b>colorless</b>

Q199: <b>What is an implication of something being blue?</b>
   * Macaw-11B: <b>it reflects blue light</b> (credit: 1)
   * Macaw-3B: <b>it is a kind of color</b>
   * Macaw-large: <b>it has a blue hue</b>
   * Macaw-answer-11B: <b>it reflects blue light</b> (credit: 1)
   * GPT3-davinci: <b>It is not red.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Blue is the color of sadness.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>perceived by humans</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>having a blue color</b>
   * T5-XL-SSM-NQ: <b>blueness</b>
   * T5-large-SSM-NQ: <b>the quality of its ingredients</b>
   * T5-small-SSM-NQ: <b>its number of neutrons</b>

Q200: <b>What is an implication of something being green?</b>
   * Macaw-11B: <b>it is good for the environment</b> (credit: 1)
   * Macaw-3B: <b>it is a kind of living thing</b>
   * Macaw-large: <b>less carbon dioxide</b>
   * Macaw-answer-11B: <b>it is good for the environment</b> (credit: 1)
   * GPT3-davinci: <b>It is a leaf.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Green is the color of money.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>health</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>environmentally friendly</b>
   * T5-XL-SSM-NQ: <b>ecological</b>
   * T5-large-SSM-NQ: <b>the element chromium</b>
   * T5-small-SSM-NQ: <b>its vast size</b>

Q201: <b>What is an implication of something being colored green?</b>
   * Macaw-11B: <b>it contains chlorophyll</b> (credit: 1)
   * Macaw-3B: <b>it is a kind of plant</b>
   * Macaw-large: <b>it has chlorophyll</b>
   * Macaw-answer-11B: <b>it is alive</b> (credit: 0)
   * GPT3-davinci: <b>It is a plant.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>That it is environmentally friendly.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>health</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>health</b>
   * T5-XL-SSM-NQ: <b>alive</b>
   * T5-large-SSM-NQ: <b>the element chromium</b>
   * T5-small-SSM-NQ: <b>color is unknown</b>

## Riddle

Q202: <b>A young boy was rushed to the hospital emergency room, but the ER doctor saw the boy and refused to operate. "This boy is my son," the doctor said. But the doctor wasn't the boy's father. How could this be?</b>
   * Macaw-11B: <b>the doctor mistook the boy for his own son</b> (credit: 1)
   * Macaw-3B: <b>the doctor was the boy's biological father</b>
   * Macaw-large: <b>the boy's father knew about the boy's condition and was able to help him</b>
   * Macaw-answer-11B: <b>he was a clone</b> (credit: 1)
   * GPT3-davinci: <b>The doctor was the boy's mother.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The ER doctor was the boy's mother.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>medical ID</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>a medical error</b>
   * T5-XL-SSM-NQ: <b>a fatal car accident</b>
   * T5-large-SSM-NQ: <b>born again</b>
   * T5-small-SSM-NQ: <b>thirty-five years old</b>

Q203: <b>A truck driver is going down a one-way street the wrong way and passes at least ten cops. Why is he not caught?</b>
   * Macaw-11B: <b>they are not looking for him</b> (credit: 1)
   * Macaw-3B: <b>he is going too fast</b>
   * Macaw-large: <b>he is not wearing a seat belt</b>
   * Macaw-answer-11B: <b>they are not looking for him</b> (credit: 1)
   * GPT3-davinci: <b>Because he's driving on the one-way street the wrong way.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because he's going the wrong way.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>police presence</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>lucky</b>
   * T5-XL-SSM-NQ: <b>driving while drunk</b>
   * T5-large-SSM-NQ: <b>pulled over</b>
   * T5-small-SSM-NQ: <b>drug trafficking</b>

## Science

Q204: <b>What is the difference between ELMO and BERT?</b>
   * Macaw-11B: <b>elmo is a boy and bert is a girl</b> (credit: 0)
   * Macaw-3B: <b>ELMO is a kind of cellular automaton while BERT is a kind of biological robot</b>
   * Macaw-large: <b>ELMO can be used for generating heat without destroying the environment. BERT can be used for generating electricity by burning waste.</b>
   * Macaw-answer-11B: <b>elmo is a boy and bert is a girl</b> (credit: 0)
   * GPT3-davinci: <b>ELMO is a tool for the analysis of the structure of the text, while BERT is a tool for the analysis of the meaning of the text.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>ELMO is an acronym for Early Learning in Mathematics Online. BERT is an acronym for Building Early Numeracy through Effective Teaching.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>BERT</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>a different voice</b>
   * T5-XL-SSM-NQ: <b>a more expensive system</b>
   * T5-large-SSM-NQ: <b>a second chance to detect abnormalities</b>
   * T5-small-SSM-NQ: <b>the endometriosis</b>

Q205: <b>Which research organization invented the ELMO language model?</b>
   * Macaw-11B: <b>nist</b> (credit: 0)
   * Macaw-3B: <b>nasa</b>
   * Macaw-large: <b>microsoft</b>
   * Macaw-answer-11B: <b>university of washington</b> (credit: 1)
   * GPT3-davinci: <b>The ELMO language model was invented by the Natural Language Processing Group at the University of Edinburgh.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The Defense Advanced Research Projects Agency (DARPA).</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>Dartmouth College</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>IBM</b>
   * T5-XL-SSM-NQ: <b>AT&T Bell Laboratories</b>
   * T5-large-SSM-NQ: <b>the University of Michigan</b>
   * T5-small-SSM-NQ: <b>the University of Kansas</b>

Q206: <b>Is it possible to travel faster than light?</b>
   * Macaw-11B: <b>no</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes, it is possible to travel faster than light</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>Yes.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>No. The speed of light is the ultimate speed limit.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>travel at near-light speeds</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>faster-than-light travel</b>
   * T5-XL-SSM-NQ: <b>is it possible</b>
   * T5-large-SSM-NQ: <b>115,000 km/s</b>
   * T5-small-SSM-NQ: <b>nautical miles</b>

Q207: <b>What is the most important advantage of quantum computing?</b>
   * Macaw-11B: <b>it can simulate physical systems</b> (credit: 0)
   * Macaw-3B: <b>it can perform calculations faster than classical computers</b>
   * Macaw-large: <b>it can be used for many purposes</b>
   * Macaw-answer-11B: <b>it can perform calculations faster</b> (credit: 1)
   * GPT3-davinci: <b>The most important advantage of quantum computing is that it can solve certain problems that are impossible to solve on a classical computer.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Quantum computing is a revolutionary technology. It has the potential to solve certain problems that are intractable for classical computers.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>unrestricted quantum computing</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>quantum error correction</b>
   * T5-XL-SSM-NQ: <b>Breakthrough performance</b>
   * T5-large-SSM-NQ: <b>low-cost</b>
   * T5-small-SSM-NQ: <b>the price</b>

Q208: <b>What is COVID-19?</b>
   * Macaw-11B: <b>a kind of virus</b> (credit: 1)
   * Macaw-3B: <b>a virus that causes AIDS</b>
   * Macaw-large: <b>a compound that combines with other elements to form a new compound</b>
   * Macaw-answer-11B: <b>a bacterium that causes a disease in humans</b> (credit: 0)
   * GPT3-davinci: <b>COVID-19 is a new, experimental, and potentially dangerous drug. It is a combination of the drugs Caffeine and Dextromethorphan.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>COVID-19 is a respiratory illness caused by a new coronavirus.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a gene sequence</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>a virus</b>
   * T5-XL-SSM-NQ: <b>a computer virus</b>
   * T5-large-SSM-NQ: <b>The fourth international avian virus</b>
   * T5-small-SSM-NQ: <b>liquid petroleum fuel</b>

Q209: <b>What makes eggplant purple?</b>
   * Macaw-11B: <b>pigments</b> (credit: 1)
   * Macaw-3B: <b>the pigment in the fruit</b>
   * Macaw-large: <b>pigments</b>
   * Macaw-answer-11B: <b>anthocyanins</b> (credit: 1)
   * GPT3-davinci: <b>Eggplant is purple because it contains a pigment called anthocyanin.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Eggplants get their color from anthocyanins, the same pigments that give blueberries and blackberries their deep hue.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>anthocyanins</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>the anthocyanins</b>
   * T5-XL-SSM-NQ: <b>Capsaicin</b>
   * T5-large-SSM-NQ: <b>rhodopsin</b>
   * T5-small-SSM-NQ: <b>Petals on the Wind</b>

Q210: <b>What causes blossom-end rot?</b>
   * Macaw-11B: <b>fungi</b> (credit: 1)
   * Macaw-3B: <b>dampness</b>
   * Macaw-large: <b>decaying tissue</b>
   * Macaw-answer-11B: <b>a fungus</b> (credit: 1)
   * GPT3-davinci: <b>Blossom-end rot is caused by a calcium deficiency in the plant. It is most common in tomatoes, peppers, and eggplants, but can also occur in other plants.
Blossom-end rot is a physiological disorder, not a disease. It is caused by a lack of calcium in the plant. Cal</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Blossom-end rot is a physiological disorder that occurs when calcium is leached from developing fruit. The calcium is leached from the fruit when the soil is too wet or too dry.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Phylloxera</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>bacterial blight</b>
   * T5-XL-SSM-NQ: <b>the oleum of the soil</b>
   * T5-large-SSM-NQ: <b>torn off by fungus</b>
   * T5-small-SSM-NQ: <b>Commensalism</b>

Q211: <b>How can I find Orion's Belt in the night sky?</b>
   * Macaw-11B: <b>look for the three brightest stars in the constellation</b> (credit: 1)
   * Macaw-3B: <b>look for the constellation of Orion</b>
   * Macaw-large: <b>by looking at the night sky</b>
   * Macaw-answer-11B: <b>look for the three bright stars</b> (credit: 1)
   * GPT3-davinci: <b>Orion's Belt is the three bright stars in a row that form the middle of the Hunter's body.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Orion's Belt is easy to find. Just look south around midnight. The belt is three bright stars in a row.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>three bright stars</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>by using binoculars</b>
   * T5-XL-SSM-NQ: <b>by following the constellation of Orion</b>
   * T5-large-SSM-NQ: <b>by using my binoculars</b>
   * T5-small-SSM-NQ: <b>map projection</b>

Q212: <b>What causes fermentation?</b>
   * Macaw-11B: <b>yeast</b> (credit: 1)
   * Macaw-3B: <b>lactic acid</b>
   * Macaw-large: <b>yeast</b>
   * Macaw-answer-11B: <b>a chemical reaction</b> (credit: 1)
   * GPT3-davinci: <b>Fermentation is caused by yeast. Yeast is a single-celled organism that feeds on sugar and produces alcohol and carbon dioxide as waste products.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Fermentation is caused by yeasts, which are microscopic fungi. Yeasts occur naturally in the air and on plants.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>the yeast</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>acetylation</b>
   * T5-XL-SSM-NQ: <b>yeast</b>
   * T5-large-SSM-NQ: <b>an increased pH</b>
   * T5-small-SSM-NQ: <b>plate tectonics</b>

Q213: <b>A student perfoms an experiment growing two plants. One plant is placed in a dark room and the other plant is placed near a window. The plant near the window grows faster than the plant in the dark.  What does this experiment suggest?</b>
   * Macaw-11B: <b>plants need sunlight</b> (credit: 1)
   * Macaw-3B: <b>sunlight increases plant growth</b>
   * Macaw-large: <b>light has a positive impact on plants</b>
   * Macaw-answer-11B: <b>plants need sunlight</b> (credit: 1)
   * GPT3-davinci: <b>The experiment suggests that plants need light to grow.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The plants near the window receive more sunlight.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>plants need light to grow</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>light stimulates photosynthesis</b>
   * T5-XL-SSM-NQ: <b>light</b>
   * T5-large-SSM-NQ: <b>self-incompatibility</b>
   * T5-small-SSM-NQ: <b>the osmotic flow of light</b>

Q214: <b>A student performs an experiment growing two plants. One plant is placed in a dark room and the other plant is placed near a window. The plant near the window grows slower than the plant in the dark. What does this experiment suggest?</b>
   * Macaw-11B: <b>plants need sunlight</b> (credit: 0)
   * Macaw-3B: <b>light affects plant growth</b>
   * Macaw-large: <b>light has a positive impact on plants</b>
   * Macaw-answer-11B: <b>plants need sunlight</b> (credit: 0)
   * GPT3-davinci: <b>The experiment suggests that plants need light to grow.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The experiment suggests that plants need sunlight to grow.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>photosynthesis</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>light deprivation</b>
   * T5-XL-SSM-NQ: <b>light affects growth</b>
   * T5-large-SSM-NQ: <b>self-incompatibility</b>
   * T5-small-SSM-NQ: <b>the osmotic flow of light</b>

Q215: <b>An experiment is performed with a sealed container. The container starts out with a temperature of 70 degrees F and an air pressure of 20 psi. The container is heated, and the pressure inside the container rises evenly with increased temperature. If the container is cooled back to 70 degrees F, what will the air pressure be?</b>
   * Macaw-11B: <b>20 psi</b> (credit: 1)
   * Macaw-3B: <b>20 psi</b>
   * Macaw-large: <b>the same</b>
   * Macaw-answer-11B: <b>20 psi</b> (credit: 1)
   * GPT3-davinci: <b>The air pressure will be 20 psi.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The air pressure inside the container will be 20 psi.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>29.78 psi</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>15 psi</b>
   * T5-XL-SSM-NQ: <b>100 psi</b>
   * T5-large-SSM-NQ: <b>20 psi</b>
   * T5-small-SSM-NQ: <b>100 psi</b>

Q216: <b>What gases are involved in photosynthesis?</b>
   * Macaw-11B: <b>carbon dioxide</b> (credit: 0.5)
   * Macaw-3B: <b>carbon dioxide</b>
   * Macaw-large: <b>oxygen</b>
   * Macaw-answer-11B: <b>oxygen and carbon dioxide</b> (credit: 1)
   * GPT3-davinci: <b>The main gases involved in photosynthesis are carbon dioxide, water, and oxygen.</b> (credit: 0.66)
   * Jurassic-1-jumbo: <b>Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce glucose and oxygen.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>carbon dioxide</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>carbon dioxide</b>
   * T5-XL-SSM-NQ: <b>Water vapor</b>
   * T5-large-SSM-NQ: <b>Oxygen</b>
   * T5-small-SSM-NQ: <b>vapor</b>

Q217: <b>What is the role of hydrogen peroxide in photosynthesis?</b>
   * Macaw-11B: <b>it is a product of photosynthesis</b> (credit: 1)
   * Macaw-3B: <b>it is a cofactor in the reaction that releases oxygen</b>
   * Macaw-large: <b>it removes carbon from the air</b>
   * Macaw-answer-11B: <b>it is a by-product</b> (credit: 1)
   * GPT3-davinci: <b>Hydrogen peroxide is a byproduct of photosynthesis. It is formed when water is split into oxygen and hydrogen. The oxygen is released into the atmosphere and the hydrogen is used to make glucose.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Hydrogen peroxide (H2O2) is a compound that is produced during photosynthesis. It is produced when water (H2O) is split by the enzyme photosystem II (PSII).</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>reaction centres</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the first electron donor</b>
   * T5-XL-SSM-NQ: <b>the reaction centres</b>
   * T5-large-SSM-NQ: <b>catalyst</b>
   * T5-small-SSM-NQ: <b>light</b>

Q218: <b>What are the products of photosynthesis?</b>
   * Macaw-11B: <b>sugar</b> (credit: 0.5)
   * Macaw-3B: <b>sugar</b>
   * Macaw-large: <b>sugar</b>
   * Macaw-answer-11B: <b>oxygen and sugar</b> (credit: 1)
   * GPT3-davinci: <b>The products of photosynthesis are glucose and oxygen.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Photosynthesis produces carbohydrates, lipids, and proteins.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>carbohydrate molecules</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>carbon dioxide</b>
   * T5-XL-SSM-NQ: <b>carbon dioxide</b>
   * T5-large-SSM-NQ: <b>carbohydrate molecules</b>
   * T5-small-SSM-NQ: <b>ATP and NADPH</b>

Q219: <b>Why is the sky blue?</b>
   * Macaw-11B: <b>because of the reflection of light from the clouds</b> (credit: 1)
   * Macaw-3B: <b>it is made of mostly water</b>
   * Macaw-large: <b>water reflects blue light from the earth's surface</b>
   * Macaw-answer-11B: <b>refraction of light in the sky</b> (credit: 1)
   * GPT3-davinci: <b>Because it's full of air.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because God hates you.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>The answer is simple</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>reflected light</b>
   * T5-XL-SSM-NQ: <b>aether</b>
   * T5-large-SSM-NQ: <b>The silicate minerals</b>
   * T5-small-SSM-NQ: <b>its vast size</b>

Q220: <b>Why does the sky reflect blue light?</b>
   * Macaw-11B: <b>water reflects all colors except blue</b> (credit: 0)
   * Macaw-3B: <b>it is blue in color</b>
   * Macaw-large: <b>because it is blue in color</b>
   * Macaw-answer-11B: <b>because of the high altitude of the sky</b> (credit: 0)
   * GPT3-davinci: <b>The sky is blue because of Rayleigh scattering.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The blue color of the sky is caused by Rayleigh scattering.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>blue light is more energetic</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the atmosphere</b>
   * T5-XL-SSM-NQ: <b>the sky is blue</b>
   * T5-large-SSM-NQ: <b>The effect of refraction</b>
   * T5-small-SSM-NQ: <b>reflecting light</b>

Q221: <b>Why do plants produce sugar?</b>
   * Macaw-11B: <b>to provide energy for the plant</b> (credit: 1)
   * Macaw-3B: <b>to feed their animals</b>
   * Macaw-large: <b>to meet the demand of consumers</b>
   * Macaw-answer-11B: <b>to survive</b> (credit: 1)
   * GPT3-davinci: <b>Plants produce sugar to store energy.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Plants produce sugar (glucose) for energy.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to store energy</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>to store energy</b>
   * T5-XL-SSM-NQ: <b>photosynthesis</b>
   * T5-large-SSM-NQ: <b>to feed the hungry</b>
   * T5-small-SSM-NQ: <b>to boil or steam rice</b>

Q222: <b>Why do plants need energy?</b>
   * Macaw-11B: <b>to make food</b> (credit: 1)
   * Macaw-3B: <b>to make food</b>
   * Macaw-large: <b>to grow</b>
   * Macaw-answer-11B: <b>to grow</b> (credit: 1)
   * GPT3-davinci: <b>Plants need energy to grow and to reproduce.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Plants need energy to grow, reproduce, and carry out other life processes.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to produce more sugar</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>to make food</b>
   * T5-XL-SSM-NQ: <b>photosynthesis</b>
   * T5-large-SSM-NQ: <b>to run cellular processes</b>
   * T5-small-SSM-NQ: <b>to run cellular processes</b>

Q223: <b>Why does it get colder at higher altitudes?</b>
   * Macaw-11B: <b>less sunlight</b> (credit: 0)
   * Macaw-3B: <b>less air</b>
   * Macaw-large: <b>the atmosphere is less dense at higher elevations so there is less sunlight</b>
   * Macaw-answer-11B: <b>less greenhouse gases at higher altitudes</b> (credit: 0)
   * GPT3-davinci: <b>The air pressure is lower at higher altitudes. The air pressure is what keeps the heat in.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The atmosphere gets thinner as you go higher, so there is less air to trap heat.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>decreased atmospheric pressure</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>decreased atmospheric pressure</b>
   * T5-XL-SSM-NQ: <b>Lapse rate</b>
   * T5-large-SSM-NQ: <b>decreased atmospheric pressure</b>
   * T5-small-SSM-NQ: <b>cold-water regions</b>

Q224: <b>How does photosynthesis work?</b>
   * Macaw-11B: <b>sun shines on plants</b> (credit: 1)
   * Macaw-3B: <b>plants absorb sunlight to make food</b>
   * Macaw-large: <b>plants use carbon dioxide and other gases to make food</b>
   * Macaw-answer-11B: <b>sunlight and carbon dioxide are combined to make food</b> (credit: 1)
   * GPT3-davinci: <b>Photosynthesis is the process by which plants and other organisms convert light energy, usually from the Sun, into chemical energy that can be used to fuel the organisms' activities. This chemical energy is stored in carbohydrate molecules, such as sugars, which are synthesized from carbon dioxide and water \[Dash] hence the name photosynthesis, from</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce glucose and oxygen.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>reaction centres</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>reaction centres</b>
   * T5-XL-SSM-NQ: <b>light energy</b>
   * T5-large-SSM-NQ: <b>light</b>
   * T5-small-SSM-NQ: <b>in photosystem II</b>

Q225: <b>What are the inputs for photosynthesis?</b>
   * Macaw-11B: <b>sunlight, carbon dioxide, water</b> (credit: 1)
   * Macaw-3B: <b>carbon dioxide</b>
   * Macaw-large: <b>sunlight and energy from the sun</b>
   * Macaw-answer-11B: <b>carbon dioxide, hydrogen, water</b> (credit: 1)
   * GPT3-davinci: <b>Sunlight, water, and carbon dioxide.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Photosynthesis requires sunlight, carbon dioxide, and water.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>light energy</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>carbon dioxide</b>
   * T5-XL-SSM-NQ: <b>light energy</b>
   * T5-large-SSM-NQ: <b>light</b>
   * T5-small-SSM-NQ: <b>light</b>

Q226: <b>List the inputs of photosynthesis.</b>
   * Macaw-11B: <b>sunlight, carbon dioxide, water</b> (credit: 1)
   * Macaw-3B: <b>carbon dioxide</b>
   * Macaw-large: <b>glucose and light</b>
   * Macaw-answer-11B: <b>carbon dioxide, hydrogen, water</b> (credit: 1)
   * GPT3-davinci: <b>Sunlight, water, carbon dioxide, and minerals.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Light, carbon dioxide, water, and chlorophyll.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>carbon dioxide</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>carbon dioxide</b>
   * T5-XL-SSM-NQ: <b>light energy</b>
   * T5-large-SSM-NQ: <b>water</b>
   * T5-small-SSM-NQ: <b>ATP</b>

Q227: <b>What are the outputs of photosynthesis?</b>
   * Macaw-11B: <b>sugar</b> (credit: 0.5)
   * Macaw-3B: <b>sugar</b>
   * Macaw-large: <b>glucose</b>
   * Macaw-answer-11B: <b>oxygen and sugar</b> (credit: 1)
   * GPT3-davinci: <b>The outputs of photosynthesis are oxygen and glucose.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Photosynthesis produces carbohydrates and oxygen.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>carbohydrate molecules</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>carbon dioxide</b>
   * T5-XL-SSM-NQ: <b>ATP and NADPH</b>
   * T5-large-SSM-NQ: <b>carbohydrate molecules</b>
   * T5-small-SSM-NQ: <b>light</b>

Q228: <b>List the outputs of photosynthesis.</b>
   * Macaw-11B: <b>sugar</b> (credit: 0.5)
   * Macaw-3B: <b>oxygen</b>
   * Macaw-large: <b>glucose, oxygen and carbohydrates</b>
   * Macaw-answer-11B: <b>oxygen, sugar, water</b> (credit: 0.66)
   * GPT3-davinci: <b>The products of photosynthesis are oxygen and glucose.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Oxygen, glucose, and ATP.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>carbohydrate molecules</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>carbon dioxide</b>
   * T5-XL-SSM-NQ: <b>carbon dioxide</b>
   * T5-large-SSM-NQ: <b>carbohydrate molecules</b>
   * T5-small-SSM-NQ: <b>ATP</b>

Q229: <b>Where does photosynthesis occur?</b>
   * Macaw-11B: <b>in plants</b> (credit: 1)
   * Macaw-3B: <b>in the leaves of a plant</b>
   * Macaw-large: <b>in plants</b>
   * Macaw-answer-11B: <b>in plants</b> (credit: 1)
   * GPT3-davinci: <b>Photosynthesis occurs in the chloroplasts of plant cells.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Photosynthesis occurs in chloroplasts.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>thylakoid membranes</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>thylakoid membranes</b>
   * T5-XL-SSM-NQ: <b>thylakoid membranes</b>
   * T5-large-SSM-NQ: <b>on the thylakoid membranes</b>
   * T5-small-SSM-NQ: <b>in the ice caps</b>

Q230: <b>In what part of a plant does photosynthesis occur?</b>
   * Macaw-11B: <b>leaves</b> (credit: 1)
   * Macaw-3B: <b>leaves</b>
   * Macaw-large: <b>leaf</b>
   * Macaw-answer-11B: <b>leaves</b> (credit: 1)
   * GPT3-davinci: <b>In the leaves.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Photosynthesis occurs in the leaves.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>cyanobacteria</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>in chloroplasts</b>
   * T5-XL-SSM-NQ: <b>thylakoid membranes</b>
   * T5-large-SSM-NQ: <b>in the stroma of chloroplast</b>
   * T5-small-SSM-NQ: <b>in the stroma</b>

Q231: <b>List all the gases involved in photosynthesis.</b>
   * Macaw-11B: <b>oxygen, carbon dioxide, water vapor, nitrogen</b> (credit: 1)
   * Macaw-3B: <b>carbon dioxide</b>
   * Macaw-large: <b>oxygen - carbon dioxide</b>
   * Macaw-answer-11B: <b>oxygen, carbon dioxide, nitrogen</b> (credit: 1)
   * GPT3-davinci: <b>Oxygen, carbon dioxide, water vapor, and nitrogen.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Oxygen, carbon dioxide, and hydrogen.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>carbon dioxide</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>carbon dioxide</b>
   * T5-XL-SSM-NQ: <b>Water</b>
   * T5-large-SSM-NQ: <b>water</b>
   * T5-small-SSM-NQ: <b>water</b>

Q232: <b>What force causes a ball to roll downhill?</b>
   * Macaw-11B: <b>gravity</b> (credit: 1)
   * Macaw-3B: <b>gravity</b>
   * Macaw-large: <b>gravity</b>
   * Macaw-answer-11B: <b>gravity</b> (credit: 1)
   * GPT3-davinci: <b>Gravity.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Gravity.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>gravity</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>gravity</b>
   * T5-XL-SSM-NQ: <b>gravity</b>
   * T5-large-SSM-NQ: <b>gravity</b>
   * T5-small-SSM-NQ: <b>gravity</b>

Q233: <b>How does a volcanic eruption interfere with the ability of producers to obtain the energy they need to produce food?</b>
   * Macaw-11B: <b>the eruption blocks the sun</b> (credit: 1)
   * Macaw-3B: <b>the nutrients are destroyed</b>
   * Macaw-large: <b>by disrupting the sunlight from reaching producers</b>
   * Macaw-answer-11B: <b>less sunlight</b> (credit: 1)
   * GPT3-davinci: <b>Volcanic eruptions can have a significant impact on the availability of energy for food production. Volcanic eruptions can release large amounts of sulfur dioxide into the atmosphere. Sulfur dioxide reacts with water vapor to form sulfuric acid, which can be carried by the wind for thousands of miles. The sulfuric</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>The eruption of a volcano can disrupt the flow of energy to producers.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>by reducing available light</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>reduces soil fertility</b>
   * T5-XL-SSM-NQ: <b>without food</b>
   * T5-large-SSM-NQ: <b>will have no effect on food production</b>
   * T5-small-SSM-NQ: <b>produce power</b>

Q234: <b>How does a volcanic eruption result in reduced sunlight?</b>
   * Macaw-11B: <b>ash in the atmosphere reflects light</b> (credit: 1)
   * Macaw-3B: <b>ash clouds block sunlight</b>
   * Macaw-large: <b>ash from the eruption clouds the sky</b>
   * Macaw-answer-11B: <b>ash clouds</b> (credit: 1)
   * GPT3-davinci: <b>Volcanic eruptions can result in reduced sunlight in two ways. First, the eruption can result in a large amount of ash and other particles in the atmosphere. This can block sunlight from reaching the surface of the Earth. Second, volcanic eruptions can result in a large amount of sulfur dioxide being released into the atmosphere</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The ash and gases released into the atmosphere by volcanic eruptions reflect sunlight back into space.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>clouds</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>ashfall</b>
   * T5-XL-SSM-NQ: <b>create a cloudy sky</b>
   * T5-large-SSM-NQ: <b>a cooler atmosphere</b>
   * T5-small-SSM-NQ: <b>indirectly using concentrated solar power</b>

Q235: <b>Why does a reduction in sunlight cause producers to receive less energy than they need to produce food?</b>
   * Macaw-11B: <b>less sunlight means less energy for photosynthesis</b> (credit: 1)
   * Macaw-3B: <b>plants require sunlight for photosynthesis</b>
   * Macaw-large: <b>the plant requires sunlight for photosynthesis</b>
   * Macaw-answer-11B: <b>less energy</b> (credit: 0)
   * GPT3-davinci: <b>The energy from the sun is not directly used by plants. Plants use the energy from the sun to convert carbon dioxide and water into glucose and oxygen. Plants use the glucose to produce energy and the oxygen is released into the atmosphere.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Because plants use sunlight to make food.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>photosynthesis</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>less sunlight</b>
   * T5-XL-SSM-NQ: <b>Decline of photosynthesis</b>
   * T5-large-SSM-NQ: <b>decreased sunlight</b>
   * T5-small-SSM-NQ: <b>decreased food availability</b>

Q236: <b>List all the birds.</b>
   * Macaw-11B: <b>wrens, cardinals, robins, eagles, hawks, sparrows, red-winged blackbirds, tufted titmice, red-breasted nuthatches, tufted flycatchers, painted buntings, red-breasted nuthatches, tufted titmice, black-throated blue warblers, painted green heron, sandpipers, black-throated blue-birds</b> (credit: 1)
   * Macaw-3B: <b>eagle, hawk, owl, crow, heron, vulture</b>
   * Macaw-large: <b>type of bird</b>
   * Macaw-answer-11B: <b>hummingbird, cardinal, robin, goldfinch, kingfisher, robin redbreast, robin smallwing, robin largewing, robin small, robin largewing, robin small, robin small, robin small, robin small, robin small, robin smallwing, robin small, robin small, robin small, robin small, robin smallwings, and robits, ; ;</b> (credit: 1)
   * GPT3-davinci: <b>The birds are:</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The birds that fly.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>pigeon</b> (credit: 0.2)
   * T5-11B-SSM-NQ: <b>the killdeer</b>
   * T5-XL-SSM-NQ: <b>eagles</b>
   * T5-large-SSM-NQ: <b>passerine birds</b>
   * T5-small-SSM-NQ: <b>9</b>

Q237: <b>List all the animals.</b>
   * Macaw-11B: <b>apes, wolves, foxes, raccoons, skunks, snakes, lizards, frogs, toads, fish, amphibians, birds, mammals, reptiles, amphibians, fish, frogs, toads, and snakes</b> (credit: 1)
   * Macaw-3B: <b>mammals</b>
   * Macaw-large: <b>birds, mammals, fish, insects</b>
   * Macaw-answer-11B: <b>lion, tiger, bear, fox, giraffe, zebra, giraffe, ostrich, penguin, sea lion, sea cow, ostrich, giraffe, opossum, octopus, penguin, octopus, octopus, octopus, octopus, octopus, octopus, octopus, octo</b> (credit: 1)
   * GPT3-davinci: <b>Dog, cat, mouse, cow, pig, chicken, duck, horse, sheep, goat, fish, snake, bird, and frog.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A dog, a cat, a frog, a duck, a goose, a sheep, a cow, a goat, a donkey, a horse, a camel, a giraffe, a zebra, a kangaroo, a koala, a panda, a penguin, a polar bear, a seal, a walrus, a whale, a dolphin, a</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>pigeon</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Antelope</b>
   * T5-XL-SSM-NQ: <b>Carnivora</b>
   * T5-large-SSM-NQ: <b>cats</b>
   * T5-small-SSM-NQ: <b>all animal facts</b>

Q238: <b>List all the mammals.</b>
   * Macaw-11B: <b>apes, whales, dolphins, walruses, penguins, sea lions, and polar bears</b> (credit: 1)
   * Macaw-3B: <b>mammals</b>
   * Macaw-large: <b>mammals</b>
   * Macaw-answer-11B: <b>mammals include humans, whales, dolphins, and seals</b> (credit: 1)
   * GPT3-davinci: <b>The mammals are:</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Mammals are warm-blooded animals that have hair or fur, feed their young with milk, and suckle their young.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>Carnivora</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>rodents</b>
   * T5-XL-SSM-NQ: <b>rodents</b>
   * T5-large-SSM-NQ: <b>cats</b>
   * T5-small-SSM-NQ: <b>Crepuscular</b>

Q239: <b>List all the snakes.</b>
   * Macaw-11B: <b>python, coral snake, king cobra, black racer, western coral snake, western coral snake</b> (credit: 1)
   * Macaw-3B: <b>venomous</b>
   * Macaw-large: <b>type of snake</b>
   * Macaw-answer-11B: <b>vipers, boa constrictors, coral snakes, king snakes, milk snakes, western diamondbacks, eastern diamondbacks, western diamondback kings, eastern diamondback kings, western diamondback kings, western diamondback kings, western diamondback kings, western diamondback kings, western diamondback kings, western diamondback kings, western diamondback kings, western diamondback kings, western diamondback kings,,,,,,,</b> (credit: 1)
   * GPT3-davinci: <b>There are two snakes in the game. The first is the snake that you play as. The second is the snake that you play against.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Snakes are reptiles. They do not have legs. Snakes do not have arms. Snakes do not have fingers. Snakes do not have toes. Snakes do not have ears. Snakes do not have noses. Snakes do not have tongues. Snakes do not have hair. Snakes do not have fur. Snakes do not have feathers. Snakes do not have scales. Snakes do not have shells. Snake</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>71</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>colubrid snakes</b>
   * T5-XL-SSM-NQ: <b>colubrid snakes</b>
   * T5-large-SSM-NQ: <b>Eastern brown snake</b>
   * T5-small-SSM-NQ: <b>Raju</b>

Q240: <b>How many legs does a snake have?</b>
   * Macaw-11B: <b>8</b> (credit: 0)
   * Macaw-3B: <b>8</b>
   * Macaw-large: <b>two</b>
   * Macaw-answer-11B: <b>usually 8</b> (credit: 0)
   * GPT3-davinci: <b>Four.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Four, unless it's a snake with two heads.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>eight</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>four</b>
   * T5-XL-SSM-NQ: <b>five</b>
   * T5-large-SSM-NQ: <b>four</b>
   * T5-small-SSM-NQ: <b>ten</b>

Q241: <b>Is oxygen transparent?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>No.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Oxygen is transparent to visible light, but absorbs ultraviolet and infrared radiation.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>colorless</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>almost clear</b>
   * T5-XL-SSM-NQ: <b>colorless</b>
   * T5-large-SSM-NQ: <b>Ozone transparent</b>
   * T5-small-SSM-NQ: <b>transparency</b>

Q242: <b>Does oxygen reflect blue light?</b>
   * Macaw-11B: <b>yes</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 0)
   * GPT3-davinci: <b>Yes, oxygen reflects blue light.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Yes, oxygen does reflect blue light.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>blue light</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>yellow-orange</b>
   * T5-XL-SSM-NQ: <b>blue light</b>
   * T5-large-SSM-NQ: <b>Alkali metals</b>
   * T5-small-SSM-NQ: <b>photosynthetic organisms</b>

Q243: <b>Does oxygen contain a lot of hydrogen?</b>
   * Macaw-11B: <b>no</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>Yes, oxygen contains a lot of hydrogen.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>No. Oxygen contains 8 protons, 8 neutrons, and 8 electrons. Hydrogen contains 1 proton, 1 neutron, and 1 electron.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>atoms</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Yes</b>
   * T5-XL-SSM-NQ: <b>contains about 7% hydrogen</b>
   * T5-large-SSM-NQ: <b>very low</b>
   * T5-small-SSM-NQ: <b>most stable</b>

Q244: <b>You blow up a toy balloon, and tie the end shut. What is the air pressure in the balloon, relative to outside?</b>
   * Macaw-11B: <b>equal to the air pressure outside the balloon</b> (credit: 0)
   * Macaw-3B: <b>equal to atmospheric pressure</b>
   * Macaw-large: <b>equal to the atmospheric pressure</b>
   * Macaw-answer-11B: <b>equal to the atmospheric pressure</b> (credit: 1)
   * GPT3-davinci: <b>The air pressure inside the balloon is the same as outside.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The air pressure in the balloon is 1/2 of the air pressure outside.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>hypothetical pressure</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>negative pressure</b>
   * T5-XL-SSM-NQ: <b>100 kPa, 1 bar</b>
   * T5-large-SSM-NQ: <b>Toy balloon pressure</b>
   * T5-small-SSM-NQ: <b>approximately 13 wpm</b>

## Spatial

Q245: <b>Where is the roof relative to the walls and floors in a house?</b>
   * Macaw-11B: <b>on top</b> (credit: 1)
   * Macaw-3B: <b>above the walls</b>
   * Macaw-large: <b>at the top</b>
   * Macaw-answer-11B: <b>on top</b> (credit: 1)
   * GPT3-davinci: <b>The roof is the top of the walls and floors.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The roof is above everything else.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>highest point</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>above</b>
   * T5-XL-SSM-NQ: <b>first</b>
   * T5-large-SSM-NQ: <b>over the porch</b>
   * T5-small-SSM-NQ: <b>the floor scale</b>

Q246: <b>Where are the walls relative to the roof and floors in a house?</b>
   * Macaw-11B: <b>on the outside</b> (credit: 1)
   * Macaw-3B: <b>walls are above the roof</b>
   * Macaw-large: <b>in the middle</b>
   * Macaw-answer-11B: <b>vertical</b> (credit: 0)
   * GPT3-davinci: <b>The walls are on the outside of the roof and floors.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The walls are always below the roof and floors.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>supporting a roof</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>parallel to the floor</b>
   * T5-XL-SSM-NQ: <b>between a foundation and a roof</b>
   * T5-large-SSM-NQ: <b>from the outside</b>
   * T5-small-SSM-NQ: <b>the floor scale</b>

Q247: <b>Where is the floor relative to the roof and walls in a house?</b>
   * Macaw-11B: <b>the floor is on the inside of the walls</b> (credit: 1)
   * Macaw-3B: <b>below the roof</b>
   * Macaw-large: <b>in the middle</b>
   * Macaw-answer-11B: <b>the middle</b> (credit: 1)
   * GPT3-davinci: <b>The floor is the bottom surface of the house.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The floor is the lowest horizontal surface in a house.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>between walls</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>below the ceiling</b>
   * T5-XL-SSM-NQ: <b>first</b>
   * T5-large-SSM-NQ: <b>from the floor to the wall</b>
   * T5-small-SSM-NQ: <b>between the walls and walls</b>

Q248: <b>Why was it easier for Aristotle to travel to Egypt than Eastern Asia?</b>
   * Macaw-11B: <b>it was closer</b> (credit: 1)
   * Macaw-3B: <b>it was closer to the equator</b>
   * Macaw-large: <b>it was much easier to get the visa for Egypt than for the rest of the world</b>
   * Macaw-answer-11B: <b>shorter distance</b> (credit: 1)
   * GPT3-davinci: <b>Because the Greeks had already invented the wheel.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because Aristotle was Greek.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>much further</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>logistically easier</b>
   * T5-XL-SSM-NQ: <b>easier</b>
   * T5-large-SSM-NQ: <b>easier</b>
   * T5-small-SSM-NQ: <b>ben Adam</b>

Q249: <b>How can I reach a high window in my kitchen?</b>
   * Macaw-11B: <b>step stool</b> (credit: 1)
   * Macaw-3B: <b>step ladder</b>
   * Macaw-large: <b>use a ladder</b>
   * Macaw-answer-11B: <b>step stool</b> (credit: 1)
   * GPT3-davinci: <b>You can use a step stool or a chair to reach the window.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>A ladder or stool is the safest way to reach a high window.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a stepladder</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>a step ladder</b>
   * T5-XL-SSM-NQ: <b>a ladder</b>
   * T5-large-SSM-NQ: <b>high window sill</b>
   * T5-small-SSM-NQ: <b>to be an extension</b>

Q250: <b>You want to mail a beautiful eight-inch diameter circular piece of fabric to your mother. The only box you have is five-by-five-by-two inches. You will have to do what?</b>
   * Macaw-11B: <b>fold the fabric in half</b> (credit: 1)
   * Macaw-3B: <b>fold the fabric in half</b>
   * Macaw-large: <b>fold the fabric in half</b>
   * Macaw-answer-11B: <b>fold the fabric in half</b> (credit: 1)
   * GPT3-davinci: <b>Fold the fabric into a square.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Fold it.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>fold the fabric</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>fold it in half</b>
   * T5-XL-SSM-NQ: <b>fold it</b>
   * T5-large-SSM-NQ: <b>fold it</b>
   * T5-small-SSM-NQ: <b>A stuffed cotton</b>

Q251: <b>The year is 2075. Violet Blair is an astronaut on the Moon, in the Sea of Tranquility. Right now, on Earth, there is a solar eclipse. Violet looks in the direction of the Earth and sees what?</b>
   * Macaw-11B: <b>the shadow of the earth</b> (credit: 0)
   * Macaw-3B: <b>the sun</b>
   * Macaw-large: <b>the moon</b>
   * Macaw-answer-11B: <b>blackness</b> (credit: 0)
   * GPT3-davinci: <b>A total solar eclipse.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>A solar eclipse. Violet Blair is an astronaut on the Moon, in the Sea of Tranquility. Right now, on Earth, there is a solar eclipse. Violet looks in the direction of the Earth and sees what?</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>a blue tint</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Earth</b>
   * T5-XL-SSM-NQ: <b>a large shadow</b>
   * T5-large-SSM-NQ: <b>sunlight</b>
   * T5-small-SSM-NQ: <b>"Worth"</b>

Q252: <b>John is left of Sue. Where is Sue relative to John?</b>
   * Macaw-11B: <b>to his right</b> (credit: 1)
   * Macaw-3B: <b>to the right</b>
   * Macaw-large: <b>middle</b>
   * Macaw-answer-11B: <b>to John's left</b> (credit: 0)
   * GPT3-davinci: <b>Sue is right of John.

The following is a list of the most common relative clauses in English.

Relative clauses can be used to modify nouns, pronouns, and noun phrases.

Relative clauses can be used to modify adjectives, adverbs, and prepositional phrases.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Sue is to the right of John.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>left of John</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>left</b>
   * T5-XL-SSM-NQ: <b>farthest from John</b>
   * T5-large-SSM-NQ: <b>old friend</b>
   * T5-small-SSM-NQ: <b>a friend</b>

Q253: <b>John is left of Sue. Sue is left of Mike. Where is Mike relative to John?</b>
   * Macaw-11B: <b>to the right</b> (credit: 1)
   * Macaw-3B: <b>right</b>
   * Macaw-large: <b>right side</b>
   * Macaw-answer-11B: <b>to the right</b> (credit: 1)
   * GPT3-davinci: <b>Mike is to the right of John.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Mike is to the right of John.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>right of Sue</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>to the left of John</b>
   * T5-XL-SSM-NQ: <b>John's right</b>
   * T5-large-SSM-NQ: <b>Susan</b>
   * T5-small-SSM-NQ: <b>from an unnamed seafarer</b>

Q254: <b>John is left of Sue. Sue is left of Mike. Where is Sue relative to John?</b>
   * Macaw-11B: <b>to his left</b> (credit: 0)
   * Macaw-3B: <b>to the right</b>
   * Macaw-large: <b>John is left of Sue. Mike is right of Sue.</b>
   * Macaw-answer-11B: <b>to John's left</b> (credit: 0)
   * GPT3-davinci: <b>Mike</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Sue is to the right of John.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>left of John</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>left</b>
   * T5-XL-SSM-NQ: <b>Mike</b>
   * T5-large-SSM-NQ: <b>Mike</b>
   * T5-small-SSM-NQ: <b>from an unnamed seafarer</b>

Q255: <b>If you brought a canary and an alligator together to the same place, could the canary could see what is inside the alligator's stomach?</b>
   * Macaw-11B: <b>no, because the canary is colorblind</b> (credit: 0)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>the canary could see through the alligator's belly</b>
   * Macaw-answer-11B: <b>no</b> (credit: 0)
   * GPT3-davinci: <b>No, because the canary would be inside the alligator's stomach.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, the canary would be eaten by the alligator.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Neither can see the other</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>canary's vision</b>
   * T5-XL-SSM-NQ: <b>canary</b>
   * T5-large-SSM-NQ: <b>canary</b>
   * T5-small-SSM-NQ: <b>a dog</b>

## Steps

Q256: <b>What are the steps involved in replacing a light bulb?</b>
   * Macaw-11B: <b>remove the old bulb, put in the new bulb</b> (credit: 1)
   * Macaw-3B: <b>remove old bulb</b>
   * Macaw-large: <b>switch to a new bulb</b>
   * Macaw-answer-11B: <b>remove the old bulb, insert the new bulb, and screw in the new bulb</b> (credit: 1)
   * GPT3-davinci: <b>1. Make sure it's dark. 2. Reach up high. 3. Turn the bulb. 4. Turn the bulb again. 5. Turn the bulb again. 6. Turn the bulb again. 7. Turn the bulb again. 8. Turn the bulb again. 9. Turn the bulb again. 10.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>First, turn off the power. Then, remove the old bulb. Next, install the new bulb. Finally, turn the power back on.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>unscrewing the light bulb</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>Turn off the power</b>
   * T5-XL-SSM-NQ: <b>Shake the bulb</b>
   * T5-large-SSM-NQ: <b>"Repair"</b>
   * T5-small-SSM-NQ: <b>Alliteration</b>

Q257: <b>How do I make a loaf of bread?</b>
   * Macaw-11B: <b>mix flour, yeast, and water together in a bowl</b> (credit: 1)
   * Macaw-3B: <b>using yeast</b>
   * Macaw-large: <b>a loaf of bread mix</b>
   * Macaw-answer-11B: <b>mix flour, yeast, salt, water, and oil together</b> (credit: 1)
   * GPT3-davinci: <b>You need flour, water, yeast, and salt.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Bread making is easy and fun.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>Follow these steps</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>recipe</b>
   * T5-XL-SSM-NQ: <b>I've never made bread</b>
   * T5-large-SSM-NQ: <b>Baking a loaf</b>
   * T5-small-SSM-NQ: <b>to boil or steam rice</b>

Q258: <b>What are the steps involved in making a loaf of bread?</b>
   * Macaw-11B: <b>mix flour, yeast, water, and salt together</b> (credit: 1)
   * Macaw-3B: <b>rising, rising, rising</b>
   * Macaw-large: <b>rising, cooling, baking</b>
   * Macaw-answer-11B: <b>mix flour, yeast, salt, water, and oil in a bowl, knead dough, shape into a loaf, and bake</b> (credit: 1)
   * GPT3-davinci: <b>Mixing, kneading, rising, shaping, proofing, baking.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>First, the baker mixes flour, water, yeast, and salt. Then, he kneads the dough. Next, he lets the dough rise. Finally, he bakes the bread.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>kneading</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>Kneading</b>
   * T5-XL-SSM-NQ: <b>Rising</b>
   * T5-large-SSM-NQ: <b>Four steps</b>
   * T5-small-SSM-NQ: <b>breadmaking</b>

Q259: <b>What are the four steps in making bread?</b>
   * Macaw-11B: <b>mix, knead, shape, bake</b> (credit: 1)
   * Macaw-3B: <b>mix, rise, bake</b>
   * Macaw-large: <b>rise, bake, cool</b>
   * Macaw-answer-11B: <b>measure, mix, knead, let rise</b> (credit: 1)
   * GPT3-davinci: <b>Mix, Knead, Rise, Bake</b> (credit: 1)
   * Jurassic-1-jumbo: <b>1. Mixing, 2. Kneading, 3. Rising, 4. Baking.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>hydrate the flour</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Kneading</b>
   * T5-XL-SSM-NQ: <b>proofing</b>
   * T5-large-SSM-NQ: <b>Baking</b>
   * T5-small-SSM-NQ: <b>to cross stanzas</b>

Q260: <b>What are the steps involved in counting cars that pass a school each day?</b>
   * Macaw-11B: <b>count the number of cars that pass the school each day</b> (credit: 0)
   * Macaw-3B: <b>count number of cars that pass school</b>
   * Macaw-large: <b>observation</b>
   * Macaw-answer-11B: <b>record the number of cars</b> (credit: 1)
   * GPT3-davinci: <b>The steps are:
1. The count is done by a trained volunteer.
2. The volunteer counts the number of cars that pass the school on a single day.
3. The count is done at the same time each day.
4. The count is done on a day when there is no school</b> (credit: 1)
   * Jurassic-1-jumbo: <b>First, count the number of cars that pass the school each day. Then, divide that number by the number of days you counted. Finally, multiply that number by 365.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>traffic counting</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>travel time</b>
   * T5-XL-SSM-NQ: <b>traffic monitoring</b>
   * T5-large-SSM-NQ: <b>Traffic calming</b>
   * T5-small-SSM-NQ: <b>to be nocturnal</b>

Q261: <b>If you want to drive a car, what do you do first?</b>
   * Macaw-11B: <b>learn to drive a stick shift</b> (credit: 0)
   * Macaw-3B: <b>get a license</b>
   * Macaw-large: <b>learn the basics of driving</b>
   * Macaw-answer-11B: <b>get a license</b> (credit: 1)
   * GPT3-davinci: <b>You get a license.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You turn the key in the ignition.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>get a license</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>take a driving lesson</b>
   * T5-XL-SSM-NQ: <b>learn to drive</b>
   * T5-large-SSM-NQ: <b>driving</b>
   * T5-small-SSM-NQ: <b>a car</b>

Q262: <b>In an internal combustion engine, what happens after the air is compressed in the cylinder?</b>
   * Macaw-11B: <b>it is heated</b> (credit: 1)
   * Macaw-3B: <b>it is burned</b>
   * Macaw-large: <b>the gas is released</b>
   * Macaw-answer-11B: <b>it is ignited</b> (credit: 1)
   * GPT3-davinci: <b>The air is ignited by the spark plug, which ignites the fuel.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The compressed air is ignited by a spark.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>ignited</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>ignited</b>
   * T5-XL-SSM-NQ: <b>fire</b>
   * T5-large-SSM-NQ: <b>the engine revs</b>
   * T5-small-SSM-NQ: <b>decreasing the volume</b>

Q263: <b>In an internal combustion engine, what happens after the air is heated?</b>
   * Macaw-11B: <b>it is combusted</b> (credit: 1)
   * Macaw-3B: <b>it is mixed with fuel</b>
   * Macaw-large: <b>the gas is heated</b>
   * Macaw-answer-11B: <b>it is combusted</b> (credit: 1)
   * GPT3-davinci: <b>The air is mixed with fuel and ignited.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>The heated air expands and pushes the piston down.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>compressibility</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>combustion</b>
   * T5-XL-SSM-NQ: <b>to fire</b>
   * T5-large-SSM-NQ: <b>exhaust</b>
   * T5-small-SSM-NQ: <b>heat</b>

Q264: <b>Some kids are planning a rollerskating race. What happens next?</b>
   * Macaw-11B: <b>they practice</b> (credit: 1)
   * Macaw-3B: <b>they practice</b>
   * Macaw-large: <b>they fall off the skates</b>
   * Macaw-answer-11B: <b>they fall down</b> (credit: 0)
   * GPT3-davinci: <b>They all fall down.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>They start rolling! They roll and race, roll and race, roll and race.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>disaster</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>They're off!</b>
   * T5-XL-SSM-NQ: <b>The kids are separated</b>
   * T5-large-SSM-NQ: <b>School's Out</b>
   * T5-small-SSM-NQ: <b>20-a-Ride</b>

Q265: <b>Some kids are planning a rollerskating race. They practice. What happens next?</b>
   * Macaw-11B: <b>they fall</b> (credit: 1)
   * Macaw-3B: <b>they get faster</b>
   * Macaw-large: <b>they get tired</b>
   * Macaw-answer-11B: <b>they fall</b> (credit: 1)
   * GPT3-davinci: <b>They race.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>They race.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>disaster</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>The big race</b>
   * T5-XL-SSM-NQ: <b>The kids are separated</b>
   * T5-large-SSM-NQ: <b>the race</b>
   * T5-small-SSM-NQ: <b>20\[Dash]25 years</b>

Q266: <b>List all the steps in planning a vacation.</b>
   * Macaw-11B: <b>research, make a list, make a budget, research some more, book the trip</b> (credit: 1)
   * Macaw-3B: <b>research, booking, packing</b>
   * Macaw-large: <b>travel, attractions, hotels</b>
   * Macaw-answer-11B: <b>research, budget, book, pack</b> (credit: 1)
   * GPT3-davinci: <b>1. Make a list of all the things you want to do on your vacation.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>1. Decide where to go.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>research</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>Research</b>
   * T5-XL-SSM-NQ: <b>Research</b>
   * T5-large-SSM-NQ: <b>Read the FAQ</b>
   * T5-small-SSM-NQ: <b>plan-assisted plan</b>

Q267: <b>List all the steps in going to the zoo.</b>
   * Macaw-11B: <b>get in car, drive to zoo, park, walk around the zoo</b> (credit: 1)
   * Macaw-3B: <b>plan, get there, enjoy</b>
   * Macaw-large: <b>the zoo is open to the public</b>
   * Macaw-answer-11B: <b>get in car, drive to zoo, look at animals, get out of car, pay admission</b> (credit: 0.5)
   * GPT3-davinci: <b>1. Go to the zoo.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>First, you get dressed. Second, you pack your lunch. Third, you brush your teeth. Fourth, you put on your shoes. Fifth, you grab your coat. Sixth, you grab your backpack. Seventh, you grab your hat. Eighth, you grab your mittens. Ninth, you grab your scarf. Tenth, you grab your gloves. Eleventh, you grab your backpack</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>Plan the trip</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>park</b>
   * T5-XL-SSM-NQ: <b>Going to the zoo</b>
   * T5-large-SSM-NQ: <b>Plan a trip</b>
   * T5-small-SSM-NQ: <b>to be released in 1972</b>

Q268: <b>List all the steps in making a cake.</b>
   * Macaw-11B: <b>measure, mix, pour, cover, cool</b> (credit: 1)
   * Macaw-3B: <b>baking, cooling, frosting</b>
   * Macaw-large: <b>making the cake</b>
   * Macaw-answer-11B: <b>measure, mix, pour, cool</b> (credit: 1)
   * GPT3-davinci: <b>1. Bake a cake. 2. Eat the cake.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>1. Get all the ingredients.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>Cream the butter</b> (credit: 0.2)
   * T5-11B-SSM-NQ: <b>measure dry ingredients</b>
   * T5-XL-SSM-NQ: <b>pâté</b>
   * T5-large-SSM-NQ: <b>Baking</b>
   * T5-small-SSM-NQ: <b>A panda</b>

Q269: <b>List all the steps in repairing a flat tire.</b>
   * Macaw-11B: <b>check air pressure, change flat tire, inflate tire</b> (credit: 1)
   * Macaw-3B: <b>changing air in the tire</b>
   * Macaw-large: <b>change the oil</b>
   * Macaw-answer-11B: <b>check for leaks, inflate tire, replace valve stem, and re-balance wheel</b> (credit: 0)
   * GPT3-davinci: <b>1. Buy a new tire. 2. Put it on the car. 3. Drive on it.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>1. Stop the car. 2. Put on the emergency brake. 3. Turn on the hazard lights. 4. Get out of the car. 5. Remove the hubcap. 6. Loosen the lug nuts. 7. Remove the flat tire. 8. Put on the spare tire. 9. Tighten the lug</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>remove the wheel</b> (credit: 0.2)
   * T5-11B-SSM-NQ: <b>Check the air pressure</b>
   * T5-XL-SSM-NQ: <b>removing the valve stem</b>
   * T5-large-SSM-NQ: <b>Check the alignment</b>
   * T5-small-SSM-NQ: <b>Reduction of car parts</b>

Q270: <b>List all the steps in planning a wedding.</b>
   * Macaw-11B: <b>make a guest list, choose a date, make a budget, invite people</b> (credit: 1)
   * Macaw-3B: <b>from invitations to reception</b>
   * Macaw-large: <b>make a list of all the steps in planning a wedding</b>
   * Macaw-answer-11B: <b>choose a date, find a venue, invite guests, plan the menu, and choose a wedding dress</b> (credit: 1)
   * GPT3-davinci: <b>The first step is to get engaged. The second step is to plan the wedding. The third step is to get married. The fourth step is to have a baby. The fifth step is to have another baby. The sixth step is to have another baby. The seventh step is to have another baby. The eighth step</b> (credit: 0)
   * Jurassic-1-jumbo: <b>1. Set the date. 2. Set the budget. 3. Set your priorities. 4. Set your guest list. 5. Set your theme. 6. Set your colors. 7. Set your dress. 8. Set your flowers. 9. Set your cake. 10.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>set a budget</b> (credit: 0.2)
   * T5-11B-SSM-NQ: <b>Venue selection</b>
   * T5-XL-SSM-NQ: <b>invitations</b>
   * T5-large-SSM-NQ: <b>wedding ceremony</b>
   * T5-small-SSM-NQ: <b>A wedding plan</b>

## Story understanding

Q271: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. Why did I call a taxi?</b>
   * Macaw-11B: <b>to get me home</b> (credit: 1)
   * Macaw-3B: <b>to get to my hotel</b>
   * Macaw-large: <b>to get help</b>
   * Macaw-answer-11B: <b>I was too tired to drive</b> (credit: 1)
   * GPT3-davinci: <b>Because you were in a hospital.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because you were too injured to drive.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>I was too embarrassed to drive</b> (credit: 0.2)
   * T5-11B-SSM-NQ: <b>I couldn't drive</b>
   * T5-XL-SSM-NQ: <b>I was sleepwalking</b>
   * T5-large-SSM-NQ: <b>I had no idea what to do</b>
   * T5-small-SSM-NQ: <b>late 2003</b>

Q272: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. Why couldn't I drive home?</b>
   * Macaw-11B: <b>i was too tired</b> (credit: 1)
   * Macaw-3B: <b>I was too tired</b>
   * Macaw-large: <b>the car was too heavy</b>
   * Macaw-answer-11B: <b>i was too tired</b> (credit: 1)
   * GPT3-davinci: <b>You were probably still under the influence of the drugs they gave you at the hospital.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Driving a car is complex. It requires your full attention. Even if you're physically able, you may not be mentally or emotionally able to drive.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>because of the alcohol</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>I was too tired</b>
   * T5-XL-SSM-NQ: <b>"Dreams of Death"</b>
   * T5-large-SSM-NQ: <b>I had no idea</b>
   * T5-small-SSM-NQ: <b>18 months</b>

Q273: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. Why was I in hospital?</b>
   * Macaw-11B: <b>injuries</b> (credit: 1)
   * Macaw-3B: <b>to have my broken bones fixed</b>
   * Macaw-large: <b>I was injured in a car crash</b>
   * Macaw-answer-11B: <b>injuries</b> (credit: 1)
   * GPT3-davinci: <b>You were in hospital because you crashed your car.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You crashed your car because you were driving while tired.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>alcoholism</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>a concussion</b>
   * T5-XL-SSM-NQ: <b>for the accident</b>
   * T5-large-SSM-NQ: <b>I had a stroke</b>
   * T5-small-SSM-NQ: <b>18 months old</b>

Q274: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. How did I get my injuries?</b>
   * Macaw-11B: <b>from the crash</b> (credit: 1)
   * Macaw-3B: <b>car accident</b>
   * Macaw-large: <b>I was hit by a car</b>
   * Macaw-answer-11B: <b>from the crash</b> (credit: 1)
   * GPT3-davinci: <b>You were in a car accident.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The insurance company for the other driver will argue that your injuries were caused by the accident. They will argue that you were not hurt in the accident, but that you were injured when you fell out of bed.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>a car accident</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>car crash</b>
   * T5-XL-SSM-NQ: <b>I had no idea</b>
   * T5-large-SSM-NQ: <b>from a drug overdose</b>
   * T5-small-SSM-NQ: <b>18 May 1980</b>

Q275: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. What was a result of the crash?</b>
   * Macaw-11B: <b>i was too tired to drive</b> (credit: 1)
   * Macaw-3B: <b>I was tired</b>
   * Macaw-large: <b>I broke my neck</b>
   * Macaw-answer-11B: <b>I was exhausted</b> (credit: 1)
   * GPT3-davinci: <b>A taxi bill.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You learned the importance of calling a taxi.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>a broken leg</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>insomnia</b>
   * T5-XL-SSM-NQ: <b>Traumatic Brain Injury</b>
   * T5-large-SSM-NQ: <b>death</b>
   * T5-small-SSM-NQ: <b>died in a plane crash</b>

Q276: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. Was I hurt in the crash?</b>
   * Macaw-11B: <b>yes</b> (credit: 1)
   * Macaw-3B: <b>yes</b>
   * Macaw-large: <b>yes</b>
   * Macaw-answer-11B: <b>yes</b> (credit: 1)
   * GPT3-davinci: <b>Yes. You were hurt in the crash.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Yes. You were hurt in the crash.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>not seriously</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>hurt bad</b>
   * T5-XL-SSM-NQ: <b>Traumatic Brain Injury</b>
   * T5-large-SSM-NQ: <b>no one was hurt</b>
   * T5-small-SSM-NQ: <b>1979</b>

Q277: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. Why did I go to the hospital?</b>
   * Macaw-11B: <b>to get checked out</b> (credit: 1)
   * Macaw-3B: <b>to get checked out</b>
   * Macaw-large: <b>to get medical help</b>
   * Macaw-answer-11B: <b>to get checked out</b> (credit: 1)
   * GPT3-davinci: <b>Because you were in an accident.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You went to the emergency room because you had chest pain.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>I'd been drinking</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>because I was drunk</b>
   * T5-XL-SSM-NQ: <b>sleep</b>
   * T5-large-SSM-NQ: <b>to die</b>
   * T5-small-SSM-NQ: <b>...</b>

Q278: <b>I crashed my car. When I finally left the hospital, all I wanted to do was sleep. I had to call a taxi. When did I leave the hospital?</b>
   * Macaw-11B: <b>after midnight</b> (credit: 1)
   * Macaw-3B: <b>after a few hours</b>
   * Macaw-large: <b>after 2 hours</b>
   * Macaw-answer-11B: <b>after a week</b> (credit: 1)
   * GPT3-davinci: <b>You left the hospital at 8:00 p.m.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>You left the hospital when you called a taxi.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>June 25, 2015</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the morning of July 4</b>
   * T5-XL-SSM-NQ: <b>December 3, 1972</b>
   * T5-large-SSM-NQ: <b>November 7, 1984</b>
   * T5-small-SSM-NQ: <b>2004</b>

Q279: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. Why was Josh grounded?</b>
   * Macaw-11B: <b>his parrot said a bad word</b> (credit: 1)
   * Macaw-3B: <b>he made his teacher mad</b>
   * Macaw-large: <b>the parrot's owner told Josh not to bring his parrot to school</b>
   * Macaw-answer-11B: <b>his parrot said a bad word</b> (credit: 1)
   * GPT3-davinci: <b>Because his parrot didn't say "Hello, Mrs. Smith."</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because his parrot said a bad word.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>his parrot</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>his parents were busy</b>
   * T5-XL-SSM-NQ: <b>a verbal apprehension</b>
   * T5-large-SSM-NQ: <b>discipline</b>
   * T5-small-SSM-NQ: <b>"The Search"</b>

Q280: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. Why did the teacher tell Joshua not to bring his bird again?</b>
   * Macaw-11B: <b>the bird said something bad</b> (credit: 1)
   * Macaw-3B: <b>the bird might hurt someone</b>
   * Macaw-large: <b>because the parrot could not speak</b>
   * Macaw-answer-11B: <b>the parrot said a bad word</b> (credit: 1)
   * GPT3-davinci: <b>Because the parrot kept saying, "Josh is a dork!"</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Because the bird said a bad word.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>use of bad language</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>due to safety concerns</b>
   * T5-XL-SSM-NQ: <b>he's been mute</b>
   * T5-large-SSM-NQ: <b>discipline</b>
   * T5-small-SSM-NQ: <b>"Say Say Say"</b>

Q281: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. What bad word might the parrot have said?</b>
   * Macaw-11B: <b>swear</b> (credit: 1)
   * Macaw-3B: <b>swear</b>
   * Macaw-large: <b>no</b>
   * Macaw-answer-11B: <b>poop</b> (credit: 1)
   * GPT3-davinci: <b>"Birds of a feather flock together."</b> (credit: 0)
   * Jurassic-1-jumbo: <b>"I hate you, Josh!"</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>Fuck</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>Fuck</b>
   * T5-XL-SSM-NQ: <b>pissed off</b>
   * T5-large-SSM-NQ: <b>"unkindness"</b>
   * T5-small-SSM-NQ: <b>"Fatal Distraction"</b>

Q282: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. Why did Josh bring the parrot to school?</b>
   * Macaw-11B: <b>to show off</b> (credit: 1)
   * Macaw-3B: <b>to show his friends</b>
   * Macaw-large: <b>to play with it</b>
   * Macaw-answer-11B: <b>to show his friends</b> (credit: 1)
   * GPT3-davinci: <b>He wanted to show and tell the class a bad word.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because he wanted to show off.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>to show his classmates</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>to impress his friends</b>
   * T5-XL-SSM-NQ: <b>to embarrass the teacher</b>
   * T5-large-SSM-NQ: <b>not sure what to do</b>
   * T5-small-SSM-NQ: <b>"The Search"</b>

Q283: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. How did Josh feel?</b>
   * Macaw-11B: <b>sad</b> (credit: 1)
   * Macaw-3B: <b>sad</b>
   * Macaw-large: <b>sad</b>
   * Macaw-answer-11B: <b>sad</b> (credit: 1)
   * GPT3-davinci: <b>Josh felt like a parrot.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Josh felt sad. He missed his parrot.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>sad</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>upset</b>
   * T5-XL-SSM-NQ: <b>adios</b>
   * T5-large-SSM-NQ: <b>shocked</b>
   * T5-small-SSM-NQ: <b>"The Voyage of the Beagle</b>

Q284: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. What was Josh doing during show and tell?</b>
   * Macaw-11B: <b>showing off his parrot</b> (credit: 1)
   * Macaw-3B: <b>showing off his bird</b>
   * Macaw-large: <b>yelling at the parrot</b>
   * Macaw-answer-11B: <b>showing his parrot</b> (credit: 1)
   * GPT3-davinci: <b>Josh was showing off.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>He was showing his parrot.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>babbling</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>showing off his parrot</b>
   * T5-XL-SSM-NQ: <b>his parrot</b>
   * T5-large-SSM-NQ: <b>talking to his friends</b>
   * T5-small-SSM-NQ: <b>"Fatal Distraction"</b>

Q285: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. How did the teacher feel?</b>
   * Macaw-11B: <b>mad</b> (credit: 1)
   * Macaw-3B: <b>annoyed</b>
   * Macaw-large: <b>angry</b>
   * Macaw-answer-11B: <b>mad</b> (credit: 1)
   * GPT3-davinci: <b>The teacher felt a little par-rot-ted.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The teacher felt bad.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>annoyed</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>frustrated</b>
   * T5-XL-SSM-NQ: <b>a little bit naughty</b>
   * T5-large-SSM-NQ: <b>shocked</b>
   * T5-small-SSM-NQ: <b>"The Voyage of the Beagle</b>

Q286: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. How did Josh's parents feel?</b>
   * Macaw-11B: <b>mad</b> (credit: 1)
   * Macaw-3B: <b>sad</b>
   * Macaw-large: <b>angry</b>
   * Macaw-answer-11B: <b>mad</b> (credit: 1)
   * GPT3-davinci: <b>They were pissed.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>They felt bad. They felt bad because Josh's parrot said a bad word.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>outraged</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>disappointed</b>
   * T5-XL-SSM-NQ: <b>Stupid</b>
   * T5-large-SSM-NQ: <b>shocked</b>
   * T5-small-SSM-NQ: <b>"Scientific Method."</b>

Q287: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. Why did the parrot saying a bad word make the teacher mad?</b>
   * Macaw-11B: <b>it was a bad word</b> (credit: 0)
   * Macaw-3B: <b>it was disrespectful</b>
   * Macaw-large: <b>the parrot was threatening</b>
   * Macaw-answer-11B: <b>it was a bad word</b> (credit: 0)
   * GPT3-davinci: <b>Because the parrot was a foul-mouthed parrot.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Because the teacher was afraid of the parrot.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>hurtful word</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>might scare the other students</b>
   * T5-XL-SSM-NQ: <b>a prank</b>
   * T5-large-SSM-NQ: <b>bad luck</b>
   * T5-small-SSM-NQ: <b>"The Little Rascals</b>

Q288: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. Why did the parrot saying a bad word make Josh's parents mad?</b>
   * Macaw-11B: <b>it was a bad word</b> (credit: 0)
   * Macaw-3B: <b>it was a bad word</b>
   * Macaw-large: <b>the parrot could not understand what Josh was saying</b>
   * Macaw-answer-11B: <b>they thought he was being disrespectful</b> (credit: 0)
   * GPT3-davinci: <b>Because the parrot was a foul-mouth.</b> (credit: 0.5)
   * Jurassic-1-jumbo: <b>Because Josh's parents didn't want him to say bad words.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>hurt feelings</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>might have hurt his feelings</b>
   * T5-XL-SSM-NQ: <b>being obscene</b>
   * T5-large-SSM-NQ: <b>had a bad day</b>
   * T5-small-SSM-NQ: <b>"Fatal Distraction"</b>

Q289: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. What happens during show and tell?</b>
   * Macaw-11B: <b>kids show and tell things they have</b> (credit: 1)
   * Macaw-3B: <b>the parrot says a bad word</b>
   * Macaw-large: <b>the parrot gets in trouble</b>
   * Macaw-answer-11B: <b>kids show and tell things they have</b> (credit: 1)
   * GPT3-davinci: <b>Josh's parrot said a bad word.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Josh's parrot said a bad word.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>students bring in something interesting</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>students bring in their pets</b>
   * T5-XL-SSM-NQ: <b>usually ignored</b>
   * T5-large-SSM-NQ: <b>Josh</b>
   * T5-small-SSM-NQ: <b>"The Search"</b>

Q290: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. How did the teacher feel before show and tell?</b>
   * Macaw-11B: <b>happy</b> (credit: 1)
   * Macaw-3B: <b>annoyed</b>
   * Macaw-large: <b>nervous</b>
   * Macaw-answer-11B: <b>calm</b> (credit: 1)
   * GPT3-davinci: <b>She was excited.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The teacher was excited.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>excited</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>irritated</b>
   * T5-XL-SSM-NQ: <b>a little nervous</b>
   * T5-large-SSM-NQ: <b>nervous</b>
   * T5-small-SSM-NQ: <b>"The Voyage of the Beagle</b>

Q291: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. What did the other children in Josh's class think of the parrot?</b>
   * Macaw-11B: <b>they thought it was funny</b> (credit: 1)
   * Macaw-3B: <b>they thought it was cool</b>
   * Macaw-large: <b>they thought it was weird</b>
   * Macaw-answer-11B: <b>they thought it was funny</b> (credit: 1)
   * GPT3-davinci: <b>They thought it was a parrot.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>They thought it was cool.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>other children</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>Josh</b>
   * T5-XL-SSM-NQ: <b>hated it</b>
   * T5-large-SSM-NQ: <b>negative</b>
   * T5-small-SSM-NQ: <b>"Fatal Distraction"</b>

Q292: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. Did the other children in Josh's class mind that the parrot had said a bad word?</b>
   * Macaw-11B: <b>no, they didn't mind</b> (credit: 1)
   * Macaw-3B: <b>no</b>
   * Macaw-large: <b>they were happy that Josh told them</b>
   * Macaw-answer-11B: <b>no</b> (credit: 1)
   * GPT3-davinci: <b>No, they didn't mind. They were used to it.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>No, they didn't mind.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>did not care</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>none</b>
   * T5-XL-SSM-NQ: <b>did not</b>
   * T5-large-SSM-NQ: <b>did they</b>
   * T5-small-SSM-NQ: <b>"Frank's father"</b>

Q293: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. How did Josh's parents find out about the parrot saying a bad word?</b>
   * Macaw-11B: <b>they heard it on the news</b> (credit: 0)
   * Macaw-3B: <b>the teacher told them</b>
   * Macaw-large: <b>called the school</b>
   * Macaw-answer-11B: <b>they heard it on the news</b> (credit: 0)
   * GPT3-davinci: <b>The parrot told them.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The parrot told his parents.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>called the police</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>the teacher</b>
   * T5-XL-SSM-NQ: <b>Josh</b>
   * T5-large-SSM-NQ: <b>accidentally being artificially inseminated</b>
   * T5-small-SSM-NQ: <b>"Fatal Distraction"</b>

Q294: <b>Josh had a parrot that talked. He brought his parrot to school. During show and tell, Josh's parrot said a bad word. The teacher told Joshua not to bring his bird again. When Josh got home, he was grounded. Who grounded Josh?</b>
   * Macaw-11B: <b>his mother</b> (credit: 1)
   * Macaw-3B: <b>his mother</b>
   * Macaw-large: <b>the school</b>
   * Macaw-answer-11B: <b>his parents</b> (credit: 1)
   * GPT3-davinci: <b>His parrot.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>His mom.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>his father</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>his father</b>
   * T5-XL-SSM-NQ: <b>his parents</b>
   * T5-large-SSM-NQ: <b>the teacher</b>
   * T5-small-SSM-NQ: <b>"The Little Rascals</b>

Q295: <b>Karen was assigned a roommate her first year of college. Her roommate asked her to go to a nearby city for a concert. Karen agreed happily.  The show was absolutely exhilarating. What happened that might cause Karen to become good friends with her roommate?</b>
   * Macaw-11B: <b>they had a good time together</b> (credit: 1)
   * Macaw-3B: <b>they had a great time</b>
   * Macaw-large: <b>she made new friends</b>
   * Macaw-answer-11B: <b>they had a good time together</b> (credit: 1)
   * GPT3-davinci: <b>Karen and her roommate were both arrested for smoking marijuana in the parking lot.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>Karen's roommate asked her to go to a nearby city for a concert. Karen agreed happily.  The show was absolutely exhilarating.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>falling in love</b> (credit: 1)
   * T5-11B-SSM-NQ: <b>Karen's parents were divorced</b>
   * T5-XL-SSM-NQ: <b>Karen Cartwright</b>
   * T5-large-SSM-NQ: <b>her father died</b>
   * T5-small-SSM-NQ: <b>"Future Distraction"</b>

## Temporal

Q296: <b>Why were Neanderthals unable to own Aristotle's books?</b>
   * Macaw-11B: <b>they didn't have writing</b> (credit: 0)
   * Macaw-3B: <b>they were too small</b>
   * Macaw-large: <b>they were unable to read</b>
   * Macaw-answer-11B: <b>they didn't have writing</b> (credit: 0)
   * GPT3-davinci: <b>Because they couldn't read.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>Because they were Neanderthals.</b> (credit: 0)
   * T5-XXL-SSM-NQ: <b>unable to write</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>The Library of Alexandria</b>
   * T5-XL-SSM-NQ: <b>lacking the ability to read</b>
   * T5-large-SSM-NQ: <b>copyright reasons</b>
   * T5-small-SSM-NQ: <b>to represent the Jews</b>

Q297: <b>Moshe posted on Facebook a photograph showing Maurice Ravel, Francois Poulenc, Frederic Mompou, and Erik Satie. Satie died in 1925. Poulenc was born in 1899. So the photograph must  have been taken when?</b>
   * Macaw-11B: <b>before 1925</b> (credit: 0.5)
   * Macaw-3B: <b>before 1925</b>
   * Macaw-large: <b>1899</b>
   * Macaw-answer-11B: <b>before 1925</b> (credit: 0.5)
   * GPT3-davinci: <b>The photograph was taken in the year 1875.</b> (credit: 0)
   * Jurassic-1-jumbo: <b>The photograph was taken in 1925.</b> (credit: 0.5)
   * T5-XXL-SSM-NQ: <b>1924</b> (credit: 0.5)
   * T5-11B-SSM-NQ: <b>1924</b>
   * T5-XL-SSM-NQ: <b>1926</b>
   * T5-large-SSM-NQ: <b>1924</b>
   * T5-small-SSM-NQ: <b>1904</b>

## Winograd

Q298: <b>The trophy couldn't fit into the box because it was too big. What was too big?</b>
   * Macaw-11B: <b>the trophy</b> (credit: 1)
   * Macaw-3B: <b>the trophy</b>
   * Macaw-large: <b>the trophy</b>
   * Macaw-answer-11B: <b>the trophy</b> (credit: 1)
   * GPT3-davinci: <b>The trophy.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The trophy.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>the XL5</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>24 inches</b>
   * T5-XL-SSM-NQ: <b>the Heisman Trophy</b>
   * T5-large-SSM-NQ: <b>football</b>
   * T5-small-SSM-NQ: <b>, a Wilson volleyball</b>

Q299: <b>The elephant couldn't fit into the box because it was too big. What was too big?</b>
   * Macaw-11B: <b>the box</b> (credit: 0)
   * Macaw-3B: <b>the elephant</b>
   * Macaw-large: <b>the elephant's body</b>
   * Macaw-answer-11B: <b>the elephant</b> (credit: 1)
   * GPT3-davinci: <b>The elephant.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The elephant.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>its trunk</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>too heavy</b>
   * T5-XL-SSM-NQ: <b>an elephant</b>
   * T5-large-SSM-NQ: <b>how to cope</b>
   * T5-small-SSM-NQ: <b>, a Spartan</b>

Q300: <b>A man is watching television. The elephant couldn't fit in the box because it was too big. What was too big?</b>
   * Macaw-11B: <b>the elephant</b> (credit: 1)
   * Macaw-3B: <b>elephant</b>
   * Macaw-large: <b>the elephant's trunk</b>
   * Macaw-answer-11B: <b>the elephant</b> (credit: 1)
   * GPT3-davinci: <b>The elephant.</b> (credit: 1)
   * Jurassic-1-jumbo: <b>The elephant.</b> (credit: 1)
   * T5-XXL-SSM-NQ: <b>its trunk</b> (credit: 0)
   * T5-11B-SSM-NQ: <b>too heavy</b>
   * T5-XL-SSM-NQ: <b>an elephant</b>
   * T5-large-SSM-NQ: <b>television</b>
   * T5-small-SSM-NQ: <b>television film director James Cameron</b>
