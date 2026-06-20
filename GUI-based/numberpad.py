from tkinter import *
root = Tk()
root.geometry("250x300")
root.title("NumberPad")

nums = [
    [9, 8, 7], # 0
    [6, 5, 4], # 1
    [3, 2, 1], # 2
    ["#", 0, "*"] # 3 
    # 0  1  2
]
for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = Frame(master=root, relief=RAISED, borderwidth=2)
        frame.grid(row=i, column=j)
        label = Button(master=frame, text=nums[i][j], bg="#A795CC")
        label.pack(padx=3, pady=3)
root.mainloop()