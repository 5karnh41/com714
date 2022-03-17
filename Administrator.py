import tkinter as boot
from tkinter import Entry, GROOVE, END

from ADD_USER import *

class Administrator(boot.Frame):

    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window
        self.Heading1 = boot.Label(self, text="ADMIN FUNCTIONS")
        self.Heading1.grid(row=1, column=3, padx=9, pady=9)
        Lable_text = boot.Button(self, text='SEE ROUTE', width=20, bg='#FFC1CC', fg='black', command=self.information_view)
        Lable_text.grid(row=3, column=3, padx=9, pady=9)
        Lable_text = boot.Button(self, text='SEE TRANSPORT', width=20, bg='#FFC1CC', fg='black', command=self.information_view_transport)
        Lable_text.grid(row=3, column=5, padx=9, pady=9)
        Lable_text = boot.Button(self, text='ADD ROUTE', width=20, bg='#FFC1CC', fg='black',
                           command=lambda: Starting_window.Open_window("Write_route"))
        Lable_text.grid(row=3, column=7, padx=9, pady=9)
        Lable_text = boot.Button(self, text='SEE DESTINATION', width=20, bg='#FFC1CC', fg='black', command=self.information_view_pp)
        Lable_text.grid(row=4, column=3, padx=9, pady=9)
        Lable_text = boot.Button(self, text='ADD Transport', width=20, bg='#FFC1CC', fg='black',
                           command=lambda: Starting_window.Open_window("Add_transport"))
        Lable_text.grid(row=4, column=5, padx=9, pady=9)
        Lable_text = boot.Button(self, text='ADD LOCATION', width=20, bg='#FFC1CC', fg='black', command=lambda :Starting_window.Open_window("Add_pp"))
        Lable_text.grid(row=4, column=7, padx=9, pady=9)
        Lable_text = boot.Button(self, text='BACK', width=20, bg='red', fg='black',
                           command=lambda: Starting_window.Open_window("First_page"))
        Lable_text.grid(row=6, column=4)

    def information_view(self):
        newone = []
        ll = len(Routes)
        for i in range(ll):

            lower = []

            for j in range(3):
                final = Entry(relief=GROOVE)

                final.grid(row=i, column=j, sticky="nsew")

                final.insert(END, Routes[i][j])
                lower.append(final)

            newone.append(lower)

    def information_view_pp(self):
        newone = []
        ll = len(pp)
        for i in range(ll):

            lower = []

            for j in range(2):
                final = Entry(relief=GROOVE)

                final.grid(row=i, column=j, sticky="nsew")

                final.insert(END, pp[i][j])
                lower.append(final)

            newone.append(lower)


    def information_view_transport(self):
        newone = []
        ll = len(Transport)
        for i in range(ll):

            lower = []

            for j in range(3):
                final = Entry(relief=GROOVE)

                final.grid(row=i, column=j, sticky="nsew")

                final.insert(END, Transport[i][j])
                lower.append(final)

            newone.append(lower)