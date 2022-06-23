from tkinter import *
root = Tk()
root.title("Krishna Sharma 2101330130071")
root.geometry("750x350")
root.resizable(width=False,height=False)
label=Label(root,text="if you click the button the message will disapper",font=("Helvetica 20"),fg="blue")
label.place(x=100,y=100)
def delete():
   label.config(text="")
def on_enter(e):
    button.config(background='OrangeRed3', foreground="white")
def on_leave(e):
    button.config(background='SystemButtonFace', foreground='black')
button = Button(root, text="Click me!",
                font=('Helvetica 25 bold'),command= delete)
button.pack(pady=20)
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)
root.mainloop()