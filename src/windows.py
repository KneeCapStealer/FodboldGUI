from customtkinter import *


def new_top_window(size: tuple[int, int]=(854, 480),
                   title: str="New Window") -> CTkToplevel:
    win = CTkToplevel()
    win.geometry(f"{size[0]}x{size[1]}")
    win.title(title)
    win.attributes("-topmost", 1)
    return win


def create_settings_window() -> CTkToplevel:
    win = new_top_window(title="Settings")

    return win
