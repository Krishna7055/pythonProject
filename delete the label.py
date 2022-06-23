from tkinter import *
root = Tk()
root.geometry("400x400")
def remove_text():
    label.config(text="")
label = Label(root, text="Hello World!", font="BOLD")
label.pack()
Button(root, text="Delete", command=remove_text).pack()
root.mainloop()