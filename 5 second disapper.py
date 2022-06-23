from tkinter import *
win = Tk()
win.title("Krishna Sharma 2101330130071")
win.geometry("750x400")
Label(win, text= "This window will get closed after 5 seconds...",
      font=('Helvetica 20 bold'),fg="red").pack(pady=20)
#Automatically close the window after 5 seconds
win.after(5000,lambda:win.destroy()) # 5000ms = 5 s
win.mainloop()