# payWindow.py
from tkinter import *
from tkinter import messagebox
import pickle

class payWindowClass:
    def __init__(self, master):
        self.master = master
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")
#ToDO navnefunktion
#todone Navnefunktion
        Label(self.payWindow, text="Navn").pack()
        self.input_name = Entry(self.payWindow)
        self.input_name.pack()

        Label(self.payWindow, text="Indbetal").pack()
        self.input_amount = Entry(self.payWindow)
        self.input_amount.pack()

        self.button = Button(self.payWindow, text="Betal", command=self.registrer_betaling)
        self.button.pack()
#ToDo tilføjelse af pickle filen
#ToDone tilføjelse af pickle filen
#TODO betallingssystem
#ToDone betallingssystem
    def registrer_betaling(self):
        member = self.input_name.get()
        amount = float(self.input_amount.get())
        try:
            with open('betalinger.pk', 'rb') as file:
                data = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Fejl", "Filen blev ikke fundet!")
            return
        except Exception as e:
            messagebox.showerror("Fejl", f"Der opstod en fejl: {str(e)}")
            return

        if member in data:
            data[member] += amount
        else:
            messagebox.showerror("Fejl", f"Navnet '{member}' findes ikke.")
            return

        try:
            with open('betalinger.pk', 'wb') as file:
                pickle.dump(data, file)
        except Exception as e:
            messagebox.showerror("Fejl", f"Der opstod en fejl under skrivning til filen: {str(e)}")
            return

        messagebox.showinfo("Success", "Betalingsregistrering fuldført.")
        self.input_name.delete(0, END)
        self.input_amount.delete(0, END)
