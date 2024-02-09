from customtkinter import *
import tkinter as tk
from tkinter import ttk


from windows import *
from data import Data
from widgets import Button, Label

size = 854, 480
padding = {"padx": 5, "pady": 5}

if __name__ == '__main__':
    root = CTk()

    Button.default("grid", padx=5, pady=5)
    Button.new_theme("grid", "left", sticky="w")

    Data.init()
    root.geometry(f"{size[0]}x{size[1]}")

    # [    ] [            ] [    ]
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=2)
    root.columnconfigure(3, weight=1)

    # ----------------------------------
    # ------------- Buttons ------------
    # ----------------------------------

    # Settings Button
    Button.create(root, {"text": "Settings", "command": create_settings_window},
                  {"row": 1, "column": 1}, "left")
    # Save Button
    Button.create(root, {"text": "Save", "command": Data.save},
                  {"row": 2, "column": 1}, "left")
    # Exit Button
    Button.create(root, {"text": "Exit", "command": Data.exit_app},
                  {"row": 3, "column": 1}, "left")

    # ----------------------------------
    # ------------- Labels -------------
    # ----------------------------------

    # Total paid
    Label.create(root, {"textvariable": Data.get_total_str()})

    CTkLabel(root).grid(row=1, column=3, **padding)

    root.mainloop()
