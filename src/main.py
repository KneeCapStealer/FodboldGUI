from customtkinter import *
import tkinter as tk
from tkinter import ttk
import math
from CTkMessagebox import CTkMessagebox as MsgBox


from windows import *
from data import Data
from widgets import *

size = 854, 480
padding = {"padx": 5, "pady": 5}
button_font = ("Arial", 20)

tree: ttk.Treeview
root: CTk
data: Data


def sort_button():
    data.sort_individuals()
    repopulate_people_list(tree, data.get_individuals())


def add_member_button():
    def func(name: str) -> bool:
        if not data.add_member(name):
            return False

        repopulate_people_list(tree, data.get_individuals())
        data.update_values()
        return True

    create_new_member_window(func)


def make_payment_button():
    def func(name: str, payment: int) -> bool:
        if not data.register_payment(name, payment):
            return False

        repopulate_people_list(tree, data.get_individuals())
        data.update_values()
        return True

    names = list(data.get_individuals().keys())
    if len(names) == 0:
        MsgBox(root, 333, 222, "Payment Error",
               "There are no members added to this save",
               icon="cancel", sound=True)
        return

    tree_select_name = tree.item(tree.focus())["text"]
    create_payment_window(func, names, tree_select_name)


def remove_member_button():
    selected_name = tree.item(tree.focus())["text"]
    if selected_name == "":
        MsgBox(root, 333, 222, "Member Error",
               "You have not selected a member.\n"
               "Please select a member first.",
               icon="cancel", sound=True)

        return

    first_name = selected_name.split(" ", 1)[0]
    confirm = MsgBox(root, 360, 230, "Do you want to remove this member?",
                     f"Are you sure you want to remove {selected_name} from the participants?\n\n"
                     f"All of {selected_name}'s payments will be removed as well.",
                     icon="question", sound=False,
                     option_1=f"Remove {first_name}", option_2="Cancel")

    if confirm.get() == "Cancel":
        return

    if not data.remove_member(selected_name):
        MsgBox(root, 333, 222, "How?!",
               "The member you have selected doesn't exist.\n"
               "Just.. How did you manage to do that?",
               icon="cancel", sound=True)

    repopulate_people_list(tree, data.get_individuals())
    data.update_values()


if __name__ == '__main__':
    root = CTk()
    data = Data()

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
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#232323",
                    foreground="white", borderwidth=0, font=("", 15))
    style.configure("Treeview", fieldbackground="#2c2c2c",
                    background="#2c2c2c", foreground="white", font=("", 13))

    tree = ttk.Treeview(root, columns="DKK")
    tree.grid(row=1, column=3, rowspan=3, **padding)

    tree.heading("#0", text="Names", anchor="c")
    tree.heading("DKK", text="DKK", anchor="c")

    tree.column("#0", anchor="c")
    tree.column("DKK", anchor="c")

    repopulate_people_list(tree, data.get_individuals())

    # endregion

    # region Buttons

    # Settings Button
    Button.create(root, {"text": "Settings", "command": create_settings_window},
                  {"row": 1, "column": 1}, "left")
    # Save Button
    Button.create(root, {"text": "Save", "command": data.save},
                  {"row": 2, "column": 1}, "left")

    # Exit Button
    Button.create(root, {"text": "Exit", "command": exit},
                  {"row": 3, "column": 1}, "left")

    # Pay Button
    Button.create(root, {"text": "Make Payment", "command": make_payment_button},
                  {"row": 4, "column": 2})
    # Add Member Button
    Button.create(root, {"text": "Add Member", "command": add_member_button},
                  {"row": 5, "column": 2})
    # Remove Member Button
    Button.create(root, {"text": "Remove Member", "command": remove_member_button},
                  {"row": 6, "column": 2})
    # Sort Button
    Button.create(root, {"text": "Sort", "command": sort_button},
                  {"row": 4, "column": 3})

    # endregion

    # region Labels
    # ----------------------------------
    # ------------- Labels -------------
    # ----------------------------------

    # Total paid
    Label.create(root, {"textvariable": data.total_str},
                 {"row": 1, "column": 2}, "money")
    # Missing money
    Label.create(root, {"textvariable": data.difference_str},
                 {"row": 2, "column": 2}, "money")
    # Target money
    Label.create(root, {"textvariable": data.target_str},
                 {"row": 3, "column": 2}, "money")
    # endregion

    root.mainloop()
