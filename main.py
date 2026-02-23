import time

from datetime import datetime ,time as dtime
import platform

if platform.system() == "Windows":
    from plyer import notification
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
        return "Windows"
    else:
        result = subprocess.run(
                    [
                        "dunstify",
                        "--action=Done,Done",
                        "--action=No,Remind Again?",
                        title,
                        message,
                    ],
                    capture_output=True,
                    text=True
                )
        
        if result.stdout.strip()=="Done":
            return True
        else:
            return False
        


def askUser():
    tell_me=input("Have you drink water ? :").strip().lower()
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

def startNotifications(delay : int ,title : str,message : str, startTime,stoptime):
    while True:
        now=datetime.now().time()
        if startTime<stoptime:
            in_stop_time=startTime<=now<=stoptime
        else:
            in_stop_time=now>=startTime or now<=stoptime
        if not in_stop_time:
            time.sleep(delay)
            done = sendNotification(title=title,message=message)
            if done:
                break
        else:
            time.sleep(60)
            

def main():
    start_time_input = input("Enter stop start time (HH:MM:SS): ")
    end_time_input = input("Enter stop end time (HH:MM:SS): ")

    startTime=datetime.strptime(start_time_input,"%H:%M:%S").time() 
    stoptime=datetime.strptime(end_time_input,"%H:%M:%S").time()

    print(startTime,stoptime)
    

    TimeInterval=int(input("Enter the Time Interval :"))
    ReminderFor=input("This reminder is for :")
    Msg=input("Enter the message that you want to show in notificaton :")
    startNotifications(TimeInterval,ReminderFor,Msg,startTime,stoptime)

if __name__ == "__main__":
    main()

