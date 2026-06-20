from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Message boxes")
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "STOP! there's a virus in your device!")
    #                      title     message
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40,y=50)
def question():
    messagebox.askquestion("Question", "Do you wish to exit the window?")
btn1 = Button(text="Anwer a question", command=question)
btn1.pack()
root.mainloop()