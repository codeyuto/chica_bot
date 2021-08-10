from libs.question_funcs import choose_question,result
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from libs.chica_do import choose_do
question=""
answer=""


def greeting_1(message):
    # Slackに応答を返す
    message.reply("あら、こんにちは")
 
#メンションなしの応答
@listen_to("わーーーー")
def greeting_2(message):
    message.reply("うるさいわね……")

def greeting_3(message):
    message.reply("ココア入れてあげるから、これ飲んで早く寝なさいな")

def chicas_question(message):
    global question
    global answer
    message.reply("ちょっとまって")
    data=choose_question()
    message.reply("問題！"+data[0])
    question=data[0]
    answer=data[1]
def chicas_now(message):
    now=choose_do()
    message.reply(now)
    
@respond_to(".+")
def choose_action(message):
    global question
    global answer
    functions = {
    ("辛い","死にたい"): greeting_3,
    ("ハロー","こんにちは"):greeting_1,
    ("問題出して"):chicas_question,
    ("今何してるの"):chicas_now}
    ms=message.body["text"]
    for words, function in functions.items():
        if ms in words:
            function(message)
            return
    if question!="":
        result_ans(message,answer,ms)
    else:
        message.reply("あら？")
        

def result_ans(message,ans,ms):
    if result(ans,ms):
        message.reply("正解！")
    else:
        message.reply("残念、正解は"+ans+"でした")
    global question
    question=""
    global answer
    answer=""

