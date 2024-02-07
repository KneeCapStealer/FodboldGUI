from customtkinter import *


def new_top_window(size: tuple[int, int]=(854, 480),
                   title: str="New Window") -> CTkToplevel:
    window = CTkToplevel()
    window.geometry(f"{size[0]}x{size[1]}")
    window.title(title)
    window.attributes("-topmost", 1)
    return window

