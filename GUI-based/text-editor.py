from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Text Editor")
window.geometry("800x800")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    """ open a file """
    filepath = askopenfilename(
        filetypes=[("Text file", "*.txt"), ("All file types", "*.*")]
        # * for all/any filename or filetype
    )
    if not filepath:
        return
    txt.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt.insert(END, text)
        input_file.close()
    window.title(f"Text Editor - {filepath}")

def file_saveas():
    filepath = asksaveasfilename(
        defaultextension= "txt",
        filetypes= [("Text file", "*.txt"), ("All file types", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt.get(1.0, END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")
    
txt = Text(window)
frame = Frame(window, relief=GROOVE, bd=2)
btn_open = Button(frame, text="Open", command=open_file)
btn_save_as = Button(frame, text="Save as...", command=file_saveas)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save_as.grid(row=1, column=0, padx=5)

frame.grid(row=0,column=0, sticky="ns")
txt.grid(row=0, column=1, sticky="nsew")

window.mainloop()