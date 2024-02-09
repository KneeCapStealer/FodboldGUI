import pickle as pk
from math import *
from customtkinter import *


class Data:
    _individuals: dict[str, int]
    _changes: list[str]
    _total: int
    _total_str: StringVar
    _target: int
    _target_str: StringVar

    _autosave: bool

    @staticmethod
    def init():
        Data._individuals = {}
        Data._changes = []

        Data._total = 0
        Data._target = 10000

        Data._total_str = StringVar()
        Data._total_str = StringVar()

    @staticmethod
    def get_total() -> int:
        return Data._total

    @staticmethod
    def get_total_str() -> StringVar:
        return Data._total_str

    @staticmethod
    def get_target_str() -> StringVar:
        return Data._total_str

    @staticmethod
    def update_values():
        Data._total = sum(Data._individuals.values())


    @staticmethod
    def save() -> None:
        pass

    @staticmethod
    def toggle_autosave(mode: bool = None) -> bool:
        if mode is not None:
            _autosave = mode
            return mode

        Data._autosave = not Data._autosave
        return Data._autosave

    @staticmethod
    def exit_app() -> None:
        if not Data._autosave:
            exit()

        Data.save()
        exit()
