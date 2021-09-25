import time
from datetime import datetime
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM\n")
print("Setting up alarm..")
while True:
    now = str(datetime.now())
    now = now.split(' ')
    current_time = now[1][:5]
    if current_time == alarm_time:
        print("Wake Up!")
        break