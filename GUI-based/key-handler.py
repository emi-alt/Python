from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Key Handler")

def key_handler(e):
    print(e.char)

root.bind("<Key>", key_handler)
#        capital K
def btn(e):
    print("The button was clicked.")
button = Button(text="click here")
button.pack()
root.bind("<Button-1>", btn)
root.mainloop()