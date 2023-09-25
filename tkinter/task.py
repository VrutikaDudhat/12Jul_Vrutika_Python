import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()

screen.title("calculator")
screen.geometry("400x500")

l1=tkinter.Label(text="Value1")
l1.grid(row=0,column=0)

l2=tkinter.Label(text="Value2")
l2.grid(row=1,column=0)

txt1=tkinter.Entry()
txt1.grid(row=0,column=1)

txt2=tkinter.Entry()
txt2.grid(row=1,column=1)

def add():
    l1=int(txt1.get())
    l2=int(txt2.get())
    a=l1+l2

    #messagebox.showinfo("success","your data has been saved")

    print("Value1:",txt1.get())
    print("Value2:",txt2.get())
    messagebox.showinfo("your data",a)

btn1=tkinter.Button(command=add,text="addition")
btn1.place(x=30,y=120)

def sub():
    l1=int(txt1.get())
    l2=int(txt2.get())
    a=l1-l2

    print("Value1:",txt1.get())
    print("Value2:",txt2.get())
    messagebox.showinfo("your data",a)

btn2=tkinter.Button(command=sub,text="sub")
btn2.place(x=100,y=120)

def mul():
    l1=int(txt1.get())
    l2=int(txt2.get())
    a=l1*l2

    print("Value1:",txt1.get())
    print("Value2:",txt2.get())
    messagebox.showinfo("your data",a)

btn3=tkinter.Button(command=mul,text="mul")
btn3.place(x=150,y=120)

def div():
    l1=int(txt1.get())
    l2=int(txt2.get())
    a=l1/l2

    print("Value1:",txt1.get())
    print("Value2:",txt2.get())
    messagebox.showinfo("your data",a)

btn4=tkinter.Button(command=div,text="div")
btn4.place(x=200,y=120)
    

tkinter.mainloop()


