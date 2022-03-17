from tkinter import font as fonts

from ADD_USER import *
from Administrator import *
from Import import *
from Infromation import *
from Login import *
from Manager import ADVISE
from User import User

Routes = [['1','Australia','palace'],['2','Australia','Grevalley']]
Transport = [['1','Car','Available'],['2','minibus','not',]]
pp = [['1','Australia'],['2','palace'],['3','jaskstop']]
Users = [['1','lane','Australia','Australia stop2','Palace','jas']]
Route = ['Australia','swizerland','Palace','Grevalley']
Trans = ['Coach','Min-bus','Private Car']
pickup = ['Australia stop1','Australia stop2','Australia stop3','jaskstop 1','kimjo sto3']





class Booking(boot.Tk):

    def __init__(self, *args, **kwargs):
        boot.Tk.__init__(self, *args, **kwargs)

        self.title_font = fonts.Font(family='cursive', size=30)
        self.title("Welcome to Trip booking system")
        self.geometry("800x800")


        panel = boot.Frame(self)

        panel.grid(row="6",column="8")

        self.configure(bg="#FFC1CC")


        self.windows_all = {}
        for frmaes in (
                Login_panel, First_page, User, ADVISE, Administrator, Information, Write_route, Add_transport, Add_pp,
                Add_User,
                Import):
            Window_title = frmaes.__name__
            window = frmaes(parent=panel, Starting_window=self)
            self.windows_all[Window_title] = window

            window.configure(bg="#FBE870")
            window.grid(row=5, column=5, sticky="nsew")


        self.Open_window("Login_panel")

    def Open_window(self, Window_title):

        window = self.windows_all[Window_title]
        window.tkraise()


class First_page(boot.Frame):

    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window





        Heading4 = boot.Label(self, text="Welcome to Solent System", fg="#D70A53")
        Heading4.grid(row=1, column=3, padx=49, pady=49)
        lable8 = boot.Button(self, text="User", width=20, bg='#D70A53', fg='white',
                           command=lambda: Starting_window.Open_window("User"))
        lable8.grid(row=2, column=3, padx=9, pady=9)
        lable9 = boot.Button(self, text="Administrator", width=20, bg='#D70A53', fg='white',
                           command=lambda: Starting_window.Open_window("Administrator"))
        lable9.grid(row=2, column=5, padx=9, pady=9)
        Login_Manager = boot.Button(self, text="ADVISOR", width=20, bg='#D70A53', fg='white',
                                  command=lambda: Starting_window.Open_window("ADVISE"))
        Login_Manager.grid(row=3, column=4, padx=9, pady=9)


class Write_route(boot.Frame):
    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window
        self.Heading1 = boot.Label(self, text="Item Number")
        self.Heading1.grid(row=1, column=0, padx=9, pady=9)
        self.Unique_number = boot.Entry(self)
        self.Unique_number.grid(row=1, column=1)
        self.Lable_text = boot.Label(self, text="ENTER Destination")
        self.Lable_text.grid(row=2, column=0, padx=9, pady=9)
        self.textbox1 = boot.Entry(self)
        self.textbox1.grid(row=2, column=1)
        self.label6 = boot.Label(self, text="ENTER Way")
        self.label6.grid(row=3, column=0, padx=9, pady=9)
        self.system_g2 = boot.Entry(self)
        self.system_g2.grid(row=3, column=1)
        Heading3 = boot.Button(self, text='Submit', width=30, bg='#D70A53', fg='grey', command=self.call_system)
        Heading3.grid(row=7, column=1)
        Heading5 = boot.Button(self, text='BACK', width=30, bg='black', fg='grey',
                           command=lambda: Starting_window.Open_window("Administrator"))
        Heading5.grid(row=7, column=2)

    def call_system(self):

        second2 = self.textbox1.get()
        t = self.system_g2.get()
        i = self.Unique_number.get()
        Routes.append([i, second2, t])


class Add_transport(boot.Frame):
    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window
        self.Heading1 = boot.Label(self, text="ENTER ID")
        self.Heading1.grid(row=1, column=0, padx=9, pady=9)
        self.Unique_number = boot.Entry(self)
        self.Unique_number.grid(row=1, column=1)
        self.Lable_text = boot.Label(self, text="ENTER Transport Name")
        self.Lable_text.grid(row=2, column=0, padx=9, pady=9)
        self.textbox1 = boot.Entry(self)
        self.textbox1.grid(row=2, column=1)
        self.label6 = boot.Label(self, text="IS AVAILABLE?")
        self.label6.grid(row=3, column=0, padx=9, pady=9)
        self.system_g2 = boot.Entry(self)
        self.system_g2.grid(row=3, column=1)
        Heading3 = boot.Button(self, text='Submit', width=20, bg='#D70A53', fg='white', command=self.call_system)
        Heading3.grid(row=7, column=1)
        Heading5 = boot.Button(self, text='BACK', width=20, bg='black', fg='white',
                           command=lambda: Starting_window.Open_window("Administrator"))
        Heading5.grid(row=7, column=2)

    def call_system(self):

        second2 = self.textbox1.get()
        t = self.system_g2.get()
        i = self.Unique_number.get()
        Transport.append([i, second2, t])

class Add_pp(boot.Frame):
    def __init__(self, parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window
        self.Heading1 = boot.Label(self, text="ENTER ID")
        self.Heading1.grid(row=1, column=0, padx=9, pady=9)
        self.Unique_number = boot.Entry(self)
        self.Unique_number.grid(row=1, column=1)
        self.Lable_text = boot.Label(self, text="ENTER Pick up Point")
        self.Lable_text.grid(row=2, column=0, padx=9, pady=9)
        self.textbox1 = boot.Entry(self)
        self.textbox1.grid(row=2, column=1)
        Heading3 = boot.Button(self, text='Submit', width=20, bg='#D70A53', fg='white', command=self.call_system)
        Heading3.grid(row=7, column=1)
        Heading5 = boot.Button(self, text='BACK', width=20, bg='black', fg='white',
                           command=lambda: Starting_window.Open_window("Administrator"))
        Heading5.grid(row=7, column=2)

    def call_system(self):

        second2 = self.textbox1.get()
        i = self.Unique_number.get()
        pp.append([i, second2])


if __name__ == "__main__":
    app = Booking()
    app.mainloop()