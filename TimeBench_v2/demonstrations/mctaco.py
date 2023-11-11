demonstrations = [
    {"qid": 93, "context": "She ordered the tastiest kind of each vegetable and the prettiest kind of each flower.", "question": "How often does she order vegetables and flowers?", "options": ["once a second", "three days a week", "every 10 centuries", "once a week"], "labels": ["no", "yes", "no", "yes"], "type": "Frequency", "cot" : "According to commonsense knowledge, ordering vegetables and flowers typically happens on a regular basis, usually every few days. Therefore, the answer is B. three days a week, D. once a week."}, 

    {"qid": 18, "context": "Carl Laemmle, head of Universal Studios, gave Einstein a tour of his studio and introduced him to Chaplin.", "question": "Afterwards did Einstein and Chaplin know each other?", "options": ["no", "yes, they were introduced", "yes", "no, they forgot each other"], "labels": ["no", "yes", "yes", "no"], "type": "Event Ordering", "cot" : "Based on the context, it can be inferred that after Carl Laemmle introduced Einstein to Chaplin, Einstein and Chaplin know each other. Therefore, the answer is B. yes, they were introduced, C. yes."},

    {"qid": 243, "context": "Then they laid down on some towels and enjoyed the sun.", "question": "How long did they enjoy under the sun?", "options": ["they enjoyed being under the sun for 2 seconds", "for an hour", "they enjoyed being under the sun for 2 hours", "they enjoyed 2 years under the sun"], "labels": ["no", "yes", "yes", "no"], "type": "Event Duration", "cot" : "According to commonsense knowledge, enjoying the sunlight typically lasts for several hours. Therefore, the answer is B. for an hour, C. they enjoyed being under the sun for 2 hours."},
    
    {"qid": 490, "context": "Wallace, 38, called Gastonia home from the age of 8 until she graduated from Hunter Huss High School in 1983.", "question": "When did Wallace wake up for high school?", "options": ["at 6 am", "at 1 am", "7:00 AM", "at 6 pm"], "labels": ["yes", "no", "yes", "no"], "type": "Typical Time", "cot" : "According to commonsense knowledge, waking up for high school typically happens in the morning, usually between 6 AM and 8 AM. Therefore, the answer is A. at 6 am, C. 7:00 AM."}

]


demonstrations_cot = demonstrations