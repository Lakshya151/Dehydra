import time
from plyer import notification
import winsound

state=True
while state:
    time.sleep(10)
    winsound.Beep(1000,1) # this is for beep sound
    notification.notify(
        title="wate reminder !",
        message="Time to drink water, Sir",
        timeout=10
    )
    state=False # remove this to get msg repeatedly
  
