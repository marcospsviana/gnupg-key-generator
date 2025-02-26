from tkinter import ttk
from tkinter import Tk, PhotoImage

import gnupg
import tempfile
import os

import time

def get_name_gnupghome(entity):
    return f"{entity} {time.strftime('%Y-%m-%d')}"


def make_directories_name(entity):
    dest_current_key = ""
    try:
        os.makedirs(f"{os.path.expanduser("~")}/.gnugenerator", exist_ok=False)
    except FileExistsError:
        ...
    gpnupghome = get_name_gnupghome(entity)
    formated_name = "".join(gpnupghome.split())
    dest_current_key = f"{os.path.expanduser("~")}/.gnugenerator/{formated_name}"
    os.makedirs(dest_current_key, exist_ok=True)
    return dest_current_key


def generate_key_pair(type, size, alg, email, entity):
    
    dest_current_key = make_directories_name(entity=entity)
    real_name = get_name_gnupghome(entity=entity)
    gpg = gnupg.GPG(gnupghome=dest_current_key)
    gpg.encoding = 'utf-8'
    key_input = gpg.gen_key_input(
        name_real=real_name,
        name_email=f"{email}",
        key_type=type,
        key_length=size,
        subkey_type=type,
        subkey_length=size,
        expire_date=365,
        passphrase='passphrase'
    )
    key = gpg.gen_key(key_input)
    return key

root = Tk()
root.title("My App")
root.geometry("800x600")
main = ttk.Frame(root, padding=(5, 5, 12, 12))
main.grid(column=0, row=0)
logo_img = PhotoImage(file="assets/gnupgEncrypter.png")
logo = ttk.Label(main, image=logo_img)
logo.grid(column=0, row=0, columnspan=2)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()