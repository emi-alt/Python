from tkinter import *
root = Tk()
root.title("Login App")
root.geometry("400x400")
frame = Frame(master=root, height = 200, width= 400, bg="#959ECC")
 
l1 = Label(frame, text = "Full Name", bg="#A893CC", fg='white', width=12)
l2 = Label(frame, text = "Email Id", bg="#A893CC", fg='white', width=12)
l3 = Label(frame, text = "Enter Password", bg="#A893CC", fg='white', width=12)


namee = Entry(frame)
email = Entry(frame)
password = Entry(frame, show="*")

def display():
	name = namee.get()
	greet = "Hey "+name
	message =  "\nYou can now use your account."
	textbox.insert(END, greet)
	textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text = "Create Account", command=display, bg="#CF97D8")

frame.place(x=20,y=0)
l1.place(x=20, y=20)
namee.place(x=150, y=20)
l2.place(x=20, y=80)
email.place(x=150, y=80)
l3.place(x=20, y=140)
password.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()