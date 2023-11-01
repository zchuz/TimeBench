import sys
import json
import numpy as np
import random
import time
sys.path.append('../utils/')
from utils import gpt_decoder, load_json, load_jsonl
def write(fp, line):
    with open(fp, 'a', encoding='utf-8') as f:
        f.write(json.dumps(line) + '\n')

# 0.5 Normal prompt, without label desc.
timexnli_cs1_prompt_100 = """Read the following statements about time and determine if the hypothesis can be inferred from the premise.
Premise: {}
Hypothesis: {}
Options: 
A. Entailment
B. Contradiction
C. Neutral
Answer:
"""

# 0.44 Normal prompt, with label desc.
timexnli_cs1_prompt_101 = """Read the following statements about time and determine if the hypothesis can be inferred from the premise. 
Premise: {}
Hypothesis: {}
Choose one of the following options:
A. Entailment. The hypothesis can be inferred from the premise.
B. Contradiction. The hypothesis can not be inferred from the premise.
C. Neutral. Indeterminately, it cannot be determine based on the information.
Answer:
"""

# 0.0 amazing all wrong.Task specific prompt, with label desc.
timexnli_cs1_prompt_102 = """Read the following premise and hypothesis about time. You have to determine whether there is a contradiction between the premise and the hypothesis from a chronological point of view.
Premise: {}
Hypothesis: {}
Choose one of the following options:
A. Entailment. There is no contradiction between the premise and the hypothesis. The hypothesis can be inferred from the premise.
B. Contradiction. There is a contradiction between the premise and the hypothesis. The hypothesis can not be inferred from the premise.
C. Neutral. Indeterminately, it cannot be determine based on the information.
Answer:
"""

# 0.37 Task specific prompt, without label desc.
timexnli_cs1_prompt_103 = """Read the following premise and hypothesis about time. You have to determine whether there is a contradiction between the premise and the hypothesis from a chronological point of view.
Premise: {}
Hypothesis: {}
Choose one of the following options:
A. Entailment. 
B. Contradiction.
C. Neutral. 
Answer:
"""

# with zero-shot cot 
timexnli_cs1_prompt_110 = """Read the following statements about time and determine if the hypothesis can be inferred from the premise.
Premise: {}
Hypothesis: {}
Options: 
A. Entailment
B. Contradiction
C. Neutral
Let's think step by step.
"""

timexnli_cs2_prompt_100 = """Read the following statements about time and determine if the hypothesis can be inferred from the premise.
Premise: {}
Hypothesis: {}
Options: 
A. Entailment
B. Contradiction
Answer:
"""

timexnli_cs2_prompt_102 = """Read the following premise and hypothesis about time. You have to determine whether there is a contradiction between the premise and the hypothesis from an event duration point of view.
Premise: {}
Hypothesis: {}
Choose one of the following options:
A. Entailment. There is no contradiction between the premise and the hypothesis. The hypothesis can be inferred from the premise.
B. Contradiction. There is a contradiction between the premise and the hypothesis. The hypothesis can not be inferred from the premise.
Answer:
"""

timexnli_cs3_prompt_100 = timexnli_cs1_prompt_100
timexnli_cs3_prompt_101 = timexnli_cs1_prompt_101





def run(pattern, outfile, datas, max_retry=2):
    from tqdm import tqdm
    results = []
    retry = 0
    success = False
    e, s = 0, 0
    for data in tqdm(datas, desc=f'Api Calling...'):
        retry = 0
        success = False
        while retry < max_retry and not success:
            try:
                premise = data['Premise']
                hypothesis = data['Hypothesis']
                label = data['Label']
                prompt = pattern.format(premise, hypothesis)
                s = time.time()
                predict = gpt_decoder(prompt, n=1)
                e = time.time()
                tqdm.write(f'{e-s}s')
                results.append([label, predict])
                write(outfile, {'Premise':premise, 'Hypothesis' : hypothesis, 'a': label, 'p':predict[0]})
                time.sleep(2)
                success = True
            except:
                retry += 1
                print(f'Retry, sleep 5s {retry}/{max_retry}')
                time.sleep(5)
    return results

if __name__ == '__main__':
    prompt = timexnli_cs3_prompt_100
    print(f'prompt: {prompt}')
    datas = load_jsonl('./cs3_timebench.70.jsonl')
    results = run(prompt, 'results_70/cs3_results_100.jsonl', datas[:])
    print(results)