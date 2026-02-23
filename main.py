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
<<<<<<< userDefine
        subprocess.run(["notify-send", title, message])
    
def askUser(title,message):
    tell_me=input(f"Have you {title} ? :").strip().lower()
=======
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
>>>>>>> main
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
<<<<<<< userDefine
            sendNotification(title=title,message=message)
            time.sleep(30)
            askUser(title,message)
=======
            done = sendNotification(title=title,message=message)
            if done:
                break
>>>>>>> main
        else:
            time.sleep(60)
            

def main():
<<<<<<< userDefine
    start_time_input = input("Enter stop start time (HH:MM:SS): ")
    end_time_input = input("Enter stop end time (HH:MM:SS): ")

    stopStart=datetime.strptime(start_time_input,"%H:%M:%S").time() 
    stopEnd=datetime.strptime(end_time_input,"%H:%M:%S").time()

    TimeInterval=int(input("Enter the Time Interval :"))
    ReminderFor=input("This reminder is for :")
    Msg=input("Enter the message that you want to show in notificaton :")
    startNotifications(TimeInterval,ReminderFor,Msg,stopStart,stopEnd)
=======
    startNotifications(5,"paani peelo","jaldi paani peelo fast fast")
>>>>>>> main

if __name__ == "__main__":
    main()

