from tkinter import *
import tkinter as tk

class Container(tk, Frame):
    def __init__(self, padre, controlador):
        super(). __init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg= "C6D9E3")