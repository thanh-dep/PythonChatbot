from tkinter import *
import tkinter as tk 
window = Tk ()
window.title ('ChatBot')
window.geometry('800x800')
micro_icon  = PhotoImage(file = 'd:\Thanh_PyThon\mircoicon.png')
logo_path = PhotoImage(file = 'd:\Thanh_PyThon\logo.png')
send_icon = PhotoImage(file = 'd:\Thanh_PyThon\sendicon.png')
title_label = Label(window,text='ChatBot',fg='pink',font=('cambria',50),width = 16).place(x = 50, y = 0)
entry_histroy = Entry(window,bg ='#FFFF99').place(x = 30,y = 100,height=500,width=700)
entry_command = Entry(window,bg ='#FFFFCC').place(x = 30,y = 600,height=100,width=500)
buton_send = Button(window,image=send_icon,bg ='#0066FF',text = 'SEND').place(x = 530, y = 600,height=100,width=100)
buton_listen = Button(window,image=micro_icon,bg='#00FFFF',text= 'LISTEN').place(x = 630,y = 600,height=100,width=100)
window.iconphoto(False,logo_path)

window.mainloop()