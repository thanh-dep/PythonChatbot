from tkinter import *
from customtkinter import *
import tkinter as tk 
frame = tk.Frame
frame.pack(fill="both", expand=True)
window =Tk()
window.title('ChatBot')
window.minsize(height=500,width=500)
Label1=Label(window,text='ChatBot',fg='pink',font=('cambria,18'),width=18).grid(row=0)
Label2=Label(window,text='Micro').grid(row=5,column=0)
Entry1=Entry(window,width=60).grid(row=0,column=2)
Button=CTkButton(window,width=10,text='Xoa',corner_radius = 32).grid(row=10,column=0)
mic_button = tk.Button(frame, text="Microphone") 
mic_button.pack(side="left", padx=6, pady=6) 

window.mainloop()