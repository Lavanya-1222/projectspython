from tkinter import *
root=Tk()
root.geometry("500x400")
root.resizable(0,0)
root.title("TIC TOC TOE")
c=1
global s
s=False
p1=StringVar()
p2=StringVar()
l=StringVar()
def reset():
  b1["text"] = ""
  b1["bg"] = "white"
  b2["text"] = ""
  b2["bg"] = "white"
  b3["text"] = ""
  b3["bg"] = "white"
  b4["text"] = ""
  b4["bg"] = "white"
  b5["text"] = ""
  b5["bg"] = "white"
  b6["text"] = ""
  b6["bg"] = "white"
  b6["text"] = ""
  b6["bg"] = "white"
  b8["text"] = ""
  b8["bg"] = "white"
  b9["text"] = ""
  b9["bg"] = "white"


def show(b):
    global c
    global s
    c=c+1
    if c%2==0:
        if(b["text"]==""):
          b["text"]="0"
          b["bg"]="pink"
    else:
        if(b["text"]==""):
          b["text"]="x"
          b["bg"]="Skyblue"

    if(b1["text"]=="0" and b2["text"]=="0"and b3["text"]=="0"):#---
        l.set("Winner is "+p1.get())
        b1["text"]=""
        b1["bg"]="white"
        b2["text"] = ""
        b2["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b7["text"] = ""
        b7["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"
        b9["text"] = ""
        b9["bg"] = "white"




    elif (b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0"):#--
         l.set("Winner is "+p1.get())
         b1["text"] = ""
         b1["bg"] = "white"
         b2["text"] = ""
         b2["bg"] = "white"
         b3["text"] = ""
         b3["bg"] = "white"
         b4["text"] = ""
         b4["bg"] = "white"
         b5["text"] = ""
         b5["bg"] = "white"
         b7["text"] = ""
         b7["bg"] = "white"
         b8["text"] = ""
         b8["bg"] = "white"
         b9["text"] = ""
         b9["bg"] = "white"

    elif (b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0"):#--
         l.set("Winner is "+p1.get())
         b1["text"] = ""
         b1["bg"] = "white"
         b2["text"] = ""
         b2["bg"] = "white"
         b3["text"] = ""
         b3["bg"] = "white"
         b4["text"] = ""
         b4["bg"] = "white"
         b5["text"] = ""
         b5["bg"] = "white"
         b6["text"] = ""
         b6["bg"] = "white"
         b7["text"] = ""
         b7["bg"] = "white"
         b8["text"] = ""
         b8["bg"] = "white"

    elif(b1["text"]=="0" and b4["text"]=="0"and b7["text"]=="0"):#|
         l.set("Winner is "+p1.get())
         b1["text"] = ""
         b1["bg"] = "white"
         b2["text"] = ""
         b2["bg"] = "white"
         b3["text"] = ""
         b3["bg"] = "white"
         b4["text"] = ""
         b4["bg"] = "white"
         b5["text"] = ""
         b5["bg"] = "white"
         b6["text"] = ""
         b6["bg"] = "white"
         b8["text"] = ""
         b8["bg"] = "white"
         b9["text"] = ""
         b9["bg"] = "white"

    elif (b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0"):  # |
         l.set("Winner is "+p1.get())
         b1["text"] = ""
         b1["bg"] = "white"
         b2["text"] = ""
         b2["bg"] = "white"
         b3["text"] = ""
         b3["bg"] = "white"
         b4["text"] = ""
         b4["bg"] = "white"
         b5["text"] = ""
         b5["bg"] = "white"
         b6["text"] = ""
         b6["bg"] = "white"
         b7["text"] = ""
         b7["bg"] = "white"
         b9["text"] = ""
         b9["bg"] = "white"

    elif (b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0"):  # |
         l.set("Winner is "+p1.get())
         b1["text"] = ""
         b1["bg"] = "white"
         b2["text"] = ""
         b2["bg"] = "white"
         b3["text"] = ""
         b3["bg"] = "white"
         b4["text"] = ""
         b4["bg"] = "white"
         b5["text"] = ""
         b5["bg"] = "white"
         b6["text"] = ""
         b6["bg"] = "white"
         b7["text"] = ""
         b7["bg"] = "white"
         b8["text"] = ""
         b8["bg"] = "white"

    elif(b1["text"]=="0" and b5["text"]=="0"and b9["text"]=="0"):#/
         l.set("Winner is "+p1.get())
         b1["text"] = ""
         b1["bg"] = "white"
         b2["text"] = ""
         b2["bg"] = "white"
         b3["text"] = ""
         b3["bg"] = "white"
         b4["text"] = ""
         b4["bg"] = "white"
         b5["text"] = ""
         b5["bg"] = "white"
         b6["text"] = ""
         b6["bg"] = "white"
         b7["text"] = ""
         b7["bg"] = "white"
         b8["text"] = ""
         b8["bg"] = "white"

    elif (b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0"):#\
         l.set("Winner is "+p1.get())
         b1["text"] = ""
         b1["bg"] = "white"
         b2["text"] = ""
         b2["bg"] = "white"
         b3["text"] = ""
         b3["bg"] = "white"
         b4["text"] = ""
         b4["bg"] = "white"
         b5["text"] = ""
         b5["bg"] = "white"
         b6["text"] = ""
         b6["bg"] = "white"
         b8["text"] = ""
         b8["bg"] = "white"
         b9["text"] = ""
         b9["bg"] = "white"


    #For Player Two
    elif(b1["text"] == "x" and b2["text"] == "x" and b3["text"] == "x"):  # ---
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b7["text"] = ""
        b7["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"
        b9["text"] = ""
        b9["bg"] = "white"

    elif (b4["text"] == "x" and b5["text"] == "x" and b6["text"] == "x"):  # --
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b3["text"] = ""
        b3["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b7["text"] = ""
        b7["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"
        b9["text"] = ""
        b9["bg"] = "white"

    elif (b7["text"] == "x" and b8["text"] == "x" and b9["text"] == "x"):  # --
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b3["text"] = ""
        b3["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b7["text"] = ""
        b7["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"

    elif (b1["text"] == "x" and b4["text"] == "x" and b7["text"] == "x"):  # |
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b3["text"] = ""
        b3["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"
        b9["text"] = ""
        b9["bg"] = "white"

    elif (b2["text"] == "x" and b5["text"] == "x" and b8["text"] == "x"):  # |
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b3["text"] = ""
        b3["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b7["text"] = ""
        b7["bg"] = "white"
        b9["text"] = ""
        b9["bg"] = "white"

    elif (b3["text"] == "x" and b6["text"] == "x" and b9["text"] == "x"):  # |
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b3["text"] = ""
        b3["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b7["text"] = ""
        b7["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"

    elif (b1["text"] == "x" and b5["text"] == "x" and b9["text"] == "x"):  # /
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b3["text"] = ""
        b3["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b7["text"] = ""
        b7["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"

    elif (b3["text"] == "x" and b5["text"] == "x" and b7["text"] == "x"):  # \
        l.set("Winner is " + p2.get())
        b1["text"] = ""
        b1["bg"] = "white"
        b2["text"] = ""
        b2["bg"] = "white"
        b3["text"] = ""
        b3["bg"] = "white"
        b4["text"] = ""
        b4["bg"] = "white"
        b5["text"] = ""
        b5["bg"] = "white"
        b6["text"] = ""
        b6["bg"] = "white"
        b8["text"] = ""
        b8["bg"] = "white"
        b9["text"] = ""
        b9["bg"]="white"


e1=Entry(textvariable=p1,fg="Red",font=("",14))
e2=Entry(textvariable=p2,fg="Red",font=("",14))

la=Label(root,textvariable=l,fg="Green",font=("Arial bold",14))
la.grid(row=2,column=3,padx=10)
l2=Label(text="Name of players",font=(" bold"))
l2.place(x=257,y=20)
e2.place(x=258,y=80,width=200,height=20)
e1.place(x=258,y=50,width=200,height=20)
# e1.grid(row=1,column=3)
b1=Button(root,width=10,height=5,command=lambda:show(b1))
b1.grid(row=0,column=0)
b2=Button(root,width=10,height=5,command=lambda:show(b2))
b2.grid(row=0,column=1)
b3=Button(root,width=10,height=5,command=lambda:show(b3))
b3.grid(row=0,column=2)
b4=Button(root,width=10,height=5,command=lambda:show(b4))
b4.grid(row=1,column=0)
b5=Button(root,width=10,height=5,command=lambda:show(b5))
b5.grid(row=1,column=1)
b6=Button(root,width=10,height=5,command=lambda:show(b6))
b6.grid(row=1,column=2)
b7=Button(root,width=10,height=5,command=lambda:show(b7))
b7.grid(row=2,column=0)
b8=Button(root,width=10,height=5,command=lambda:show(b8))
b8.grid(row=2,column=1)
b9=Button(root,width=10,height=5,command=lambda:show(b9))
b9.grid(row=2,column=2)
btn=Button(text="Reset",bg="skyblue",font=("Arial bold",12),command=reset)
btn.grid(row=4,column=1,pady=10)




root.mainloop()