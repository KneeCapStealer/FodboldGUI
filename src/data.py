import pickle as pk
from math import *
from customtkinter import *


class Data:
    _individuals: dict[str, int]
    _sort_reversed: bool

    _changes: list[str]
    _total: int
    _total_str: StringVar

    _target: int
    _target_str: StringVar

    _difference_str: StringVar

    _autosave: bool

    @staticmethod
    def init():
        Data._individuals = {"Name Nameson": 200,
                             "Jone Joneson": 300,
                             "Bone Bonerson": 10}
        Data._sort_reversed = False
        Data._changes = []

        Data._total = 0
        Data._target = 10000

        Data._total_str = StringVar()
        Data._target_str = StringVar()
        Data._difference_str = StringVar()

        Data._autosave = False

        Data.sort_individuals()
        Data.update_values()

    @staticmethod
    def get_total() -> int:
        return Data._total

    @staticmethod
    def get_total_str() -> StringVar:
        return Data._total_str

    @staticmethod
    def get_target_str() -> StringVar:
        return Data._target_str

    @staticmethod
    def get_difference_str() -> StringVar:
        return Data._difference_str

    @staticmethod
    def get_individuals() -> dict:
        return Data._individuals.copy()

    @staticmethod
    def sort_individuals() -> dict:
        Data._individuals = dict(sorted(Data._individuals.items(), key=lambda x: x[1], reverse=Data._sort_reversed))
        Data._sort_reversed = not Data._sort_reversed
        return Data._individuals

    @staticmethod
    def update_values():
        Data._total = sum(Data._individuals.values())
        total_str = str(Data._total)
        target_str = str(Data._target)
        difference = Data._target - Data._total
        difference_str = str(difference)

        Data._total_str.set(f"{total_str[:-2] if Data._total > 1 else '0'},{total_str[-2:]} DKK")
        Data._target_str.set(f"{target_str[:-2] if Data._target > 1 else '0'},{target_str[-2:]} DKK")
        Data._difference_str.set(f"{difference_str[:-2] if difference > 1 else '0'},{difference_str[-2:]} DKK")

    @staticmethod
    def save() -> None:
        pass

    @staticmethod
    def toggle_autosave(mode: bool = None) -> bool:
        if mode is not None:
            Data._autosave = mode
            return mode

        Data._autosave = not Data._autosave
        return Data._autosave

    @staticmethod
    def exit() -> None:
        if not Data._autosave:
            exit()

        Data.save()
        exit()
