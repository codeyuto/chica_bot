from libs.question_funcs import choose_question,result
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from libs.chica_do import choose_do
from libs.greeting_func import time_greeting,announce_time
from libs.tsurai_funcs import return_tsurai,write_tsurai
import random
question=""
answer=""

def greeting_1(message):
    # Slackに応答を返す
    greeting=time_greeting()
    message.reply(greeting)
    message.reply(announce_time())
 
#メンションなしの応答
@listen_to("わーーーー")
def greeting_2(message):
    message.reply("うるさいわね……")

def greeting_3(message):
    message.reply("ココア入れてあげるから、これ飲んで早く寝なさいな")
    write_tsurai()

def chicas_question(message):
    global question
    global answer
    data=choose_question()
    message.reply("問題！"+data[0])
    question=data[0]
    answer=data[1]

def chicas_now(message):
    now=choose_do()
    message.reply(now)

def tsurai_mater(message):
    message.reply("最近の辛いメーターはこんな感じ:")
    recent=return_tsurai()
    message.reply("3週間前:"+"*"*recent[0])
    message.reply("2週間前:"+"*"*recent[1])
    message.reply("1週間前:"+"*"*recent[2])
    message.reply("今週:"+"*"*recent[3])
    result=recent[4]
    if result==0:
        message.reply("3週間前が一番高いみたい。最近は安定してきた？")
    elif result==1:
        message.reply("2週間前が一番高いみたい。適度な休憩を忘れずにね。")
    elif result==2:
        message.reply("1週間前が一番高いみたい。まだまだ注意が必要ね。")
    elif result==3:
        message.reply("ここ最近が一番高いみたい。一度ゆっくりしてみてはどう？")
    else:
        message.reply("なるほどなぁ")
    
@respond_to(".+")
def choose_action(message):
    global question
    global answer
    functions = {
    ("辛い","死にたい"): greeting_3,
    ("ハロー","こんにちは","おはよう","こんばんは"):greeting_1,
    ("問題出して"):chicas_question,
    ("今何してるの"):chicas_now,
    ("最近の辛いメータ教えて"):tsurai_mater}
    ms=message.body["text"]
    for words, function in functions.items():
        if ms in words:
            function(message)
            return
    if question!="":
        result_ans(message,answer,ms)
    else:
        a_m=random.choice["ふむ","？","ほう","なるほど","へー","ふーん"]
        message.reply(a_m)
        

def result_ans(message,ans,ms):
    if result(ans,ms):
        message.reply("正解！")
    else:
        message.reply("残念、正解は"+ans+"でした")
    global question
    question=""
    global answer
    answer=""

