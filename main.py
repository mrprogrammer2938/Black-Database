#!/usr/bin/python3
# Black DataBase v1.2
# Data Base Connector
import os
import platform
import sys
import webbrowser
from datetime import datetime
try:
    from tkinter import *
    from tkinter.colorchooser import askcolor
    from tkinter.ttk import *
    from tkinter.messagebox import *
except ImportError:
    os.system("pip install tk-tools")
try:
    import mysql.connector
except ImportError:
    os.system("pip install mysql-connector-python")
try:
    from win10toast import ToastNotifier
except ImportError:
    os.system("pip install win10toast")

class black_database(object):
    def __init__(self):
        super(black_database,self).__init__()

    def main_window(self):
        global root
        root = Tk()
        root.title('Black-DataBase')
        self.photo = PhotoImage(file = 'black.png')
        self.database_help = """
help
exit or quit
INSERT INTO customers (name, address) VALUES (n,n)
show database
DELETE FROM customers WHERE address = n
"""
        global Host,Password,Database,user
        menu = Menu(root)

        aboutmenu = Menu(menu,tearoff=0)
        aboutmenu.add_command(label='Help',accelerator="F1",command=self.black_help)
        aboutmenu.add_command(label='Black',accelerator="F2",command=self.black)
        thememenu = Menu(root,tearoff=0)
        thememenu.add_command(label='Dark',command=self.dark)
        thememenu.add_command(label='Light',command=self.light)
        thememenu.add_command(label='Custom',command=self.custom)
        donate_file = Menu(menu,tearoff=0)
        donate_file.add_command(label='donate',accelerator="F5",command=self.donate)
        menu.add_cascade(label='About',menu=aboutmenu)
        menu.add_cascade(label='Theme',menu=thememenu)
        menu.add_cascade(label='Donate',menu=donate_file)

        global txt
        root.config(menu=menu)

        txt = Text(root,width=20,height=30)
        txt.pack()
        txt.place(bordermode=INSIDE,x=10,y=1)

        self.user_label = Label(root,text='Enter User:')
        self.user_label.pack()
        self.user = Entry(root)
        self.user.pack()
        self.user.focus()

        self.host_label = Label(root,text='Enter Host:',background='white')
        self.host_label.pack()
        self.Host = Entry(root)
        self.Host.pack()

        self.pass_label = Label(root,text='Enter Password:',background='white')
        self.pass_label.pack()
        self.Password = Entry(root,show="*")
        self.Password.pack()

        self.pass_label_2 = Label(root,text='Retype Password',background='white')
        self.pass_label_2.pack()
        self.Password_re = Entry(root,show="*")
        self.Password_re.pack()

        self.database_label = Label(root,text='Enter Database:')
        self.database_label.pack()

        self.Database = Entry(root)
        self.Database.pack()
        global login,exit
        login = Button(root,text='Login',command=lambda: self.login_database())
        login.pack()
        login.place(x=215,y=210)
        exit = Button(root,text='Exit',command=lambda: self.ext())
        exit.pack()
        exit.place(x=215,y=240)
        root.bind("<F1>",lambda x: self.black_2(x))
        root.bind("<F2>",lambda x: self.black_help_2(x))
        root.bind("<F5>",lambda x: self.donate_2(x))
        root.iconphoto(False,self.photo)
        root.resizable(0,0)
        root.attributes('-alpha',0.9)
        root.configure(background='white')
        root.geometry("500x300")
        root.mainloop()

    def ext(self):
        root.destroy()
        root.quit()

    def login_database(self):
        x = []
        global dbs,user_lbl
        try:
            if self.Database.get() == '' or self.Database.get() == ' ':
                x.append(1)
            elif self.Password.get() == '' or self.Password.get() == ' ':
                x.append(2)
            elif self.Password.get() == self.Password_re.get():
                print(True)
            elif self.Host == '' or self.Host == ' ':
                x.append(3)
            elif self.user == '' or self.user == ' ':
                x.append(4)
            else:
                user_lbl = Label(root,text=self.user.get(),background='white',foreground='black')
                user_lbl.pack(side=BOTTOM)
                txt.insert(END,f"Connecting User: {self.user.get()}")
                database = mysql.connector.connect(user=self.user.get(),password=self.Password.get(),host=self.Host.get(),database=self.Database.get(),)
                print(database)
                try:
                    dbs = database.cursor()
                    txt.insert(END,f"\nUser: {self.user.get()} Connected!")
                    toast = ToastNotifier() #                                            Black Data Base Icon
                    toast.show_toast('Black DataBase',f'Data Base: {self.Database.get()}',icon_path="None",duration=5)
                    self.database_command()
                except:
                    self.main_window()
                finally:
                    pass
            if x:
                showerror(title='Cannot Connecting',message='Please, Check user-password-host-DataBase')
        except mysql.connector.errors.InterfaceError:
            toaster = ToastNotifier() #                                            Black Data Base Icon
            toaster.show_toast('Black DataBase',f'Data Base: {self.Database.get()}')
            txt.insert(END,f"Cannot Connecting To {self.user.get()}")
            showerror(title='MySql Error',message='Cannot Connecting To Database')
            root.destroy()
            self.main_window()
        finally:
            print()
    def donate(self):
        webbrowser.open_new_tab('https://idpay.ir/mrprogrammer2938')

    def donate_2(self,x):
        webbrowser.open_new_tab('https://idpay.ir/mrprogrammer2938')

    def database_command(self):
        time_zone = datetime.time()
        try:
            while True:
                command = input(f"{self.user}/Command/> ").split()
                if command == []:
                    pass
                elif command.lower() == 'help':
                    print(self.database_help)
                elif command.lower() == 'exit' or command.lower() == 'quit':
                    print("Stop...\n")
                    self.user.delete(0,END)
                    self.Database.delete(0,END)
                    self.Password.delete(0,END)
                    self.Host.delete(0,END)
                    print(f"Exiting User On: {time_zone}")
                else:
                    dbs.execute(command)
                    dbs.commit()
        except (KeyboardInterrupt,EOFError,Exception):
            print("Stop...\n")
            self.user.delete(0,END)
            self.Database.delete(0,END)
            self.Password.delete(0,END)
            self.Host.delete(0,END)
            print(f"Exiting User On: {time_zone}")
            sys.exit()
    def black(self):
        webbrowser.open_new_tab('https://github.com/black-software-Com')

    def black_2(self,x):
        webbrowser.open_new_tab('https://github.com/black-software-Com')

    def black_help(self):
        webbrowser.open_new_tab('')




    def black_help_1(self,x):
        webbrowser.open_new_tab('')
    def dark(self):
        root.config(background='black')
        self.database_label.config(background='black',foreground='green')
        self.host_label.config(background='black',foreground='green')
        self.pass_label.config(background='black',foreground='green')
        self.pass_label_2.config(background='black',foreground='green')
        self.user_label.config(background='black',foreground='green')
        user_lbl.config(background='black',foreground='green')
    def light(self):
        root.config(background='white')
        self.database_label.config(background='white',foreground='black')
        self.host_label.config(background='white',foreground='black')
        self.pass_label.config(background='white',foreground='black')
        self.pass_label_2.config(background='white',foreground='black')
        self.user_label.config(background='white',foreground='black')
        user_lbl.config(background='white',foreground='black')
    def custom(self):
        try:
            choosecolor = askcolor(title='Choose Color')
            root.config(background=choosecolor[1])
            self.database_label.config(background='white',foreground='black')
            self.host_label.config(background='white',foreground='black')
            self.pass_label.config(background='white',foreground='black')
            self.pass_label_2.config(background='white',foreground='black')
            self.user_label.config(background='white',foreground='black')
        except TclError:
            print("Please, Choose Color!\n")
    @staticmethod
    def title():
        if platform.system() == 'Linux':
            os.system(f"printf '\033]2;Black-DataBase'")
        else:
            os.system("title Black-DataBase")

if __name__ == '__main__':
    time_zone = datetime.now()
    window = black_database()
    window.title()
    print(f"\nStart Black-DataBase At: {time_zone}")
    window.main_window()
    print(f"Close Black-DataBase At: {time_zone}")
