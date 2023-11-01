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


torque_prompt_100 = """You will be presented with a passage and a question about temporal ordering of event.
You have to answer the question based on the passage.
Only output the event trigger words. 
If there is no answer, output [unanswerable]
Passage: {}
Question: {}
Answer:"""






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
    prompt = timexnli_cs1_prompt_103
    print(f'prompt: {prompt}')
    datas = load_jsonl('./cs1_timebench.70.jsonl')
    results = run(prompt, 'results_70/cs1_results_103.jsonl', datas[:])
    print(results)