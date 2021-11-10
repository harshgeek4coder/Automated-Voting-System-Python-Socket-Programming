import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin
from about_us import *


def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    
    Label(frame2, text="                                                                         ").grid(row = 0,column = 1)
    Label(frame2, text="                                                                         ").grid(row = 0,column = 2)
    Label(frame2, text="         ").grid(row = 1,column = 1)
    frame2.pack(side=TOP)

    root.title("Automated Voting System Application")
    


    Label(frame1, text="Automated Voting System", font=('Comic Sans MS', 25, 'bold')).grid(row = 0, column = 1, rowspan=1)

    subs_pack = Label(frame1,text="This is a simple application developed for purpose of exhibiting TCP-Based Network Configuration for Casting of votes between Server and Client", font=('Comic Sans MS', 15, 'italic'),justify="center",wraplength=500).grid(row=12,column=1)
    


    Label(frame1, text="").grid(row = 1,column = 0)
    #Admin Login
    admin = Button(frame1, text="Admin Login Panel", width=25, command = lambda: AdmLogin(root, frame1))

    #Voter Login
    voter = Button(frame1, text="Voter Login Panel", width=25, command = lambda: voterLogin(root, frame1))

    #New Tab
    newTab = Button(frame1, text="Open New Window ", width=25, command = lambda: sb_p.call('start python main.py', shell=True))

    #Home Tab
    homeTab=Button(frame1, text="Home Panel", command = lambda: Home(root, frame1, frame2),width=25)

    #About
    aboutTab=Button(frame1, text="About Application", command = lambda: about_us(root,frame1),width=25)

    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="").grid(row = 4,column = 0)
    Label(frame1, text="").grid(row = 6,column = 0)
    admin.grid(row = 3, column = 0,ipadx=20,ipady=20)
    
    voter.grid(row = 3, column = 2,ipadx=20,ipady=20)
    newTab.grid(row = 7, column = 0,ipadx=20,ipady=20)
    homeTab.grid(row=7,column=2,ipadx=20,ipady=20)
    aboutTab.grid(row=9,column=1,ipadx=20,ipady=20)
    

    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('1280x720')
    
    
    frame1 = Frame(root)
    frame2 = Frame(root)
    Home(root, frame1, frame2)


if __name__ == "__main__":
    new_home()
