# importing tkinter module
from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow


class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger.. der er lige pt. vejarbejde her").pack()

        img = ImageTk.PhotoImage(Image.open("assets/img/vejarbejde1.png"))
        panel = Label(self.listWindow, image=img)
        panel.image = img
        panel.pack(side="bottom", fill="both", expand="yes")

        #TO DO: Her skulle der også laves en strukturetet liste af hvem der havde betalt og hvor meget det havde betalt
        # Der skulle også være et graf, så man kunne se hvor meget man manglede ud fra en cirkeldiagram