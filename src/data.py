import pickle as pk
from math import *
from customtkinter import *


class Data:
    _pkData: dict[str, any]
    _pickler: pk.Pickler
    _unpickler: pk.Unpickler

    _individuals: dict[str, int]
    _sort_reversed: bool

    _changes: list[str]
    _total: int
    _total_str: StringVar

    _target: int
    _target_str: StringVar

    _difference_str: StringVar

    _autosave: bool

    def __init__(self):
        self._individuals = {"Name Nameson": 200,
                             "Jone Joneson": 300,
                             "Bone Bonerson": 10}

        self._sort_reversed = False
        self._changes = []

        self._total = 0
        self._target = 10000

        self._total_str = StringVar()
        self._target_str = StringVar()
        self._difference_str = StringVar()

        self._autosave = False

        self.sort_individuals()
        self.update_values()

    def get_total(self) -> int:
        return self._total

    def get_total_str(self) -> StringVar:
        return self._total_str

    def get_target_str(self) -> StringVar:
        return self._target_str

    def get_difference_str(self) -> StringVar:
        return self._difference_str

    def get_individuals(self) -> dict:
        return self._individuals.copy()

    def sort_individuals(self) -> dict:
        self._individuals = dict(sorted(self._individuals.items(), key=lambda x: x[1], reverse=self._sort_reversed))
        self._sort_reversed = not self._sort_reversed
        return self._individuals

    def update_values(self):
        self._total = sum(self._individuals.values())
        total_str = str(self._total)
        target_str = str(self._target)
        difference = self._target - self._total
        difference_str = str(difference)

        self._total_str.set(f"{total_str[:-2] if self._total > 1 else '0'},{total_str[-2:]} DKK")
        self._target_str.set(f"{target_str[:-2] if self._target > 1 else '0'},{target_str[-2:]} DKK")
        self._difference_str.set(f"{difference_str[:-2] if difference > 1 else '0'},{difference_str[-2:]} DKK")

    def save(self) -> None:
        pass

    def toggle_autosave(self, mode: bool = None) -> bool:
        if mode is not None:
            self._autosave = mode
            return mode

        self._autosave = not self._autosave
        return self._autosave

    def exit(self) -> None:
        if not self._autosave:
            exit()

        self.save()
        exit()
