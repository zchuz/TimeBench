demonstrations_cs1_cot = [
    {"Premise": "On Wednesday, they got married.", "Hypothesis": "Before Friday, they got married.", "Label": "Entailment", "cot" : "Wednesday is before Friday. As a result, we can infer that if something happens on Wednesday, it definitely happens before Friday. Therefore, the answer is Entailment."},

    {"Premise": "We went to Disneyland on Monday.", "Hypothesis": "We went to Disneyland after Wednesday.", "Label": "Contradiction", "cot" : "Monday is before Wednesday. As a result, We can infer that if something happens on Monday, it definitely can not happen after Wednesday. Therefore, the answer is Contradiction."},

    {"Premise": "The failing company issued major layoffs after Tuesday.", "Hypothesis": "The failing company issued major layoffs after Thursday.", "Label": "Neutral", "cot" : "Tuesday is before Thursday. If something happened after Tuesday, we cannot be certain whether it occurred after Thursday. Therefore, the answer is Neutral."},
]
demonstrations_cs1 = demonstrations_cs1_cot

demonstrations_cs2_cot = [
    {"Premise": "Her internship at Google will last from June to October.", "Hypothesis": "Her internship at Google will last for less than 10 months.", "Label": "Entailment", "cot" : "From June to October is 4 months period. We can infer that 4 months are less than 10 months. Therefore, the answer is Entailment."},

    {"Premise": "The coding competition started at 12 PM and ended at 9 AM.", "Hypothesis": "The coding competition was held for 22 hours.", "Label": "Contradiction", "cot" : "From 12 PM to 9 AM is 9 hours period. This conflicts with the competition was held for 22 hours. Therefore, the answer is Contradiction."},

    {"Premise": "The meeting lasted from 6 PM to 1 PM.", "Hypothesis": "The meeting lasted for 19 hours.", "Label": "Entailment", "cot" : "From 6 PM to 1 PM spans a day, totaling 6 + 13 = 19 hours. This is consistent with that the meeting lasted for 19 hours. Therefore, the answer is Entailment."},

    {"Premise": "We attended outdoor concerts from 1936 to 1979.", "Hypothesis": "We attended outdoor concerts for 44 years.", "Label": "Contradiction", "cot" : "From 1936 to 1979 is 43 years. This conflicts with we attended outdoor concerts for 44 years. Therefore, the answer is Contradiction."}
]
demonstrations_cs2 = demonstrations_cs2_cot

demonstrations_cs3_cot = [
    {"Premise": "They will get married before 1 year.", "Hypothesis": "They will get married before 15 months.", "Label": "Entailment", "cot" : "1 year equals to 12 months. We can rephrase the premise: 'They will get married before 12 months.' According to that, we can infer that if something will happen before 12 months, it will definitely happen before 15 months. Therefore, the answer is Entailment."},

    {"Premise": "After 10 days, the price of this stock will peak.", "Hypothesis": "The price of this stock will peak before 261 hours.", "Label": "Neutral", "cot" : "10 days equal 240 hours. We can rephrase the premise: 'After 240 hours, the price of this stock will peak'. If something will happen after 240 hours, we cannot be certain whether it will happen before 261 hours. Therefore, the answer is Neutral."},

    {"Premise": "I will leave on a long vacation after 7 months.", "Hypothesis": "Before 184 days, I will leave on a long vacation.", "Label": "Contradiction", "cot" : "7 months equals 210 days approximately. We can rephrase the premise: 'I will leave on a long vacation after 210 days.' According to that, We can infer that if something happens after 210 days, it definitely can not happen Before 184 days. Therefore, the answer is Contradiction."}
]
demonstrations_cs3 = demonstrations_cs3_cot