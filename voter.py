import tkinter as tk
import socket
from tkinter import *
from Voting_panel import votingPg


def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again...Failed Connecting.."
    Label(frame1, text=message, font=('Comic Sans MS', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()

def log_server_main(root,frame1,client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Casted via this Voter ID."
        failed_return(root,frame1,client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter. Try To Register again via Admin Panel -> Register Voter."
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)



def voterLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Voter Login", font=('Comic Sans MS', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="Use The Registered Voter ID from Admin Panel -> Register Voters. Use the ID and password for casting votes.",font=('Comic Sans MS', 15, 'italic'),justify="center",wraplength=500).grid(row = 1,column = 1,rowspan=1)
    Label(frame1, text="Voter ID:      ", anchor="e", font=('Comic Sans MS', 10),justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Password:   ", anchor="e", font=('Comic Sans MS', 10),justify=LEFT).grid(row = 3,column = 0)

    voter_ID = tk.StringVar()
    name = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = voter_ID)
    e1.grid(row = 2,column = 2)
    e3 = Entry(frame1, textvariable = password, show = '*')
    e3.grid(row = 3,column = 2)

    sub = Button(frame1, text="Login", width=10, command = lambda: log_server_main(root, frame1, client_socket, voter_ID.get(), password.get()))
    Label(frame1, text="").grid(row = 4,column = 0,ipadx=20,ipady=20)
    sub.grid(row = 5, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()



