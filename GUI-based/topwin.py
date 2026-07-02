from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Main Window")

def topwin():
    top = Toplevel()
    top.geometry("170x100")
    top.title("Top Window")
    l2 = Label(top, text="This is top level.")
    l2.pack()
    top.mainloop()
l = Label(root, text="This is root window.")
btn = Button(root, text="Click to open top level", command=topwin)
l.pack()
btn.pack()
root.mainloop()