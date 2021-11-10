import tkinter as tk
import utils as df
from tkinter import *
from utils import *
from PIL import ImageTk,Image

def resetAll(root,frame1):

    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes Count Panel")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Total Votes Count", font=('Comic Sans MS', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="You can check out the total votes collected over here. NOTE : If the latest counts are not being reflected, do restart the server from the ADMIN panel", font=('Comic Sans MS', 15, 'italic'),justify="center",wraplength=500).grid(row = 1,column = 1, rowspan=1)

    vote = StringVar(frame1,"-1")

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((25,38),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45,30),Image.ANTIALIAS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40,35),Image.ANTIALIAS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    tdpLogo = ImageTk.PhotoImage((Image.open("img/tdp.jpg")).resize((40,35),Image.ANTIALIAS))
    tdpImg = Label(frame1, image=tdpLogo).grid(row = 6,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 7,column = 0)


    Label(frame1, text="BJP                             ->", font=('Comic Sans MS', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Comic Sans MS', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text="Cong                             ->", font=('Comic Sans MS', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Comic Sans MS', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text="AAP                             ->", font=('Comic Sans MS', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], font=('Comic Sans MS', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text="Shiv Sena                        ->", font=('Comic Sans MS', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['ss'], font=('Comic Sans MS', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text="TDP                              ->", font=('Comic Sans MS', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['tdp'], font=('Comic Sans MS', 12, 'bold')).grid(row = 6, column = 2)

    Label(frame1, text="NOTA                             ->", font=('Comic Sans MS', 12, 'bold')).grid(row = 7, column = 1)
    Label(frame1, text=result['nota'], font=('Comic Sans MS', 12, 'bold')).grid(row = 7, column = 2)

    frame1.pack()
    root.mainloop()


