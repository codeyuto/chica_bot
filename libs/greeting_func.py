import datetime,random

def time_greeting():
    time=datetime.datetime.now()
    if(time.hour>=5 and time.hour<=11):
        return random.choice(["おはよう","おはよー"])
    elif(time.hour>=12 and time.hour<=16):
        return random.choice(["あら、こんにちは","こんにちは"])
    elif(time.hour>=17 and time.hour<=19):
        return "こんばんは"
    elif(time.hour>=20 or time.hour<5):
        return random.choice(["こんばんは","(´ぅω・｀)ﾈﾑｲ","zzz..."])
    else:
        return "どうも"