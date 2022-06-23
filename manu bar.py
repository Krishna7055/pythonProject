from tkinter import *
root = Tk()
root.title("Krishna Sharma 2101330130071")
root.geometry("600x400+500+400")
mylabel=Label(root,text="",font="Arial 20")
mylabel.place(x=20,y=50)

def click(msg):
    val="you have clicked" + msg
    mylabel.config(text=val)

mainmenu=Menu(root)
root.config(menu=mainmenu)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label='New',
                    command=lambda:click("NEW"))
filemenu.add_command(label='open')
filemenu.add_separator()
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as ...')
filemenu.add_command(label='Print')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.destroy)

mainmenu.add_cascade(label="File",menu=filemenu)

mainmenu.add_cascade(label="Edit")
mainmenu.add_cascade(label="view")
mainmenu.add_cascade(label="insert")
root.mainloop()