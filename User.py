import tkinter as boot
from tkinter import Entry, GROOVE, END

from ADD_USER import *

class User(boot.Frame):

    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window

        Heading4 = boot.Label(self, text="Deatils")
        Heading4.grid(row=1, column=3, padx=20, pady=20)

        View_prop = boot.Button(self, text='View User Detail', width=20, bg='#D70A53', fg='white',
                              command=self.User_information)
        View_prop.grid(row=2, column=3, padx=9, pady=9)
        Lable_text = boot.Button(self, text='BACK', width=20, bg='red', fg='black',
                           command=lambda: Starting_window.Open_window("First_page"))
        Lable_text.grid(row=3, column=3)

    def User_information(self):

        newone = []
        ll = len(Users)


        for i in range(ll):
            lower = []

            for j in range(4):
                panel = Entry(self,relief=GROOVE)

                panel.grid(row=i, column=j, sticky="nsew")

                panel.insert(END, Users[i][j])
                lower.append(panel)

            newone.append(lower)
        Lable_text = boot.Button(self, text='BACK', width=20, bg='red', fg='black',
                               command=lambda :self.Starting_window.Open_window("First_page"))
        Lable_text.grid(row=2, column=5)