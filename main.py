from tkinter import ttk
from tkinter import Tk, PhotoImage

import gnupg
import tempfile
import os

import time

def get_name_gnupghome(entity):
    return f"{entity} {time.strftime('%Y')}-{time.strftime('%H_%M_%S')}"


def generate_key_pair(type, size, alg):
    ...

root = Tk()
root.title("My App")
root.geometry("800x600")
# root.iconphoto(False, PhotoImage(file="icon.png"))  # Set the icon of the window
main = ttk.Frame(root, padding=(5, 5, 12, 12))
main.grid(column=0, row=0)
logo_img = PhotoImage(file="assets/gnupgEncrypter.png")
logo = ttk.Label(main, image=logo_img)
logo.grid(column=0, row=0, columnspan=2)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()