from libs.question_funcs import choose_question,result
from slackbot.bot import respond_to
from slackbot.bot import listen_to
question=""
answer=""
#メンションに対する応答
@respond_to("ハロー")
def greeting_1(message):
    # Slackに応答を返す
    message.reply("あら、こんにちは")
 
#メンションなしの応答
@listen_to("わーーーー")
def greeting_2(message):
    message.reply("うるさいわね……")

@respond_to("辛い")
def greeting_3(message):
    message.reply("ココア入れてあげるから、これ飲んで早く寝なさいな")

@respond_to("問題出して")
def question(message):
    message.reply("ちょっとまって")
    data=choose_question()
    message.reply("問題！"+data[0])
    question=data[0]
    answer=data[1]
    
@respond_to(".+")
def result_ans(message):
    if result(answer,message.body["text"]):
        message.reply("正解！")
    else:
        message.reply("残念")
    question=""
    answer=""


