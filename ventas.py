from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Ventas(tk, Frame):
    def __init__(self, parent):
        super().__init__(parent) #1100, 650
        self.widgets()

        def widgets(self):

            frame1 = tkFrame(self, bg="addddddd", highligthbackground="gray", highlightthickness=1)
            frame1.pack()
            frame1.place(x=0 , y=0, width=1100, height=100)

            titulo = tk.Label(self, text="VENTAS", bg="addddddd" , font="sans 30 bold" , anchor="center")
            titulo.pack()
            titulo.place(x=5, y=0, width=1090, heiht=90)

            frame2 = tk.Frame(self, bg="#C6D9E3", highligthbackground="gray", highlightthickness=1)
            frame2.place(x=0, y=100, width=1100, height=550)