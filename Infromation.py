import tkinter as boot
from tkinter import Entry, GROOVE, END

from ADD_USER import *

class Information(boot.Frame):

    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window
        Heading1 = boot.Label(self, text="Details of User", font=Starting_window.title_font)
        Heading1.grid(row=6,column=1)

        Heading4 = boot.Button(self, text='Click here to view', width=20, bg='#D70A53', fg='white', command=self.show_estate_pro)
        Heading4.grid(row=8, column=1)
        button = boot.Button(self, text="Go to the start page",
                           command=lambda: Starting_window.Open_window("First_page"))
        button.grid(row=9,column=2)

    def show_estate_pro(self):

        newone = []
        ll = len(Users)
        for i in range(ll):
            lower = []
            for j in range(4):
                final = Entry(relief=GROOVE)


                final.grid(row=i, column=j, sticky="nsew")


                final.insert(END, Users[i][j])
                lower.append(final)

            newone.append(lower)
        Lable_text = boot.Button(self, text='BACK', width=20, bg='red', fg='black',
                           command=lambda: self.Starting_window.Open_window("User"))
        Lable_text.grid(row=7, column=4)