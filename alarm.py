import datetime
from playsound import playsound
ALhour = int(input("Enter hour: "))
ALminute = int(input("Enter minute: "))
am_pm = (input("am or pm: "))

if am_pm =="pm":
    ALhour += 12

while True:
    if ALhour==datetime.datetime.now().hour and ALminute==datetime.datetime.now().minute:
        print("ALARM ..")
        playsound("chaffing.wav")
        break


