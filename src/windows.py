from customtkinter import *
from widgets import *
from collections.abc import Callable

padding = {"padx": 10, "pady": 10}

def create_top_window(size: tuple[int, int] = (854, 480),
                      title: str = "New Window") -> CTkToplevel:
    win = CTkToplevel()
    win.geometry(f"{size[0]}x{size[1]}")
    win.title(title)
    win.attributes("-topmost", 1)

    return win


def create_error_window(message: str = "Error") -> CTkToplevel:
    win = create_top_window((128, 128), "ERROR")
    CTkLabel(win, text=message, font=("", 26)).pack()

    return win


def create_settings_window() -> CTkToplevel:
    win = create_top_window(title="Settings")
    CTkLabel(win, text="Bruda").pack()

    return win


def create_new_member_window(confirm_command: Callable[[str], any]) -> CTkToplevel:
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

    CTkEntry(win, 264, 64, placeholder_text="Member Name Here",
             textvariable=name_var, font=("impact", 18))\
        .grid(row=2, column=2)

    def confirm_func():
        confirm_command(name_var.get())
        win.destroy()

    Button.create(win, {"text": "Confirm", "width": 128,
                        "command": confirm_func},
                  {"row": 3, "column": 3})

    Button.create(win, {"text": "Cancel", "width": 128,
                        "command": win.destroy},
                  {"row": 3, "column": 1})

    win.grab_set()

    return win
