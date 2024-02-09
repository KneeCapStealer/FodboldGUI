from customtkinter import *
import tkinter as tk
from tkinter import ttk
import math


from windows import *
from data import Data
from widgets import *

size = 854, 480
padding = {"padx": 5, "pady": 5}
button_font = ("Arial", 20)

if __name__ == '__main__':
    root = CTk()
    Data.init()

    # region Setup
    Button.default("button", width=256, height=64, font=button_font)
    Button.default("grid", **padding)
    Button.new_theme("grid", "left", sticky="w")

    Label.default("grid", padx=10, pady=15)
    Label.new_theme("label", "money", font=("Impact", 20))

    root.geometry(f"{size[0]}x{size[1]}")

    # [    ] [            ] [    ]
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=2)
    root.columnconfigure(3, weight=1)

    # endregion

    # region People List
    # ----------------------------------
    # ---------- People List -----------
    # ----------------------------------
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#232323", foreground="white", borderwidth=0, font=("", 15))
    style.configure("Treeview", fieldbackground="#2c2c2c", background="#2c2c2c", foreground="white", font=("", 13))

    tree = ttk.Treeview(root, columns="DKK")
    tree.grid(row=1, column=3, rowspan=3, **padding)

    tree.heading("#0", text="Names", anchor="c")
    tree.heading("DKK", text="DKK", anchor="c")

    tree.column("#0", anchor="c")
    tree.column("DKK", anchor="c")

    repopulate_people_list(tree, Data.get_individuals())

    # endregion

    # region Buttons
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
    Button.create(root, {"text": "Exit", "command": Data.exit},
                  {"row": 3, "column": 1}, "left")

    # Pay Button
    Button.create(root, {"text": "Make Payment", "command": None},
                  {"row": 4, "column": 2})
    # Add Member Button
    Button.create(root, {"text": "Add Member", "command": None},
                  {"row": 5, "column": 2})
    # Remove Member Button
    Button.create(root, {"text": "Remove Member", "command": None},
                  {"row": 6, "column": 2})
    # Sort Button
    Button.create(root, {"text": "Sort", "command": lambda: repopulate_people_list(tree, Data.sort_individuals())},
                  {"row": 4, "column": 3})

    # endregion

    # region Labels
    # ----------------------------------
    # ------------- Labels -------------
    # ----------------------------------

    # Total paid
    Label.create(root, {"textvariable": Data.get_total_str()},
                 {"row": 1, "column": 2}, "money")
    # Missing money
    Label.create(root, {"textvariable": Data.get_difference_str()},
                 {"row": 2, "column": 2}, "money")
    # Target money
    Label.create(root, {"textvariable": Data.get_target_str()},
                 {"row": 3, "column": 2}, "money")
    # endregion

    root.mainloop()
