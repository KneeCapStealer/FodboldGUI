from customtkinter import *
import tkinter as tk

from WindowManipulation import *


if __name__ == '__main__':
    root = CTk()
    root.geometry("720x480")

    CTkButton(root, command= lambda:print("Hello"), text="Button")\
        .grid(row=1, column=1, padx=5, pady=5)
    CTkButton(root, command=lambda: new_top_window(), text="new")\
        .grid(row=1, column=2, padx=5, pady=5)

    root.mainloop()