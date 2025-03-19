from tkinter import *

Window=Tk()
Window.title("KeyHandlers")
Window.geometry("500x500")

def KeyPress(event):
    print(event.char)

Window.bind("<Key>",KeyPress)

def HandleClick(event):
    print("The Button was clicked")

Window.bind("<Button-1>",HandleClick)

B1=Button(text="Click Me")
B1.place(x=200,y=200)

Window.mainloop()