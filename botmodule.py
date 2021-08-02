from slackbot.bot import respond_to
from slackbot.bot import listen_to
 
#メンションに対する応答
@respond_to("ハロー")
def greeting_1(message):
    # Slackに応答を返す
    message.reply("あら、こんにちは")
 
# 「listen_to」はメンションがなくても応答する
@listen_to("わーーーー")
def greeting_2(message):
    message.reply("うるさいわね……")
