from tkinter import *
from tkinter import messagebox

Window=Tk()
Window.title("Warning Message")
Window.geometry("500x500")

def msg():
    messagebox.askyesno("Have you installed antivirus software?")

B1=Button(text="Click me",command=msg())
B1.place("200x200")

Window.mainloop()

