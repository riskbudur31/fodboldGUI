# importing tkinter module
from tkinter import *
from tkinter import messagebox  # Import messagebox for showing errors

class worstWindowClass:
    def __init__(self, master):
        self.master = master  # reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("200x200")

        Label(self.worstWindow, text="De værste betalere").pack()

        ##TODO Error pop up besked
        #TODONE Error popup
        messagebox.showerror("Error", "Hov, denne del er ikke færdig")
