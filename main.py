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
            tell_again=input("Pani piya ? :").strip().lower()
            if tell_again=="yes":
                print("OK!")
                break
            else:
                sendNotification(title="pani piya ?", message="Reminder: Bsdk Pani to peele ?")

def startNotifications(delay : int ,title : str,message : str):
    stopStart=dtime(0,0,0) 
    stopEnd=dtime(6,0,0) 
    while True:
        now=datetime.now().time()
        if not stopStart<=now<=stopEnd:
            time.sleep(delay)
            done = sendNotification(title=title,message=message)
            if done:
                break
        else:
            time.sleep(3600)
            

def main():
    startNotifications(5,"paani peelo","jaldi paani peelo fast fast")

if __name__ == "__main__":
    main()

