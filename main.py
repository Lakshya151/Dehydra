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
            timeout=10
        )
    else:
        subprocess.run(["notify-send", title, message])
    

def startNotifications(delay : int ,title : str,message : str):
    stopStart=dtime(0,0,0) 
    stopEnd=dtime(6,0,0) 
    while True:
        now=datetime.now().time()
        if not stopStart<=now<=stopEnd:
            time.sleep(delay)
            sendNotification(title=title,message=message)

def main():
    startNotifications(5,"paani peelo","jaldi paani peelo fast fast")

if __name__ == "__main__":
    main()

