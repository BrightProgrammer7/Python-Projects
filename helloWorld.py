import tkinter
from tkinter import *

tk = Tk()
tk.title('First App')
tk.geometry('250x100')


frame = Frame(tk, relief=SUNKEN, borderwidth=2, bd=2, bg="white",
              highlightbackground="blue", highlightthickness=2)
frame.pack(fill=BOTH, expand=1)

var = StringVar()
var.set("Hello World")

label = Label(frame, textvariable=var, fg="red",
              bg="yellow", cursor="dot", relief=RAISED, underline=5, wraplength=50)
label.pack(expand=1)

button = Button(frame, text="Exit", command=tk.destroy,
                padx=10, pady=3, bg="skyblue", activebackground="blue")
button.pack(side=BOTTOM)

tk.mainloop()
