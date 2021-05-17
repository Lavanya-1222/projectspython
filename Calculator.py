from tkinter import *
r=Tk()
r.geometry("425x285")
r.resizable(0,0)
r.configure(background="Black")
a=StringVar()
def clear():
    a.set("")
def equal():
    a.set(eval(a.get()))
def show(c):
    a.set(a.get()+c)
e1=Entry(font=("",30),justify="right",textvariable=a)
e1.place(x=0,y=0,width=425,height=60)

b1=Button(text="7",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b1.place(x=5,y=65,width=100,height=50,)
b1.configure(command=lambda:show("7"))

b2=Button(text="8",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b2.place(x=110,y=65,width=100,height=50)
b2.configure(command=lambda:show("8"))

b3=Button(text="9",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b3.place(x=215,y=65,width=100,height=50)
b3.configure(command=lambda:show("9"))

b4=Button(text="+",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b4.place(x=320,y=65,width=100,height=50)
b4.configure(command=lambda:show("+"))

b5=Button(text="6",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b5.place(x=5,y=120,width=100,height=50)
b5.configure(command=lambda:show("6"))

b6=Button(text="5",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b6.place(x=110,y=120,width=100,height=50)
b6.configure(command=lambda:show("5"))

b7=Button(text="4",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b7.place(x=215,y=120,width=100,height=50)
b7.configure(command=lambda:show("4"))

b8=Button(text="-",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b8.place(x=320,y=120,width=100,height=50)
b8.configure(command=lambda:show("-"))

b9=Button(text="3",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b9.place(x=5,y=175,width=100,height=50)
b9.configure(command=lambda:show("3"))

b10=Button(text="2",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b10.place(x=110,y=175,width=100,height=50)
b10.configure(command=lambda:show("2"))

b11=Button(text="1",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b11.place(x=215,y=175,width=100,height=50)
b11.configure(command=lambda:show("1"))

b12=Button(text="*",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b12.place(x=320,y=175,width=100,height=50)
b12.configure(command=lambda:show("*"))


b13=Button(text="C",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b13.place(x=5,y=230,width=100,height=50)
b13.configure(command=clear)


b14=Button(text="0",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b14.place(x=110,y=230,width=100,height=50)
b14.configure(command=lambda:show("0"))

b15=Button(text="=",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b15.place(x=215,y=230,width=100,height=50)
b15.configure(command=equal)

b16=Button(text="/",font=("",25),fg="white",bg="gray",activebackground="pink",activeforeground="white")
b16.place(x=320,y=230,width=100,height=50)
b16.configure(command=lambda:show("/"))

r.mainloop()