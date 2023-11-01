import openai
import time
import json
import re
openai.api_base = 'https://api.closeai-proxy.xyz/v1'
openai.api_base = 'https://api.openai-proxy.org/v1'
openai.api_key = 'sk-6N0Ow7FjBtZ7ziQBk2LYtXT4P7KmbJQKmSs0WavLdQCx7H2C'

def gpt_decoder(prompt, n=1):
    # s_time = time.time()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        n=n,
        temperature=0 if n == 1 else 0.7
    )
    # e_time = time.time()
    # print(f"time consume :{e_time - s_time}")
    return [response['choices'][i]['message']['content'] for i in range(len(response['choices']))]

def load_jsonl(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        datas = f.readlines()
    return [json.loads(line) for line in datas]

def load_json(fp):
    return json.load(open(f, 'r', encoding='utf-8'))

def extract_answer(dataset, text):
    if dataset == 'tempreason_l1':
        return extract_date(text)

MONTH_TO_NUM = {
    'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Sept' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12,
    'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11 ,'December' : 12 }
def is_date_equal(date1, date2):
    #Date format (Month, Year)
    def convert_date_to_list(date):
        if isinstance(date, list) and len(date) == 1:
            date = date[0]
        if isinstance(date, str):
            date = date.split(",")
            date = [d.strip() for d in date]
        date = [MONTH_TO_NUM[date[0].lower().capitalize()], int(date[1])]
        return date
    date1, date2 = convert_date_to_list(date1), convert_date_to_list(date2)
    if date1[0] != date2[0]:
        return False
    if date1[1] != date2[1]:
        return False
    return True


def extract_date(text):
    """Extract Date (Month, Year) format

    Args:
        text (str): e.g. xxx Jan, 2021 xxx

    Returns:
        date (str): Jan, 2021
    """
    pattern = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s*([0-9]{2,4})"
    text = text.strip()
    text = re.sub("\(|\)|:|\.|\|\n|\,", "", text)
    results = re.findall(pattern, text)
    if len(results) > 0:
        return results[-1]
    else:
        return None

def extract_multi_choice_multi_answer(text):
    """For multi-choice multi-answer questions. 
    Usually, we use EM and F1 as evaluation metrics for this type of questions.

    Args:
        text (str): A. xxx B. xxx

    Returns:
        answers (list): [A, B, C]
    """
    pattern = r"([A-Z]\.\s)"
    text = text.strip()
    answers = re.findall(pattern, answer)
    answers = list(set(answers)) # de-duplication
    answers = [a[0] for a in answers]
    answers = sorted(answers)
    return answers

def extract_nli(text):
    """Extract NLI label, Entailment, Contradiction and Neutral

    Args:
        text (str): e.g. Therefore, the answer is A. Entailment.

    Returns:
        str: 
    """
    text = text.strip()
    pattern = r"(Entailment|Contradiction|Neutral)"
    results = re.findall(pattern=pattern, string=text, flags=re.IGNORECASE)
    if len(results) > 0:
        return results[-1]
    else:
        return None

def extract_torque_trigger(text):
    """Extract Event trigger.
    We use this func to extract answers in TORQUE datasets.
    Args:
        text (str): e.g. joins, leaved, been

    Returns:
        list: 
    """
    text = text.strip()
    triggers = text.split(',')
    triggers_satisfy = []
    for trigger in triggers:
        trigger = trigger.strip()
        trigger = trigger.split()
        if len(trigger) == 1:
            triggers_satisfy.append(trigger[0])
    if len(triggers_satisfy) > 0:
        return triggers_satisfy
    else:
        return None

def calculate_f1_torque(gold, pred):
    """Calculate F1 regardless of order. This is for TORQUE dataset.

    Args:
        gold (gold): A list of golden answers, e.g. [A, B, C]
        pred (pred): A list of predictions, e.g. [C, D]

    Returns:
        tuple: (Precision, Recall, F1)
    """
    TP, FP, FN = 0, 0, 0
    for p in pred: #True positive
        if p in gold:
            TP += 1
    for p in pred: #False positive
        if p not in gold:
            FP += 1
    for g in gold: #False Negative
        if g not in pred:
            FN += 1
    P = TP / (TP + FP)
    R = TP / (TP + FN)
    if P + R == 0:
        F = 0
    else:
        F = 2 * P * R / (P + R)
    return P, R, F

def calculate_f1_multianswer(gold, pred):
    """Calculate F1 taking account into order. This is for multi-choice multi-answer dataset, e.g. mctaco, durationqa.

    Args:
        gold (gold): A list of golden answers ()
        pred (pred): A list of predictions ()

    Returns:
        tuple: (Precision, Recall, F1)
    """
    return calculate_f1_torque(gold, pred)