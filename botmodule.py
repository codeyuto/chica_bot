from libs.question_funcs import choose_question,result
from slackbot.bot import respond_to
from slackbot.bot import listen_to

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
    @respond_to(r".+")
    def answer(message2):
        if result(data,message2.body["text"]):
            message2.reply("正解！")
            return
        else:
            message2.reply("残念")
            return


