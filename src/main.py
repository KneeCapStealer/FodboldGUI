from customtkinter import *
import tkinter as tk

from windows import *
import data

size = 854, 480

if __name__ == '__main__':
    root = CTk()
    root.geometry(f"{size[0]}x{size[1]}")

    # [    ] [            ] [    ]
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=5000)
    root.columnconfigure(3, weight=1)

    # ----------------------------------
    # ------------- Buttons ------------
    # ----------------------------------

    # Settings Button
    CTkButton(root, text="Settings", command=create_settings_window)\
        .grid(row=1, column=1, padx=5, pady=5, sticky="w")
    # Save Button
    CTkButton(root, text="Save", command=data.save)\
        .grid(row=2, column=1, padx=5, pady=5, sticky="w")
    # Exit Button
    CTkButton(root, text="Exit", command=data.exit_app)\
        .grid(row=3, column=1, padx=5, pady=5, sticky="w")

    # ----------------------------------
    # ------------- Labels -------------
    # ----------------------------------

    # Total paid
    CTkLabel(root, text=data.get_total_str() + " DKK")\
        .grid(row=1, column=2, padx=5, pady=5)

    CTkLabel(root).grid(row=1, column=3, padx=5, pady=5)


    root.mainloop()
