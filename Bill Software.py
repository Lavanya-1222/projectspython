from tkinter import *
from math import *
import datetime
import mysql.connector as sql
import random
from tkinter import messagebox
root=Tk()
class Bill_Software:

    def __init__(self):
        bgc="#035A6D"
        fgc="white"
        sfg="yellow"
        root.geometry("1320x660")
        root.resizable(0,0)
        root.title("Bill Software")

# ------------Variables-----
        self.c_name = StringVar()
        self.phone1=StringVar()
        self.batch1=StringVar()
        self.date1=StringVar()
        self.laptop1 = IntVar()
        self.mouse1=IntVar()
        self.keyboard1=IntVar()
        self.monitor1=IntVar()
        self.webcam1=IntVar()
        self.pendrive1=IntVar()
        self.printer1=IntVar()
        self.Motherboard1=IntVar()
        self.HDD1 = IntVar()
        self.Power_Supply1=IntVar()
        self.RAM1=IntVar()
        self.Video_Card1=IntVar()
        self.SSD1=IntVar()
        self.Processor1=IntVar()


        self.laptop2 = IntVar()
        self.mouse2=IntVar()
        self.keyboard2=IntVar()
        self.monitor2=IntVar()
        self.webcam2=IntVar()
        self.pendrive2=IntVar()
        self.printer2=IntVar()
        self.Motherboard2=IntVar()
        self.HDD2 = IntVar()
        self.Power_Supply2=IntVar()
        self.RAM2=IntVar()
        self.Video_Card2=IntVar()
        self.SSD2=IntVar()
        self.Processor2=IntVar()
        self.totalprize1 = StringVar()
        self.totaltax1= StringVar()
        self.total1= StringVar()
        x=random.randint(1000,99999)
        self.batch1.set(str(x))
        self.phone1.set("(+91)")
        now1 = datetime.datetime.now()
        datenow = now1.strftime(" %d/%m/%y    %H:%M")
        self.date1.set(datenow)
        print(self.date1.get())


# ++++++++++++++++++++++++++++++++++++++++++Customer Details++++++++++++++++++++++++++++++++++++++++++
        top_frame=Frame(root,bd=8,relief="groove",height=40,bg=bgc)
        top_frame.pack(fill=X)
        label=Label(top_frame,text="Bill Software",font=("Engravers MT",20),fg=sfg,bg=bgc).pack()



        c_frame=LabelFrame(root,bd=7,relief="groove",height=40,text="Customer Details",bg=bgc,
                           fg=sfg,font=("times new roman",12,"bold"))
        c_frame.pack(fill=X, pady=3)


        cname=Label(c_frame,text="Customer Name :",font=("times new roman",15,"bold"),bg=bgc,fg="white")
        cname.grid(row=0,column=0,padx=20,pady=5)
        cname_en=Entry(c_frame,width=25,bd=4,relief="sunken",fg="red",font=("arial bold",10),textvariable=self.c_name)
        cname_en.grid(row=0, column=1, pady=5,padx=5)


        phone = Label(c_frame, text="Phone No. :", font=("times new roman", 15,"bold"), bg=bgc, fg="white")
        phone.grid(row=0, column=2, padx=20, pady=5)
        phone_en = Entry(c_frame, width=18, bd=4, relief="sunken",fg="red",font=("arial bold",10),textvariable=self.phone1)
        phone_en.grid(row=0, column=3, pady=5,padx=5)


        batch = Label(c_frame, text="Batch No. :", font=("times new roman", 15,"bold"), bg=bgc, fg="white")
        batch.grid(row=0, column=4, padx=20, pady=5)
        batch_en = Entry(c_frame,width=18, bd=4, relief="sunken",fg="red",font=("arial bold",10),textvariable=self.batch1)
        batch_en.grid(row=0, column=5, pady=5,padx=5)


        search=Button(c_frame,text="SEARCH",width=10,fg="blue",bd=2,relief="groove", font=("times new roman", 10,"bold"))
        search.grid(row=0,column=6,pady=5,padx=10)



        date= Label(c_frame, text="Date :", font=("times new roman", 15, "bold"), bg=bgc, fg="white")
        date.grid(row=0, column=7,pady=5,padx=20)
        date_en= Entry(c_frame, width=15, bd=4, relief="sunken", fg="black", font=("arial bold", 11),
                         textvariable=self.date1)

        date_en.grid(row=0, column=8,pady=5)
