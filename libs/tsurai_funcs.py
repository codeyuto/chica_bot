import csv
import datetime
from genericpath import exists
import os
def return_tsurai():
    data=[]
    time_now=datetime.datetime.now()
    with open("tsurai_note.csv","r",encoding="utf-8") as f:
        reader = csv.reader(f)
        
        three_weeks_ago=time_now-datetime.timedelta(days=21)
        two_weeks_ago=time_now-datetime.timedelta(days=14)
        one_weeks_ago=time_now- datetime.timedelta(days=7)
        counter_three=0
        counter_two=0
        counter_one=0
        counter_now=0
        next(reader)

        for r in reader:
            data=datetime.datetime(int(r[0]),int(r[1]),int(r[2]),int(r[3]),int(r[4]))
            if data<=time_now and data>one_weeks_ago:
                counter_now+=1
            elif data<=one_weeks_ago and data>two_weeks_ago:
                counter_one+=1
            elif data<=two_weeks_ago and data>three_weeks_ago:
                counter_two+=1
            elif data<=three_weeks_ago and data>three_weeks_ago-datetime.timedelta(days=7):
                counter_three+=1
        finally_data=[counter_three,counter_two,counter_one,counter_now]    
        result=finally_data.index(max(finally_data))
        
    return [counter_three,counter_two,counter_one,counter_now,result]


        

def write_tsurai():
    if os.path.exists("tsurai_note.csv")==False:
        with open("tsurai_note.csv","w",encoding="utf-8",newline="") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(["year","month","day","hour","minute"])

    with open("tsurai_note.csv","a",encoding="utf-8",newline="") as f:
        time=datetime.datetime.now()
        data=[time.year,time.month,time.day,time.hour,time.minute]
        writer = csv.writer(f,delimiter=",")
        writer.writerow(data)

print(return_tsurai())