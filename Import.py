import csv
import tkinter as boot

from ADD_USER import *

class Import(boot.Frame):
    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window

        Heading4 = boot.Label(self, text="Import Data :-")
        Heading4.grid(row=1, column=3, padx=20, pady=20)

        Heading4 = boot.Button(self, text='Import User Data', width=20, bg='#D70A53', fg='white',
                           command=self.Customer_data)
        Heading4.grid(row=2, column=1)



    def Customer_data(self):

        with open('Users', 'w') as f:
            write = csv.writer(f)
            fields = ['ID', 'Name', 'Date', 'Route', 'Pick up', 'Transport']
            write.writerow(fields)
            write.writerows(Users)

        Lable_text = boot.Button(self, text='BACK', width=20, bg='red', fg='black',
                             command=lambda: self.Starting_window.Open_window("First_page"))
        Lable_text.grid(row=2, column=5)