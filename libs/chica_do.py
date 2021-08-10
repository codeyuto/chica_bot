import datetime,random
def choose_do():
    t_now = datetime.datetime.now()
    if (t_now.hour==12):
        return "お昼ご飯食べてる"
    else:
        return random.choice(["寝てた","本読んでる","お掃除してる","映画見てる"])


