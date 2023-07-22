import customtkinter
import os
from replay_parser import *
from customtkinter import filedialog
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title('Replay Parser')
root.geometry("400x200")

def select_file():
    path = filedialog.askopenfilename(title="Select an osu! replay file", filetypes=((".osr", "*.osr"),("All files", "*.*")))
    parser_file(path)

def select_folder():
    path = filedialog.askdirectory(title="Select a folder with .osr files")
    parser_folder(path)

widgets = customtkinter.CTkFrame(master=root)
widgets.pack(side = LEFT, padx=15, pady=15, expand=TRUE, fill=BOTH)

label = customtkinter.CTkLabel(master=widgets, text="Replay Parser", font=customtkinter.CTkFont(family="Roboto", size=24))
label.pack(pady=12, padx=10)

dir_button = customtkinter.CTkButton(master=widgets, text="Select File", command=select_file)
dir_button.pack(pady=12, padx=10)

dir_button = customtkinter.CTkButton(master=widgets, text="Select Folder", command=select_folder)
dir_button.pack(pady=12, padx=10)

root.mainloop()