# --------------------------------------------------thing f1---------------------------------------------
        thing_f=LabelFrame(root,text="Products",font=("times new roman", 12,"bold")
                                       ,bd=7,relief="groove",bg=bgc,fg=sfg)

        thing_f.place(x=0, y=120,width=475,height=420)
# ---------------------------------------------Heading---------------------------------------
        products = Label(thing_f, text="PRODUCTS", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        products.grid(row=0, column=0, pady=10, padx=20,sticky=W)

        price = Label(thing_f, text="PRICE", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        price.grid(row=0, column=1, pady=10, padx=20)

        qtv = Label(thing_f, text="QTV", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        qtv.grid(row=0, column=2, pady=10, padx=20)

# ------------------------------------------products------------------------------------
        laptop = Label(thing_f, text="QTV", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        laptop.grid(row=0, column=2, pady=10, padx=20)
        laptop = Label(thing_f, text="Laptop:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        laptop.grid(row=1, column=0, pady=10, padx=30)
        laptop_en1= Entry(thing_f, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10)
                          ,textvariable=self.laptop1)
        laptop_en1.grid(row=1, column=1, pady=5)
        laptop_en2= Entry(thing_f, width=5, bd=4, relief="sunken", fg="black",font=("arial bold", 10),textvariable=self.laptop2)
        laptop_en2.grid(row=1, column=2, pady=5)

        Mouse = Label(thing_f, text="Mouse:", bg=bgc, font=("times new roman", 15, "bold"),fg="lightgreen")
        Mouse.grid(row=2, column=0, pady=10, padx=30)
        Mouse_en1 = Entry(thing_f, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.mouse1)
        Mouse_en1.grid(row=2, column=1, pady=5)
        Mouse_en2 = Entry(thing_f, width=5, bd=4, relief="sunken", textvariable=self.mouse2, fg="black",font=("arial bold", 10))
        Mouse_en2.grid(row=2, column=2, pady=5)

        Keyboard = Label(thing_f, text="Keyboard:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        Keyboard.grid(row=3, column=0, pady=10, padx=30)
        Keyboard_en1 = Entry(thing_f, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.keyboard1)
        Keyboard_en1.grid(row=3, column=1, pady=5)
        Keyboard_en2 = Entry(thing_f, width=5, bd=4, relief="sunken", textvariable=self.keyboard2, fg="black",font=("arial bold", 10))
        Keyboard_en2.grid(row=3, column=2, pady=5)

        Monitor = Label(thing_f, text="Monitor:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        Monitor.grid(row=4, column=0, pady=10, padx=30)
        Monitor_en1 = Entry(thing_f, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.monitor1)
        Monitor_en1.grid(row=4, column=1, pady=5)
        Monitor_en2 = Entry(thing_f, width=5, bd=4, relief="sunken", textvariable=self.monitor2, fg="black",font=("arial bold", 10))
        Monitor_en2.grid(row=4, column=2, pady=5)

        WebCam = Label(thing_f, text="WebCam:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        WebCam.grid(row=5, column=0, pady=10, padx=30)
        WebCam_en1 = Entry(thing_f, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.webcam1)
        WebCam_en1.grid(row=5, column=1, pady=5)
        WebCam_en2 = Entry(thing_f, width=5, bd=4, relief="sunken", textvariable=self.webcam2, fg="black",font=("arial bold", 10))
        WebCam_en2.grid(row=5, column=2, pady=5)

        pendrive = Label(thing_f, text="Pendrive:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        pendrive.grid(row=6, column=0, pady=10, padx=30)
        pendrive_en1 = Entry(thing_f, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.pendrive1)
        pendrive_en1.grid(row=6, column=1, pady=10)
        pendrive_en2 = Entry(thing_f, width=5, bd=4, relief="sunken", textvariable=self.pendrive2, fg="black",font=("arial bold", 10))
        pendrive_en2.grid(row=6, column=2, pady=10)

        printer = Label(thing_f, text="printer:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        printer.grid(row=7, column=0, pady=10, padx=30)
        printer_en1 = Entry(thing_f, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.printer1)
        printer_en1.grid(row=7, column=1, pady=10)
        printer_en2 = Entry(thing_f, width=5, bd=4, relief="sunken", textvariable=self.printer2, fg="black",font=("arial bold", 10))
        printer_en2.grid(row=7, column=2, pady=10)
# ---------------------------------------------------things f2-------------------------------
        thing_f2 = LabelFrame(root, text="Products", font=("times new roman", 12, "bold")
                             , bd=7, relief="groove", bg=bgc, fg=sfg)

        thing_f2.place(x=480, y=120, width=475, height=420)
# ======================================heading=============================
        products = Label(thing_f2, text="PRODUCTS", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        products.grid(row=0, column=0, pady=10, padx=35, sticky=W)

        price = Label(thing_f2, text="PRICE", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        price.grid(row=0, column=1, pady=10, padx=35)

        qtv = Label(thing_f2, text="QTV", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        qtv.grid(row=0, column=2, pady=10, padx=35)
# ----------------------------------products2--------------------------------------
        Motherboard = Label(thing_f2, text="Motherboard:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        Motherboard.grid(row=1, column=0, pady=10, padx=30)
        Motherboard_en1 = Entry(thing_f2, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.Motherboard1)
        Motherboard_en1.grid(row=1, column=1, pady=5)
        Motherboard_en2 = Entry(thing_f2, width=5, bd=4, relief="sunken",textvariable=self.Motherboard2, fg="black", font=("arial bold", 10))
        Motherboard_en2.grid(row=1, column=2, pady=5)

        HDD= Label(thing_f2, text="Hard Disk", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        HDD.grid(row=2, column=0, pady=10, padx=30)
        HDD_en1= Entry(thing_f2, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.HDD1)
        HDD_en1.grid(row=2, column=1, pady=5)
        HDD_en2= Entry(thing_f2, width=5, bd=4, relief="sunken", textvariable=self.HDD2, fg="black",font=("arial bold", 10))
        HDD_en2.grid(row=2, column=2, pady=5)


        Power_Supply = Label(thing_f2, text="Power_Supply:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        Power_Supply.grid(row=3, column=0, pady=10, padx=30)
        Power_Supply_en1= Entry(thing_f2, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.Power_Supply1)
        Power_Supply_en1.grid(row=3, column=1, pady=5)
        Power_Supply_en2= Entry(thing_f2, width=5, bd=4, relief="sunken", textvariable=self.Power_Supply2, fg="black",font=("arial bold", 10))
        Power_Supply_en2.grid(row=3, column=2, pady=5)


        RAM = Label(thing_f2, text="RAM:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        RAM.grid(row=4, column=0, pady=10, padx=30)
        RAM_en1 = Entry(thing_f2, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.RAM1)
        RAM_en1.grid(row=4, column=1, pady=5)
        RAM_en2= Entry(thing_f2, width=5, bd=4, relief="sunken", textvariable=self.RAM2, fg="black",font=("arial bold", 10))
        RAM_en2.grid(row=4, column=2, pady=5)


        Video_Card = Label(thing_f2, text="Video_Card:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        Video_Card.grid(row=5, column=0, pady=10, padx=30)
        Video_Card_en1 = Entry(thing_f2, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.Video_Card1)
        Video_Card_en1.grid(row=5, column=1, pady=5)
        Video_Card_en2= Entry(thing_f2, width=5, bd=4, relief="sunken", textvariable=self.Video_Card2, fg="black",font=("arial bold", 10))
        Video_Card_en2.grid(row=5, column=2, pady=5)


        SSD = Label(thing_f2, text="SSD:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        SSD.grid(row=6, column=0, pady=10, padx=30)
        SSD_en1 = Entry(thing_f2, width=20, bd=4, relief="sunken", fg="black", font=("arial bold", 10),textvariable=self.SSD1)
        SSD_en1.grid(row=6, column=1, pady=10)
        SSD_en2= Entry(thing_f2, width=5, bd=4, relief="sunken", textvariable=self.SSD2, fg="black",font=("arial bold", 10))
        SSD_en2.grid(row=6, column=2, pady=10)


        Processor= Label(thing_f2, text="Processor:", fg="lightgreen", bg=bgc, font=("times new roman", 15, "bold"))
        Processor.grid(row=7, column=0, pady=10, padx=30)
        Processor_en1= Entry(thing_f2, width=20, bd=4, relief="sunken", fg="black",font=("arial bold", 10),textvariable=self.Processor1)
        Processor_en1.grid(row=7, column=1, pady=10)
        Processor_en2= Entry(thing_f2, width=5, bd=4, relief="sunken", textvariable=self.Processor2, fg="black",font=("arial bold", 10))
        Processor_en2.grid(row=7, column=2, pady=10)
# ==================================================bill area===============================
        bill_f=Frame(root,bd=7,relief="groove",bg=fgc)
        bill_f.place(x=960,y=120,width=370,height=420)
        bill_title=Label(bill_f,text="Bill Area",font=("arial",15,"bold"),bd=5,relief="groove",bg=fgc)
        bill_title.pack(fill=X)


        scroll_y=Scrollbar(bill_f,orient="vertical")
        scroll_y.pack(side="right",fill=Y)
        self.text=Text(bill_f,yscrollcommand=scroll_y.set,font="arial 11 bold")
        self.text.pack(fill=BOTH)
        scroll_y.config(command=self.text.yview)
# -------------------------------------------Button_F--------------------------------
        bottom_f=LabelFrame(root,bd=7,relief="groove",text="Bill Menu",font=("times new roman bold",12),fg=sfg,bg=bgc)
        bottom_f.place(x=0,y=540,relwidth=1,height=120)


        totalPrize=Label(bottom_f,text="Total products Prize :",font=("times new roman bold",15),fg="lightgreen",bg=bgc)
        totalPrize.grid(row=0,column=0,padx=10,pady=10)
        totalPrize_en = Entry(bottom_f, width=22, bd=4, relief="sunken", fg="red", font=("arial bold", 10),
                          textvariable=self.totalprize1)
        totalPrize_en.grid(row=0, column=1, pady=10)

        totaltax=Label(bottom_f,text=" Total Products Tax :",font=("times new roman bold",15),fg="lightgreen",bg=bgc)
        totaltax.grid(row=1,column=0,padx=10,pady=10)
        totaltax_en = Entry(bottom_f, width=22, bd=4, relief="sunken", fg="red", font=("arial bold", 10)
                            ,textvariable=self.totaltax1)
        totaltax_en.grid(row=1, column=1, pady=10)

        total=Label(bottom_f,text="  Total :",font=("times new roman bold",15),fg="lightgreen",bg=bgc)
        total.grid(row=0,column=2,pady=10,rowspan=2)
        total_en = Entry(bottom_f, width=30, bd=4, relief="sunken", fg="red", font=("arial bold", 10)
                         ,textvariable=self.total1)
        total_en.grid(row=0, column=3,rowspan=2)
# =========================button_f=================================
        btn_f=Frame(bottom_f,bd=5,relief="groove",bg="white")
        btn_f.place(x=687,y=5,width=605,height=82)
        btn=Button(btn_f,width=9,height=2,font=("arial 12 bold"),bd=6,text="Total",bg="lightgreen",command=self.ctotalprize)
        btn.grid(row=0,column=0,padx=5,pady=6)

        btn = Button(btn_f, width=9, height=2, font=("arial 12 bold"), bd=6, text="Genrate Bill",
                     bg="lightgreen",command=lambda:[self.billarea(), self.DB()])
        btn.grid(row=0, column=1, padx=5, pady=6)

        btn = Button(btn_f, width=9, height=2, font=("arial 12 bold"), bd=6, text="clear",
                     bg="lightgreen")
        btn.grid(row=0, column=2, padx=5, pady=6)

        btn = Button(btn_f, width=9, height=2, font=("arial 12 bold"), bd=6, text="Exit",
                     bg="lightgreen")
        btn.grid(row=0, column=3, padx=5, pady=6)

        btn = Button(btn_f, width=9, height=2, font=("arial 12 bold"), bd=6, text="Print",
                     bg="lightgreen")
        btn.grid(row=0, column=4, padx=5, pady=6)
    def ctotalprize(self):
    # ========variables===========
        totalprize1=self.totalprize1
        totaltax1=self.totaltax1
        total1=self.total1

        laptop1=self.laptop1.get()
        mouse1=self.mouse1.get()
        keyboard1=self.keyboard1.get()
        monitor1=self.monitor1.get()
        webcam1=self.webcam1.get()
        pendrive1=self.pendrive1.get()
        printer1=self.printer1.get()
        Motherboard1=self.Motherboard1.get()
        HDD1=self.HDD1.get()
        Power_Suply1=self.Power_Supply1.get()
        RAM1=self.RAM1.get()
        Video_Card1=self.Video_Card1.get()
        SSD1=self.SSD1.get()
        Processor1=self.Processor1.get()

        laptop2=self.laptop2.get()
        mouse2=self.mouse2.get()
        keyboard2=self.keyboard1.get()
        monitor2=self.monitor2.get()
        webcam2=self.webcam2.get()
        pendrive2=self.pendrive2.get()
        printer2=self.printer2.get()
        Motherboard2=self.Motherboard2.get()
        HDD2=self.HDD2.get()
        Power_Suply2=self.Power_Supply2.get()
        RAM2=self.RAM2.get()
        Video_Card2=self.Video_Card2.get()
        SSD2=self.SSD2.get()
        Processor2=self.Processor2.get()
# =======================================Total prize===========================================
        self.ctotalprize=int((laptop1*laptop2)+(mouse1*mouse2)+(keyboard1*keyboard2)+(monitor1*monitor2)\
                          +(webcam1*webcam2)+(pendrive1*pendrive2)+(printer1*printer2)+(Motherboard1*Motherboard2)+(HDD1*HDD2)+(Power_Suply1*Power_Suply2)\
                            +(RAM1*RAM2)+(Video_Card1*Video_Card2)+(SSD1*SSD2)+(Processor1*Processor2))
        ctotalprize=self.ctotalprize
        totalprize1.set("Rs."+str(ctotalprize))
# =======================================Total tax===========================================
        self.ctotaltax = int((ctotalprize*0.05))
        ctotaltax = self.ctotaltax
        totaltax1.set("Rs." + str(ctotaltax))
# =======================================Total===========================================
        total=ctotalprize+ctotaltax

        self.total1.set("Rs." + str(total))
    def welcome(self):
       self.text.delete("1.0",END)
       self.text.insert(END,"\tWelcom To Yash Retail\n")
       self.text.insert(END, f"\n  Date : \t         {self.date1.get()}")
       self.text.insert(END,f"\n  Bill Number : {self.batch1.get()}")
       self.text.insert(END,f"\n  Cutomer Name : {self.c_name.get()}")
       self.text.insert(END,f"\n  Phone Number : {self.phone1.get()}")
       self.text.insert(END,f"\n\n=====================================")
       self.text.insert(END,"\n  Products\t\tQTY\t\tPrice")
       self.text.insert(END, f"\n=====================================")
    def billarea(self):
        if self.c_name.get()=="" or self.phone1.get()=="":
            # messagebox.showerror("Error","Cutomer details are must")
             pass
        else:
            self.welcome()
            if self.laptop1.get()!=0:
                self.lap="Laptop"
                self.text.insert(END, f"\n  Laptop :\t\t{self.laptop2.get()}\t\t{(self.laptop1.get()*self.laptop2.get())}")
            if self.mouse1.get()!=0:
                self.mou="Mouse"
                self.text.insert(END, f"\n  Mouse :\t\t{self.mouse2.get()}\t\t{(self.mouse1.get()*self.mouse2.get())}")
            if self.keyboard1.get()!=0:
                self.key="Keyboard"
                self.text.insert(END, f"\n  Keyboard :\t\t{self.keyboard2.get()}\t\t{(self.keyboard1.get()*self.keyboard2.get())}")
            if self.monitor1.get()!=0:
                self.mon="Monitor"
                self.text.insert(END, f"\n  Monitor :\t\t{self.monitor2.get()}\t\t{(self.monitor1.get()*self.monitor2.get())}")
            if self.webcam1.get()!=0:
                self.web="WebCam"
                self.text.insert(END, f"\n  WebCam :\t\t{self.webcam2.get()}\t\t{(self.webcam1.get()*self.webcam2.get())}")
            if self.pendrive1.get()!=0:
                self.pen="Pendrive"
                self.text.insert(END, f"\n  Pendrive :\t\t{self.pendrive2.get()}\t\t{(self.pendrive1.get()*self.pendrive2.get())}")
            if self.printer1.get()!=0:
                self.pri="Printer"
                self.text.insert(END, f"\n  Printer :\t\t{self.printer2.get()}\t\t{(self.printer1.get()*self.printer2.get())}")
            if self.Motherboard1.get()!=0:
                self.mon="Motherboard"
                self.text.insert(END, f"\n  Motherboard :\t\t{self.Motherboard2.get()}\t\t{(self.Motherboard1.get()*self.Motherboard2.get())}")
            if self.HDD1.get()!=0:
                self.HDD="Hard Disk"
                self.text.insert(END, f"\n  Hard Disk :\t\t{self.HDD2.get()}\t\t{(self.HDD1.get()*self.HDD2.get())}")
            if self.Power_Supply1.get()!=0:
                self.pow="Power_Supply"
                self.text.insert(END, f"\n  Power Supply :\t\t{self.Power_Supply2.get()}\t\t{(self.Power_Supply1.get()*self.Power_Supply2.get())}")
            if self.RAM1.get()!=0:
                self.text.insert(END, f"\n  RAM :\t\t{self.RAM2.get()}\t\t{(self.RAM1.get()*self.RAM2.get())}")
            if self.Video_Card1.get()!=0:
                self.text.insert(END, f"\n  Video Card :\t\t{self.Video_Card2.get()}\t\t{(self.Video_Card1.get()*self.Video_Card2.get())}")
            if self.SSD1.get()!=0:
                self.SSD="SSD"
                self.text.insert(END, f"\n  SSD :\t\t{self.SSD2.get()}\t\t{(self.SSD1.get()*self.SSD2.get())}")
            if self.Processor1.get()!=0:
                self.pro="Processor"
                self.text.insert(END, f"\n  Processor :\t\t{self.Processor2.get()}\t\t{(self.Processor1.get()*self.Processor2.get())}")

            if self.totalprize1.get()!="Rs.0":
               self.text.insert(END, f"\n-------------------------------------------------------------------")
               self.text.insert(END,f"\n  Total Product Prize  :  {self.totalprize1.get()}")
            if self.totaltax1.get() != "Rs.0":
              self.text.insert(END,f"\n  Total Product Tax  :     {self.totaltax1.get()}")
            if self.total1.get() != "Rs.0":
              self.text.insert(END,f"\n-------------------------------------------------------------------")
              self.text.insert(END,f"\n  Total Bill :                       {self.total1.get()}")
              self.text.insert(END,f"\n-------------------------------------------------------------------")

              self.text.insert(END,f"\n\n          \t\tTHANK YOU\t")
    def DB(self):
                con = sql.connect(user="root", passwd="Lava", database="Yash", host="localhost",
                                  auth_plugin="mysql_native_password", port=8080
                                  )
                if con.is_connected():
                    print("Connected")
                else:
                    print("Not connected")
                myc = con.cursor()
                try:


                        q1 ="insert into Bill_Software(Batch_no,Customer_name,Phone_no,Date,Total_product_price,Total_product_tax,Total)values(%s,%s,%s,%s,%s,%s,%s);"
                        val = (self.batch1.get(),self.c_name.get(),self.phone1.get(),self.date1.get(),self.totalprize1.get(),self.totaltax1.get(),self.total1.get())
                        myc.execute(q1,val)
                        print(myc.rowcount, "row inserted")

                        con.commit()
                        # Hello lavanya


                except Exception as e:
                        print(e)
                        con.rollback()
                q2="select * from Bill_Software;"

                myc.close()

obj=Bill_Software()
root.mainloop()