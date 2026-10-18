import numpy as np
from tkinter import *
screen = Tk()
screen.title("ATM PIN Setup Interface")
screen.geometry("400x500")

details_frame = Frame(
    master=screen,
    height=150,
    width=360,
    bg="#fcd0b4"
)
message_box = Label(
                master=screen,
                height=5,
                width=42,
                bg="#F08888",
                fg="#6D1313"
    )
def button_pressed():
     message_box.config(text=f"Hey! {name_ent.get()}, your ATM PIN has been set.")

name_lbl = Label(
    master=details_frame,
    text="Account Name",
    bg="#B33E3E",
    fg="#FCC4C4"
)
name_ent = Entry(
    master=details_frame,
)
pin_lbl = Label(
    master=details_frame,
    text="Enter PIN",
    bg="#B33E3E",
    fg="#FCC4C4"
)
pin_ent = Entry(
    master=details_frame,
    show="*"
)
confirm_button = Button(
            master=screen,
            command=button_pressed,
            text="Set ATM PIN",
            bg="#F08888",
            fg="#6D1313"
)


keypad_frame = Frame(
    master = details_frame,
    relief = SUNKEN, 
    borderwidth = 2,
    bg = "#d8721e"
)
keys = np.array([["1","2","3"],
             ["4","5","6"],
             ["7","8","9"],
             ["#","0","*"]  ])

for i in range(4):
    keypad_frame.rowconfigure(i, weight=1, minsize=30)
 
    for j in range(3):
        keypad_frame.columnconfigure(j, weight=1, minsize=50)

        cell = Frame(
            master=keypad_frame,
            relief=RAISED,
            borderwidth=1
        )
 
        cell.grid(
            row=i,
            column=j,
            sticky="nsew"
        )
        
        number_label = Label(
            master=cell,
            text=keys[i][j],
            bg="#f5acac"
        )
 
        number_label.pack(
            padx=8,
            pady=8
        )
        confirm_button = Button(
                    master=screen,
                    command = button_pressed,
                    text="Set ATM PIN",
                    bg="#F08888",
                    fg="#6D1313"
        )
     
details_frame.place(x=20, y=10)
 
name_lbl.place(x=15, y=25)
name_ent.place(x=155, y=25)

pin_lbl.place(x=15, y=75)
pin_ent.place(x=155, y=75)

keypad_frame.place(x=85, y=180)
 
confirm_button.place(x=145, y=370)
 
message_box.place(x=25, y=410)

screen.mainloop()