#!/usr/bin/python3
# Black-Attacker v1.0
import socket
import webbrowser
import subprocess
import os
import time
import requests
from tkinter import *
from tkinter.messagebox import showinfo,showerror
from tkinter.ttk import Button as TButton
from tkinter.colorchooser import askcolor
from tkinter.ttk import Notebook,Frame
"""
1. Menu = Theme
2. login & signup
"""
class attack(object):
    def __init__(self):
        super(attack,self).__init__()
    def account(self):
        global root
        root = Tk()
        root.title('Black-Attacker/Acount')
        menu = Menu(root)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='Developer',command=self.dev)
        filemenu.add_command(label='Black',command=self.black)
        themefile = Menu(menu,tearoff=0)
        themefile.add_command(label='Dark',command=self.dark)
        themefile.add_command(label='Light',command=self.light)
        themefile.add_command(label='Customize',command=self.customize)
        extfile = Menu(menu,tearoff=0)
        extfile.add_command(label='Quit',accelerator='Alt+F4',command=self.ext)
        menu.add_cascade(label='About',menu=filemenu)
        menu.add_cascade(label='Theme',menu=themefile)
        menu.add_cascade(label='Exit',menu=extfile)
        root.config(menu=menu)
        self.i = True
        self.login_user = Button(root,text='Login',width=9,height=3,command=self.login)
        self.login_user.pack()
        self.signup = Button(root,text='Signup',width=9,height=3,command=self.signup)
        self.signup.pack()
        self.exit = Button(root,text='Exit',width=9,height=3,command=self.ext)
        self.exit.pack()
        root.geometry("300x200")
        root.resizable(0,0)
        root.mainloop()
    def dark(self):
        root.config(background='black')

    def light(self):
        root.config(background='white')
    def customize(self):
        color = askcolor()
        root.config(background=color[1])
    def login(self):
        global user,password,username,main_password,login_button,back,exit
        self.login_user.destroy()
        self.signup.destroy()
        self.exit.destroy()
        root.title('Black-Attacker/Login')
        self.x = False
        user = Entry(root,width=15)
        user.pack()
        password = Entry(root,width=15,show="*")
        password.pack()
        username = user.get()
        main_password = password.get()
        login_button = TButton(root,text='Login',command=self.login_check)
        login_button.pack()
        login_button.place(bordermode=OUTSIDE,x=110,y=60)
        exit = TButton(root,text='Exit',command=self.ext)
        exit.pack()
        exit.place(bordermode=OUTSIDE,x=110,y=85)
        root.geometry("300x300")
        root.resizable(0,0)
        root.mainloop()
    def des_lo(self):
        self.login_user.destroy()
        self.signup.destroy()
        self.exit.destroy()
        self.signup()
    def signup(self):
        global user,password
        root.title('Black-Attacker/Signup')
        self.login_user.destroy()
        self.signup.destroy()
        self.exit.destroy()
        self.s_user = Entry(root,width=15)
        self.s_user.pack()
        self.s_password = Entry(root,width=15,show="*")
        self.s_password.pack()
        self.user_n = self.s_user.get()
        self.password_n = self.s_password.get()
        signup_button = TButton(root,text='Sign Up',command=self.signup_user_check)
        signup_button.pack()
        signup_button.place(bordermode=OUTSIDE,x=110,y=55)
        # back = TButton(root,text='Back',command=self.back_signup)
        # back.pack()
        exit = TButton(root,text='Exit',command=self.ext)
        exit.pack()
        exit.place(bordermode=OUTSIDE,x=110,y=80)
        root.geometry("300x300")
        root.resizable(0,0)
        root.mainloop() # Add Clear Button For Ip Founder7
    def signup_user_check(self):
        global password_s,user_s
        time.sleep(0.25)
        user_s = open("username.txt","w")
        user_s.write(self.user_n)
        user_s.close()
        password_s = open("password.txt","w")
        password_s.write(self.password_n)
        password_s.close()
        time.sleep(1.5)
        self.x = True
        self.menu_attack()
    def login_check(self):
        user_f = open("username.txt","r").read()
        if user_f == user.get():
            password_f = open("password.txt","r").read()
            if password_f == password.get():
                self.menu_attack()
            else:
                showerror(title='Cannot Login',message='Please, Check Password!')
        else:
            showerror(title='Cannot Login',message='Please, Check User')
        return
    def back_login_menu(self):
        user.destroy()
        password.destroy()
        back.destroy()
        exit.destroy()
        login_button.destroy()
        self.root2.destroy()
        self.account()
    def menu_attack(self):
        global root,host,host_2,host_3,packet,scan,scan_2,scan_3,ipfounder,pingtest,portscanner
        root = Tk()
        root.title('Black-Attack')
        menu = Menu(root)
        account = Label(root,text=" ")
        account.pack(side = BOTTOM)
        if self.x == True:
            account.config(text=self.s_user.get())
        else:
            account.config(text=user.get())
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='Developer',command=self.dev)
        filemenu.add_command(label='Black',command=self.black)
        extfile = Menu(menu,tearoff=0)
        extfile.add_command(label='Quit',accelerator='Alt+F4',command=self.ext)
        menu.add_cascade(label='About',menu=filemenu)
        menu.add_cascade(label='Exit',menu=extfile)
        root.config(menu=menu)

        ch = Notebook(root)
        ipfounder = Frame(ch)
        pingtest = Frame(ch)
        portscanner = Frame(ch)
        info_v = Frame(ch)
        ch.add(ipfounder,text='Ip Founder')
        ch.add(pingtest,text='Ping Test')
        ch.add(portscanner,text='PortScan')
        ch.add(info_v,text='Info')
        ch.pack(expand=1,fill='both')
        txt_v = """
This Software Write By Mr.Programmer2938

Black-Attacker v2.0 Comming Soon!

"""
        info_label = Label(info_v,text=txt_v)
        info_label.pack()
        host = Entry(ipfounder,width=15)
        host.pack()
        host_3 = Entry(portscanner,width=15)
        host_3.pack()
        host_3.insert(0,"Host")
        host_2 = Entry(pingtest,width=15)
        host_2.pack()
        host_2.insert(0,"Host")
        packet = Entry(pingtest,width=15)
        packet.pack()
        packet.insert(0,"Packet")
        scan = Button(ipfounder,width=9,height=3,text='Scan',command=self.scan_ip)
        scan.pack(padx=10,pady=10)
        scan_2 = Button(pingtest,width=9,height=3,text='Scan',command=self.pingtest_m)
        scan_2.pack(padx=5,pady=5)
        scan_3 = Button(portscanner,width=9,height=3,text='Scan',command=self.portscan)
        scan_3.pack(padx=10,pady=10)
        root.geometry("500x400")
        root.resizable(0,0)
        root.mainloop()
    def clear_ip(self):
        host.delete(0,END)
    def portscan(self):
        all_port = {}
        ports = [21,22,23,25,80,111,443]
        for port in ports:
            s = socket.socket()
            ch = s.connect_ex((host.get(),port))
            if ch == 0:
                all_port[port] = 'open'
            else:
                all_port[port] = 'Filter'
        showinfo(title='PortScan',message=all_port.items())
        clear_3 = Button(portscanner,width=9,height=3,text='clear',command=self.clear_portscan)
        clear_3.pack()
    def clear_portscan(self):
        host_3.delete(0,END)
        host_3.insert(0,"Host")
    def pingtest_m(self):
        ping_run = subprocess.getoutput(f"ping -w {packet.get()} {host_2.get()}")
        showinfo(title='Ping Test',message=ping_run)
        scan_2.config(text='Try')
        clear_2 = Button(pingtest,width=9,height=3,text='clear',command=self.clear_pingtest)
        clear_2.pack()

    def clear_pingtest(self):
        host_2.delete(0,END)
        packet.delete(0,END)
        host_2.insert(0,"Host")
        packet.insert(0,"Packet")
    def scan_ip(self):
        showinfo(title='Ip',message=f'Ip: {socket.gethostbyname(host.get())}')
        scan.config(text='Try')

        clear = Button(ipfounder,width=9,height=3,text='clear',command=self.clear_ipfounder)
        clear.pack()
    def clear_ipfounder(self):
        host.delete(0,END)
        host.insert(0,"Host")
    def ipf(self):
        global host,scan_ip_b,back,exit
        ipfounder.destroy()
        pingtest.destroy()
        root.title('Black-Attack/IpFounder')
        host = Entry(root,width=15)
        host.pack()
        host.insert(0,"Host")
        host.place(bordermode=OUTSIDE,x=205,y=15)
        scan_ip_b = Button(root,text='Scan',width=9,height=3,command=self.scan_ip)
        scan_ip_b.pack()
        scan_ip_b.place(bordermode=OUTSIDE,x=215,y=100)
        back = TButton(root,text='Back',command=self.start_menu)
        back.pack()
        back.place(bordermode=OUTSIDE,x=400,y=345)
        exit = TButton(root,text='Exit',command=self.ext)
        exit.pack()
        exit.place(bordermode=OUTSIDE,x=315,y=345)

    def ext(self):
        quit()
    def black(self):
        webbrowser.open_new_tab('https://github.com/black-software-com')
    def dev(self):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def scan_ip(self):
        showinfo(title='Ip',message=f'Ip: {socket.gethostbyname(host.get())}')
        clear_ip = Button(ipfounder,width=9,height=3,text='Clear',command=self.clear_ip)
        clear_ip.pack()
if __name__ == '__main__':
    black = attack()
    black.account()
