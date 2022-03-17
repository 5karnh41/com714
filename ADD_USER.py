import tkinter as boot

from main import Route, pickup, Trans, Users , pp, Routes, Transport


class Add_User(boot.Frame):

    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window
        Heading1 = boot.Label(self, text="ITEM NUMBER")
        Heading1.grid(row=1, column=0, padx=9, pady=9)
        self.Unique_number = boot.Entry(self)
        self.Unique_number.grid(row=1, column=1)
        Lable_text = boot.Label(self, text="USERNAME NAME")
        Lable_text.grid(row=2, column=0, padx=9, pady=9)
        self.textbox1 = boot.Entry(self)
        self.textbox1.grid(row=2, column=1)
        Lable_text = boot.Label(self, text="Date")
        Lable_text.grid(row=3, column=0, padx=9, pady=9)
        self.textbox2 = boot.Entry(self)
        self.textbox2.grid(row=3, column=1)
        Heading4 = boot.Label(self, text="Select Route")
        Heading4.grid(row=4, column=0, padx=9, pady=9)
        self.Textbox10 = boot.StringVar(self)
        self.Textbox10.set(Route[0])
        self.l = boot.OptionMenu(self, self.Textbox10, *Route)
        self.l.grid(row=4, column=1, padx=9, pady=9)

        Lable_text = boot.Label(self, text="Pick Up")
        Lable_text.grid(row=5, column=0, padx=9, pady=9)
        self.Textbox11 = boot.StringVar(self)
        self.Textbox11.set(pickup[0])
        self.l1 = boot.OptionMenu(self, self.Textbox11, *pickup)
        self.l1.grid(row=5, column=1, padx=9,pady=9)


        Lable_text = boot.Label(self, text="Transport")
        Lable_text.grid(row=6, column=0, padx=9, pady=9)
        self.textbox3 = boot.StringVar(self)
        self.textbox3.set(Trans[0])
        self.label15 = boot.OptionMenu(self, self.textbox3, *Trans)
        self.label15.grid(row=6, column=1, padx=9, pady=9)

        Lable_text = boot.Button(self, text='Submit', width=20, bg='#D70A53', fg='white', command=self.Add_Customer)
        Lable_text.grid(row=7, column=1)
        Lable_text = boot.Button(self, text='BACK', width=20, bg='black', fg='white',
                           command=lambda: Starting_window.Open_window("ADVISE"))
        Lable_text.grid(row=7, column=2)

    def Add_Customer(self):
        second2 = self.textbox1.get()
        i = self.Unique_number.get()
        second3 = self.textbox2.get()
        j = self.Textbox10.get()
        second4 = self.Textbox11.get()
        second5 = self.textbox3.get()

        Users.append([i, second2, second3, j, second4, second5])