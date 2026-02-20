import tkinter as tk


root = tk.Tk()


root.title("My First GUI")
root.geometry("400x300")


label = tk.Label(root, text="Hello, Kashi.")
label.pack()

btn = tk.Button(root,text="start notification")
btn.pack()


root.mainloop()
