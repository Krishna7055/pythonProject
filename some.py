from tkinter import *
root = Tk()
root.title('Registration')
root.geometry('600x400')
mylabel1 = Label(root,
 text='Student Registration Page',
 font=('Arial',25,'bold underline'),
       fg='blue',bg='white')
mylabel2 = Label(root,text='Enter name',font='Arial 15')
txt1 = Entry(root,font='Arial 15')
mylabel3 = Label(root,text='Enter Roll No',Simple Calculator
 font='Arial 15'
 )
txt2 = Entry(root,font='Arial 15')
mylabel4 = Label(root,
 text="Gender",
 font='Arial 15'
 )
gender = StringVar()
r1 = Radiobutton(root,
 text="Male",
 font='Arial 15',
 variable=gender,
 value='Male'
 )
r2 = Radiobutton(root,
 text="Female",
 font='Arial 15',
 variable=gender,
 value='Female'
 )
r1.select()
r2.deselect()
mylabel5 = Label(root,
 text="Select Course",
 font='Arial 15'
 )
var1 = StringVar()
var2 = StringVar()
ch1 = Checkbutton(root,
 text="Java",
 variable=var1,
 font='Arial 15')
ch2 = Checkbutton(root,
 text="Python",
 variable=var2,
 font='Arial 15')
ch1.deselect()
ch2.deselect()
mybutton = Button(root,text='Submit',font='Arial 15')
mylabel1.place(x=100,y=10)
mylabel2.place(x=20,y=60)
txt1.place(x=150,y=60)
mylabel3.place(x=20,y=100)
txt2.place(x=150,y=100)
mylabel4.place(x=20,y=140)
r1.place(x=150,y=140)
r2.place(x=300,y=140)
mylabel5.place(x=20,y=180)
ch1.place(x=150,y=180)
ch2.place(x=300,y=180)
mybutton.place(x=200,y=220)
root.mainloop()

