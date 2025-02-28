from tkinter import ttk
from tkinter import Tk, PhotoImage

import gnupg
import tempfile
import os

import time
import string
import random


def generate_pass(pass_lenght: int) -> string:
    password = ""
    list_chars = f"{string.ascii_letters}{string.digits}{string.punctuation}".replace("\"", "").replace("/", "")
    for _ in range(pass_lenght):
        password += random.choice(list_chars)
    return password




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


def generate_key_pair(type, size, alg, email, entity, len_pass):
    
    dest_current_key = make_directories_name(entity=entity)
    real_name = get_name_gnupghome(entity=entity)
    gpg = gnupg.GPG(gnupghome=dest_current_key)
    gpg.encoding = 'utf-8'
    passphrase = generate_pass(len_pass)
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
logo.grid(column=0, row=0, columnspan=10)
# root.columnconfigure(0, weight=2)
# root.rowconfigure(0, weight=2)

frame_entries = ttk.Frame(master=main, width=120, padding=0).grid(column=0, row=1, padx=10, pady=10)

label_entity = ttk.Label(master=frame_entries, text="Real Name", width=10).grid(column=0, row=1, padx=2, pady=10, columnspan=1, sticky="E")
input_entity = ttk.Entry(master=frame_entries, width=20, justify="left").grid(column=1, row=1, padx=10, pady=10, columnspan=1, sticky="WE")

label_alg = ttk.Label(master=frame_entries, text="Algorithm", width=10).grid(column=2, row=1, padx=2, pady=10, columnspan=1)
input_alg = ttk.Entry(master=frame_entries, width=25).grid(column=3, row=1, padx=1, pady=10, columnspan=2, sticky="EW")

label_entity = ttk.Label(master=frame_entries, text="Passphrase", width=10).grid(column=0, row=3, padx=10, pady=10, sticky="E")
input_entity = ttk.Entry(master=frame_entries, width=100).grid(column=1, row=3, padx=10, pady=10)
input_entity = ttk.Button(master=frame_entries, width=16, text="Generate Pasphrase", style="").grid(column=2, row=3, padx=10, pady=10)


root.mainloop()