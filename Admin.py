import subprocess as sb_p
import tkinter as tk
import Voter_reg_panel as regV
import admin_functions_panel as adFunc
from tkinter import *
from Voter_reg_panel import *
from admin_functions_panel import *



def AdminHome(root,frame1,frame3):
    root.title("Admin Panel")
    for widget in frame1.winfo_children():
        widget.destroy()

    
    

    Label(frame1, text="Admin Panel", font=('Comic Sans MS', 25, 'bold'),justify='center').grid(row = 0, column = 1)
    Label(frame1, text="Use this Panel For First Running the Server Side. Once The Server initiates, you can register voters and show casted votes.",font=('Comic Sans MS', 15, 'italic'),justify="center",wraplength=500).grid(row = 11,column = 1)

    #Admin Login
    runServer = Button(frame1, text="Run the main Server", width=25,justify='left', command = lambda: sb_p.call('start python Server.py', shell=True))

    #Voter Login
    registerVoter = Button(frame1, text="Register Voter Candidates", width=25, command = lambda: regV.Register(root, frame1))

    #Show Votes
    showVotes = Button(frame1, text="Show All Casted Votes", width=25, command = lambda: adFunc.showVotes(root, frame1))

    #Reset Data
    reset = Button(frame1, text="Reset Server", width=25, command = lambda: adFunc.resetAll(root, frame1))

    #Recursive Admin Panel:
    #adminPanelb = Button(frame1, text="Back to Admin Panel", width=25,command = lambda: AdminHome(root, frame1)).grid(row=9,column=1, columnspan=2)
    adminPanelb = Button(frame3 , text="Back to Admin Panel", width=25,justify='center',command = lambda: AdminHome(root, frame1,frame3))
    adminPanelb.place(x=130,y=10)
    
    
    

    Label(frame1, text="").grid(row = 2,column = 0,)
    Label(frame1, text="").grid(row = 4,column = 0)
    Label(frame1, text="").grid(row = 6,column = 0)
    Label(frame1, text="").grid(row = 8,column = 0)
    runServer.grid(row = 3, column = 0,ipadx=20,ipady=20)
    registerVoter.grid(row = 3, column = 2,ipadx=20,ipady=20)
    showVotes.grid(row = 7, column = 1,ipadx=20,ipady=20)


    frame1.pack()
    frame3.pack()
    root.mainloop()


def log_admin_main(root,frame1,admin_ID,password):

    if(admin_ID=="admin" and password=="admin"):
        frame3 = root.winfo_children()[1]
        AdminHome(root, frame1, frame3)
    else:
        msg = Message(frame1, text="Either ID or Password is Incorrect. Please Try Again.", width=500)
        msg.grid(row = 7, column = 0, columnspan = 5)


def AdmLogin(root,frame1):

    root.title("Admin Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Administrative Login Panel", font=('Comic Sans MS', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="Use this panel for configuring internal server. Make Sure to have proper credentials.", font=('Comic Sans MS', 10, 'bold')).grid(row = 1, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="Admin ID:      ", anchor="e", justify=LEFT, font=('Comic Sans MS', 15, 'bold')).grid(row = 3,column = 0)
    Label(frame1, text="Password:       ", anchor="e", justify=LEFT, font=('Comic Sans MS', 15, 'bold')).grid(row = 4,column = 0)
    Label(frame1,text="Use 'admin' for both Login and Password", font=('Comic Sans MS', 12, 'italic')).grid(row=5,column=2)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = admin_ID)
    e1.grid(row = 3,column = 2)
    e2 = Entry(frame1, textvariable = password, show = '*')
    e2.grid(row = 4,column = 2)

    sub = Button(frame1, text="Login", width=10, command = lambda: log_admin_main(root, frame1, admin_ID.get(), password.get()))
    Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 6, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


