from tkinter import *
from tkinter.ttk import Combobox
from googletrans import Translator, LANGUAGES
from PIL import Image,ImageTk
from pyttsx3 import *


root = Tk()

root.geometry('1080x500')

root.resizable(0,0)
root.title("Project--Language Translator")


canvas=Canvas(root,width=1080,height=500)
image=ImageTk.PhotoImage(Image.open("im2.png"))
canvas.create_image(0,0,anchor=NW,image=image)
photo=PhotoImage(file="TK.png")
photo1=PhotoImage(file="button (6).png")
canvas.pack()

Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold",fg="white").pack()

Label(root,text ="Translator", font = 'arial 15 bold', bg ='white smoke' ,
      width = '20').pack(side="bottom")

Label(root,text ="Enter Text", font = 'arial 13 bold',bg="#F3F7DC").place(x=200,y=60)

Label(root,text ="Output", font = 'arial 13 bold', bg="#F3F7DC").place(x=780,y=60)


Input_text = Text(root,font=('arial 10'),
                  height = 20, padx=5, pady=5, width = 60,fg="#000",bg="#F3F7DC")
Input_text.place(x=30,y = 100)

Output_text = Text(root,font =('arial 10'),
                   height =20, wrap = WORD, padx=5, pady= 5, width =60,bg="#F3F7DC")
Output_text.place(x = 600 , y = 100)

print(list(LANGUAGES.values()))

language = list(LANGUAGES.values())
# print(language)

src_lang =Combobox(root, values=language, width =22)

x=language[21]

src_lang.place(x=20,y=60)

src_lang.set(x)

dest_lang = Combobox(root, values= list(LANGUAGES.values()), width =22)

dest_lang.place(x=890,y=60)
y=language[38]
dest_lang.set(y)



def Translate():
    t=Translator()

    translated=t.translate(text= Input_text.get(1.0,END)
                           , src = src_lang.get(), dest = dest_lang.get())

    Output_text.delete(1.0, END)

    Output_text.insert(END, translated.text)

trans_btn = Button(root,image=photo, font='arial 12 bold', command=Translate,
                       activebackground="#F3F7DC")



def speech():
  text=Input_text.get(1.0,END)

  en=init()

  en.say(text)

  en.runAndWait()

trans_btn1 = Button(root, text='Speak', font='arial 12 bold', pady=10, command=speech, image=photo1,
                       activebackground="#F3F7DC")

trans_btn.place(x=470, y=180)

trans_btn1.place(x=480, y=250)

root.mainloop()