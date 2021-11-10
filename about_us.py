import tkinter as tk

from tkinter import *
from main import Home

class BulletLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        text = kwargs.pop('text', '')
        kwargs['text'] = self.bulletise(text)
        tk.Label.__init__(self, master, *args, **kwargs)

    def bulletise(self, text):
        if len(text) == 0: 
            return ''
        lines = text.split('\n')
        parts = []
        for line in lines: 
            parts.extend(['\u2022', line, '\n']) 
        return ''.join(parts)

    def configure(self, *args, **kwargs):
        text = kwargs.pop('text', '')
        if text != '':
            kwargs['text'] = self.bulletise(text)
        tk.Label.configure(*args, **kwargs)





def about_us(root,frame1):


    root.title("About This Application")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Automated Voting System", font=('Comic Sans MS', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="Subject         -> Computer Networks",font=('Comic Sans MS', 15, 'italic'),justify="left").grid(row = 1,column = 1)
    Label(frame1, text="Course Code     -> 18CSC302J",font=('Comic Sans MS', 15, 'italic'),justify="left").grid(row = 2,column = 1)
    Label(frame1, text="Section         -> N-2",font=('Comic Sans MS', 15, 'italic'),justify="left").grid(row = 3,column = 1)
    Label(frame1, text="Branch          -> CSE-BD",font=('Comic Sans MS', 15, 'italic'),justify="left").grid(row = 4,column = 1)
    Label(frame1, text="").grid(row = 5,column = 1)

    Label(frame1, text="Team : ",font=('Comic Sans MS', 15, 'italic'),justify="left").grid(row = 6,column = 1)
    blabel = BulletLabel(root, text='Anurag Pancholi (RA1911027010075)\nHarsh Kumar Sharma (RA1911027010082)\nSayyed Mansoor Ahmed (RA191027010083) \nHarsh Sharma (RA191027010085)',font=('Comic Sans MS', 16))
    

    blabel.pack()
    frame1.pack()
    root.mainloop()



