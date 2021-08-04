from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random

def choose_question():
    question={"ハローキティのリボンの色は？":"赤",
    "Pythonの名前の由来となったコメディ番組は？":"モンティ・パイソン",
    "Rubyの開発者の名前は？":"まつもとゆきひろ"
    }

    q,a=random.choice(list.(question.items()))

    return  q,a

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
    
