import json
demonstrations = [
    {"keywords":["27 days","summer","a month","July","moon","revolution"],"statement":"July is a month during the summer. A revolution of the moon is 27 days.","ids":["openbookqa::Additional\/crowdsourced-facts.txt::487","openbookqa::Additional\/crowdsourced-facts.txt::1250"],"keywords_pos":[1,0,0,0,1,1],"statements":["July is a month during the summer.","A revolution of the moon is 27 days."]},
    {"keywords":["1,440 minutes","a week","one day","7 days"],"statement":"There are 1,440 minutes in one day. There are 7 days in a week.","ids":["openbookqa::Additional\/crowdsourced-facts.txt::4689","openbookqa::Additional\/crowdsourced-facts.txt::4696"],"keywords_pos":[0,1,0,1],"statements":["There are 1,440 minutes in one day.","There are 7 days in a week."]},
    {"keywords":["December 1st","June","Summer Solstice","the day after November 30th"],"statement":"December 1st is the day after November 30th. Summer Solstice is in June.","ids":["openbookqa::Additional\/crowdsourced-facts.txt::285","openbookqa::Additional\/crowdsourced-facts.txt::781"],"keywords_pos":[0,1,1,0],"statements":["December 1st is the day after November 30th.","Summer Solstice is in June."]},
    {"keywords":["winter month","365 days","one year","January","twelve months"],"statement":"January is a winter month. Twelve months is one year, or 365 days.","ids":["openbookqa::Additional\/crowdsourced-facts.txt::480","openbookqa::Additional\/crowdsourced-facts.txt::4848"],"keywords_pos":[0,1,1,0,1],"statements":["January is a winter month.","Twelve months is one year, or 365 days."]},
    {"keywords":["April 22 every year","Argentina","Christmas","Earth Day","summer"],"statement":"Christmas happens in Argentina in summer. Earth Day happens on April 22 every year.","ids":["commonsenseqa::train::4717","creak::train::1911"],"keywords_pos":[1,0,0,1,0],"statements":["Christmas happens in Argentina in summer.","Earth Day happens on April 22 every year."]},
    {"keywords":["6 months","Christmas","summer","decade","many years"],"statement":"Summer is 6 months after Christmas. A decade is many years.","ids":["openbookqa::Additional\/crowdsourced-facts.txt::4371","openbookqa::Additional\/crowdsourced-facts.txt::1071"],"keywords_pos":[0,0,0,1,1],"statements":["Summer is 6 months after Christmas.","A decade is many years."]},
    {"keywords":["June","world","May","the month","part","a winter month","August"],"statement":"June is the month after May. August is a winter month for part of the world.","ids":["openbookqa::Additional\/crowdsourced-facts.txt::494","strategyqa::train::688"],"keywords_pos":[0,1,0,0,1,1,1],"statements":["June is the month after May.","August is a winter month for part of the world."]},
    {"keywords":["6 months","the 1920s","The Russian Civil War","Christmas","summer"],"statement":"Summer is 6 months after Christmas. The Russian Civil War ended in the 1920s.","ids":["openbookqa::Additional\/crowdsourced-facts.txt::4371","creak::train::3489"],"keywords_pos":[0,1,1,0,0],"statements":["Summer is 6 months after Christmas.","The Russian Civil War ended in the 1920s."]}

]

demonstrations_cot = None