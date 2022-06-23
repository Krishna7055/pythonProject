import tkinter
from tkinter import *
root = Tk()
root.title("Krishna Sharma 2101330130071")
root.geometry("390x370+500+400")
root.resizable(width=False , height=False)
texbox=Entry(root,font="Times 30")
texbox.place(x=1,y=1)
def clear():
    texbox.delete(0,END)
def onclick(num):
    val = texbox.get()
    if val=="0":
        texbox.delete(0,END)
    texbox.insert(END,num)
def add():
    global first,op
    first=texbox.get()
    op="+"
    texbox.delete(0,END)
def sub():
    global first,op
    first=texbox.get()
    op="-"
    texbox.delete(0,END)
def mul():
    global first,op
    first=texbox.get()
    op="*"
    texbox.delete(0,END)
def div():
    global first,op
    first=texbox.get()
    op="/"
    texbox.delete(0,END)
def equal():
    second=texbox.get()
    if op == "+":
        res=float(first)+float(second)
    elif op == "-":
        res=float(first)-float(second)
    elif op == "*":
        res=float(first)*float(second)
    elif op == "/":
        res=float(first)/float(second)
    texbox.delete(0,END)
    texbox.insert(0,res)
b7=Button(root,text="7",font="times 30",width="4",
         command=lambda:onclick("7"))
b8=Button(root,text="8",font="times 30",width="4",
         command=lambda:onclick("8"))
b9=Button(root,text="9",font="times 30",width="4",
         command=lambda:onclick("9"))
b_Add=Button(root,text="+",font="times 30",width="4",
            command=add)
b4=Button(root,text="4",font="times 30",width="4",
         command=lambda:onclick("4"))
b5=Button(root,text="5",font="times 30",width="4",
         command=lambda:onclick("5"))
b6=Button(root,text="6",font="times 30",width="4",
         command=lambda:onclick("6"))
b_Sub=Button(root,text="-",font="times 30",width="4",
            command=sub)
b1=Button(root,text="1",font="times 30",width="4",
         command=lambda:onclick("1"))
b2=Button(root,text="2",font="times 30",width="4",
         command=lambda:onclick("2"))
b3=Button(root,text="3",font="times 30",width="4",
         command=lambda:onclick("3"))
b_Mul=Button(root,text="*",font="times 30",width="4",
            command=mul)
b0=Button(root,text="0",font="times 30",width="4",
         command=lambda:onclick("0"))
b_Clear=Button(root,text="C",font="times 30",width="4",
              command=clear)
b_Equal=Button(root,text="=",font="times 30",width="4",
              command=equal)
b_Div=Button(root,text="/",font="times 30",width="4",
            command=div)
b7.place(x=1,y=50)
b8.place(x=100,y=50)
b9.place(x=199,y=50)
b_Add.place(x=298,y=50)
b4.place(x=1,y=130)
b5.place(x=100,y=130)
b6.place(x=199,y=130)
b_Sub.place(x=298,y=130)
b1.place(x=1,y=210)
b2.place(x=100,y=210)
b3.place(x=199,y=210)
b_Mul.place(x=298,y=210)
b0.place(x=1,y=290)
b_Clear.place(x=100,y=290)
b_Equal.place(x=199,y=290)
b_Div.place(x=298,y=290)
root.mainloop()

