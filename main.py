import time
from plyer import notification
from datetime import datetime ,time as dtime


import platform

if platform.system() == "Windows":
    import winsound
else:
    import subprocess


def sendNotification(title,message):
    if platform.system() == "Windows":
        winsound.Beep(1000,400) 
        notification.notify(
            title=title,
            message=message,
            timeout=60
        )
    else:
        subprocess.run(["notify-send", title, message])
    
def askUser(title,message):
    tell_me=input(f"Have you {title} ? :").strip().lower()
    if tell_me=="yes":
        print("OK!")
    else:
        while True:
            time.sleep(10)
            tell_again=input(f"{title} ?" ).strip().lower()
            if tell_again=="yes":
                print("OK!")
                break
            else:
                sendNotification(title=title, message=f"Reminder:{message}")

def startNotifications(delay : int ,title : str,message : str, stopStart,stopEnd):
    while True:
        now=datetime.now().time()
        if stopStart<stopEnd:
            in_stop_time=stopStart<=now<=stopEnd
        else:
            in_stop_time=now>=stopStart or now<=stopEnd
        if not in_stop_time:
            time.sleep(delay)
            sendNotification(title=title,message=message)
            time.sleep(30)
            askUser(title,message)
        else:
            time.sleep(60)
            

def main():
    start_time_input = input("Enter stop start time (HH:MM:SS): ")
    end_time_input = input("Enter stop end time (HH:MM:SS): ")

    stopStart=datetime.strptime(start_time_input,"%H:%M:%S").time() 
    stopEnd=datetime.strptime(end_time_input,"%H:%M:%S").time()

    TimeInterval=int(input("Enter the Time Interval :"))
    ReminderFor=input("This reminder is for :")
    Msg=input("Enter the message that you want to show in notificaton :")
    startNotifications(TimeInterval,ReminderFor,Msg,stopStart,stopEnd)

if __name__ == "__main__":
    main()

