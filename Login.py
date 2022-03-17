import tkinter as boot


class Login_panel(boot.Frame):
    def __init__(self,parent, Starting_window):
        boot.Frame.__init__(self, parent)
        self.Starting_window = Starting_window

        self.Heading1 = boot.Label(self, text="LOGIN SYSTEM")
        self.Heading1.grid(row=2, column=1, padx=9, pady=9)
        self.Heading1 = boot.Label(self, text="ENTER USERNAME")
        self.Heading1.grid(row=3, column=0, padx=9, pady=9)
        self.id1 = boot.Entry(self)
        self.id1.grid(row=3, column=1)
        self.Lable_text = boot.Label(self, text="ENTER PASSWORD")
        self.Lable_text.grid(row=5, column=0, padx=9, pady=9)
        self.password = boot.Entry(self)
        self.password.grid(row=5, column=1)
        Heading3 = boot.Button(self, text='Submit', width=22, bg='#D70A53', fg='grey', command=self.Login_method)
        Heading3.grid(row=7, column=1)

    def Login_method(self):
        Starting_window = self.Starting_window



        if (self.id1.get() == 'admin' and self.password.get() == '123'):
                Starting_window.Open_window("First_page")

        else:
            boot.messagebox.showinfo(title="Error", message="Wrong password")