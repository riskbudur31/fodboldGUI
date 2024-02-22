# worstWindow.py
from tkinter import *
from tkinter import messagebox  # Import messagebox for showing errors

class worstWindowClass:
    def __init__(self, master, fodboldtur):
        self.master = master  # reference til main window objektet
        self.fodboldtur = fodboldtur
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("200x200")

        Label(self.worstWindow, text="Under arbejde").pack()

        ##TODO Error pop up besked
        #TODONE Error popup
        messagebox.showerror("Error", "Hov, denne del er ikke færdig")
        #ToDO en funktion for at finde de specifikke personer
        #ToDO en funktion til at se hvem der har betalt mindst