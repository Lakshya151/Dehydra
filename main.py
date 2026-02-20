import time
from plyer import notification
import winsound
      
def sendNotification(title,message):
    winsound.Beep(1000,1) 
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def startNotifications(delay : int ,times : int,title : str,message : str):
    while times>0:
        time.sleep(delay)
        sendNotification(title=title,message=message)

def main():
    sendNotification(5,5,"paani peelo","jaldi paani peelo fast fast")

if __name__ == "__main__":
    main()

