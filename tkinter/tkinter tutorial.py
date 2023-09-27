from tkinter import *

root = Tk()
root.configure(background="cyan")
root.geometry("300x300+900+100")

#Creating a Label widget
myLabel1 = Label(root, text = "Hello World",bg="red",fg="white",font="Arial")
myLabel2 = Label(root, text = "My name is Duken Tran", bg="yellow",fg="green",font="VnTime")
#Shoving it onto the screen

myLabel1.grid(row = 0, column=0)
myLabel2.grid(row = 2, column=0)


root.mainloop()