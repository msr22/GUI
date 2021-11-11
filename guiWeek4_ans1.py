# source: https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python

from tkinter import *

win=Tk()
win.title('Hello Python')
win.geometry("400x300+10+10")

lbl1=Label(win, text='First number')
lbl2=Label(win, text='Second number')
lbl3=Label(win, text='Result')
t1=Entry(bd=3)
t2=Entry()
t3=Entry()
btn1 = Button(win, text='Add')
btn2 = Button(win, text='Sub')
btn3 = Button(win, text='Multi')
btn4 = Button(win, text='Div')

lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=100, y=100)
t2.place(x=200, y=100)

def add():
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1+num2
    t3.insert(END, str(result))

def sub():
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1-num2
    t3.insert(END, str(result))

def multi():
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1*num2
    t3.insert(END, str(result))

def div():
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1/num2
    t3.insert(END, str(result))
    
b1=Button(win, text='Add', command=add)
b2=Button(win, text='Sub', command=sub)
b3=Button(win, text='Multi', command=multi)
b4=Button(win, text='Div', command=div)

b1.place(x=150, y=150)
b2.place(x=200, y=150)
b3.place(x=250, y=150)
b4.place(x=300, y=150)
lbl3.place(x=100, y=200)
t3.place(x=200, y=200)


win.mainloop()
