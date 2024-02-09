from customtkinter import *
from typing import Literal
from tkinter import ttk


class Button:
    _button_opts: dict[str, any] = {}
    _button_themes: dict[str, dict[str, any]] = {}

    _grid_opts: dict[str, any] = {}
    _grid_themes: dict[str, dict[str, any]] = {}

    @staticmethod
    def default(theme_type: Literal["button", "grid"], **kwargs):
        if theme_type == "button":
            opts = Button._button_opts
        elif theme_type == "grid":
            opts = Button._grid_opts
        else:
            exit("U did dum dum")

        for key, val in kwargs.items():
            opts[key] = val

    @staticmethod
    def new_theme(theme_type: Literal["button", "grid"], name: str, **kwargs):
        match theme_type:
            case "button":
                theme = Button._button_themes
            case "grid":
                theme = Button._grid_themes

        theme[name] = kwargs

    @staticmethod
    def create(root, button_args: dict[str, any]=None, grid_args: dict[str, any]=None, theme: str=None) -> CTkButton:
        button_opts = Button._button_opts.copy()
        grid_opts = Button._grid_opts.copy()
        if theme is not None:
            if theme in Button._button_themes.keys():
                for key, val in Button._button_themes[theme].items():
                    button_opts[key] = val

            if theme in Button._grid_themes.keys():
                for key, val in Button._grid_themes[theme].items():
                    grid_opts[key] = val

        if button_args is not None:
            for key, val in button_args.items():
                button_opts[key] = val

        if grid_args is not None:
            for key, val in grid_args.items():
                grid_opts[key] = val

        button = CTkButton(root, **button_opts)
        button.grid(**grid_opts)
        return button


class Label:
    _label_opts: dict[str, any] = {}
    _label_themes: dict[str, dict[str, any]] = {}

    _grid_opts: dict[str, any] = {}
    _grid_themes: dict[str, dict[str, any]] = {}

    @staticmethod
    def default(theme_type: Literal["button", "grid"], **kwargs):
        if theme_type == "button":
            opts = Label._label_opts
        elif theme_type == "grid":
            opts = Label._grid_opts
        else:
            exit("U did dum dum")

        for key, val in kwargs.items():
            opts[key] = val

    @staticmethod
    def new_theme(theme_type: Literal["label", "grid"], name: str, **kwargs):
        match theme_type:
            case "label":
                theme = Label._label_themes
            case "grid":
                theme = Label._grid_themes
            case _:
                # this will never happen
                theme = {}

        theme[name] = kwargs

    @staticmethod
    def create(root, button_args: dict[str, any]=None, grid_args: dict[str, any]=None, theme: str=None) -> CTkLabel:
        label_opts = Label._label_opts.copy()
        grid_opts = Label._grid_opts.copy()
        if theme is not None:
            if theme in Label._label_themes.keys():
                for key, val in Label._label_themes[theme].items():
                    label_opts[key] = val

            if theme in Label._grid_themes.keys():
                for key, val in Label._grid_themes[theme].items():
                    grid_opts[key] = val

        if button_args is not None:
            for key, val in button_args.items():
                label_opts[key] = val

        if grid_args is not None:
            for key, val in grid_args.items():
                grid_opts[key] = val

        label = CTkLabel(root, **label_opts)
        label.grid(**grid_opts)
        return label


def repopulate_people_list(treeview: ttk.Treeview, people: dict[str, int]):
    treeview.delete(*treeview.get_children())

    for name, money in people.items():
        value = f"{str(money)[:-2] if money >= 100 else '0'},{str(money)[-2:]} kr"
        treeview.insert("", "end", text=name, values=(value,))
