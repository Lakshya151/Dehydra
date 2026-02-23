import tkinter as tk
from main import startNotifications
import threading
from datetime import datetime ,time as dtime


def on_button_click():
    try:
        startTime=datetime.strptime("00:00:00","%H:%M:%S").time() 
        stopTime=datetime.strptime("07:00:00","%H:%M:%S").time() 
        title = entry1.get()
        message = entry2.get()

        t = threading.Thread(
            target=startNotifications,
            args=(5,title, message,startTime,stopTime),
           
        )
        t.start()
        root.destroy()
    except:
        result_label.config(text="Error has occured")



root = tk.Tk()
root.title("DeHyra")
root.geometry("300x200")


entry1 = tk.Entry(root)
entry1.pack(pady=5)



entry2 = tk.Entry(root)
entry2.pack(pady=5)


button = tk.Button(root, text="Add", command=on_button_click)
button.pack(pady=5)



result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=5)



root.mainloop()