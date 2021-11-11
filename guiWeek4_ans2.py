# source: https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python

from tkinter import *

win=Tk()
win.title('Hello Python')
win.geometry("400x300+10+10")

lbl1=Label(win, text='Annual gross salary')
lbl2=Label(win, text='Saving target')
lbl3=Label(win, text='Amount needed to be saved each month')
t1=Entry(bd=3)
t2=Entry()
t3=Entry()
btn1 = Button(win, text='Calculate amount needed to be saved each month')

lbl1.place(x=40, y=50)
t1.place(x=200, y=50)
lbl2.place(x=40, y=100)
t2.place(x=200, y=100)

def calculate():
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result = num2/12
    t3.insert(END, str(result))

b1=Button(win, text='Calculate amount needed to be saved each month', command=calculate)

b1.place(x=40, y=150)
lbl3.place(x=40, y=200)
t3.place(x=40, y=220)


win.mainloop()
