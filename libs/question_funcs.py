import json
import random

def choose_question():
    return random.choice(list(question_data.items()))

def result(question_data,users_ans):
    if question_data[1]==users_ans:
        return "正解"
    else:
        return "残念"

question_data = json.load(open("data/question.json","r",encoding="utf-8"))

