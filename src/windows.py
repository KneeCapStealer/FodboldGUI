from customtkinter import *
from widgets import *
from collections.abc import Callable
from CTkMessagebox import CTkMessagebox as MsgBox

from data import Data

padding = {"padx": 10, "pady": 10}


def create_top_window(size: tuple[int, int] = (854, 480),
                      title: str = "New Window") -> CTkToplevel:
    win = CTkToplevel()
    win.geometry(f"{size[0]}x{size[1]}")
    win.title(title)
    win.attributes("-topmost", 1)

    return win


def create_settings_window(data: Data) -> CTkToplevel:
    win = create_top_window(title="Settings")

    autosave_switch: CTkSwitch
    datafile_entry: CTkEntry

    def autosave_func():
        data.toggle_autosave(bool(autosave_switch.get()))

    autosave_switch = CTkSwitch(win, text="Autosave", command=autosave_func)
    autosave_switch.pack(side=LEFT, **padding)

    datafile_entry = CTkEntry(win, placeholder_text=data.get_datafile())
    datafile_entry.pack(side=LEFT, **padding)

    def load_datafile():
        data.change_datafile(datafile_entry.get())

    CTkButton(win, text="Load", command=load_datafile).pack(side=LEFT, **padding)

    return win


def create_new_member_window(
        confirm_command: Callable[[str], bool]) -> CTkToplevel:
    win = create_top_window((550, 280), "New Member")
    name_var = StringVar()

    win.columnconfigure(1, weight=1)
    win.columnconfigure(3, weight=1)
    win.columnconfigure(2, weight=2)

    win.rowconfigure(1, weight=2)
    win.rowconfigure(2, weight=3)
    win.rowconfigure(3, weight=1)

    Label.create(win, {"text": "Add New Member", "font": ("impact", 28)},
                 {"row": 1, "column": 2})

    entry = CTkEntry(win, 264, 64, placeholder_text="Member Name Here",
                     textvariable=name_var, font=("impact", 18))
    entry.grid(row=2, column=2)
    entry.focus()

    def confirm_func() -> None:
        name = name_var.get()
        if name == "":
            win.destroy()
            return

        if not confirm_command(name):
            msg_win = MsgBox(title="Name Error", icon="warning",
                             message="Name already exists, try again?",
                             option_1="Try Again", option_2="Cancel",
                             sound=True)
            msg_win.bell()

            match msg_win.get():
                case "Cancel":
                    win.destroy()
                case "Try Again":
                    msg_win.destroy()
                    name_var.set("")

            return

        win.destroy()

    Button.create(win, {"text": "Confirm", "width": 128,
                        "command": confirm_func},
                  {"row": 3, "column": 3})

    Button.create(win, {"text": "Cancel", "width": 128,
                        "command": win.destroy},
                  {"row": 3, "column": 1})

    win.grab_set()

    win.bind("<Return>", lambda e: confirm_func())

    return win


def create_payment_window(confirm_command: Callable[[str, int], bool],
                          tree_data: list[str],
                          default_pick: str = "") -> CTkToplevel:
    win = create_top_window((333, 220), "Payment Window")

    default_pick = default_pick if default_pick != "" else tree_data[0]
    selected = StringVar(value=default_pick)
    payment_amount = StringVar(value="")

    CTkEntry(win, textvariable=payment_amount)\
        .pack(side=TOP, padx=15, pady=5)

    CTkOptionMenu(win, values=tree_data, variable=selected) \
        .pack(side=TOP, padx=15, pady=5)

    def confirm_func() -> None:
        decimal_marker = None
        payment_string = payment_amount.get().strip()
        if "," in payment_string:
            decimal_marker = ","
        elif "." in payment_string:
            decimal_marker = "."

        multiplier: int = 100
        if decimal_marker is not None:
            multiplier = 1
            decimal_count: int = len(payment_string.split(decimal_marker, 1)[1])
            if decimal_count > 2:
                err = MsgBox(win, title="Incorrect number", icon="warning",
                             message=f"There are {decimal_count} decimal places"
                                     "\nThe supported amount is 2\nTry Again?",
                             option_1="Try Again", option_2="Cancel",
                             sound=True)

                match err.get():
                    case "Cancel":
                        win.destroy()
                    case "Try Again":
                        payment_amount.set("")
                        err.destroy()

                return

            payment_string = payment_string[:-3] + payment_string[-2:]

        if not payment_string.isdigit():
            err = MsgBox(win, title="Incorrect number", icon="warning",
                         message=f"The number {payment_amount.get()}"
                                 " is not valid\nTry Again?",
                         option_1="Try Again", option_2="Cancel",
                         sound=True)

            match err.get():
                case "Cancel":
                    win.destroy()
                case "Try Again":
                    payment_amount.set("")
                    err.destroy()

            return

        payment_number = int(payment_string) * multiplier

        confirm_command(selected.get(), payment_number)
        win.destroy()

    CTkButton(win, text="Confirm Payment", command=confirm_func)\
        .pack(side=RIGHT, fill=BOTH, padx=15, pady=15)

    CTkButton(win, text="Cancel Payment", command=win.destroy)\
        .pack(side=LEFT, fill=BOTH, padx=15, pady=15)

    win.bind("<Return>", lambda e: confirm_func())

    return win
