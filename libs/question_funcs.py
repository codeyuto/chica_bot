import json
import random

def choose_question():
    return random.choice(list(question_data.items()))

question_data = json.load(open("data/question.json","r",encoding="utf-8"))
print("load success")

