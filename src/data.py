import pickle as pk
from math import *
from customtkinter import *
import os

GLOBAL_SETTINGS_FILE = "data/settings.pk"


class Data:
    _pkSettings: dict[str, any]
    _pkData: dict[str, any]

    _datafile_name: str

    _individuals: dict[str, int]
    _sort_reversed: bool

    _changes: list[str]
    _total: int
    total_str: StringVar

    _target: int
    target_str: StringVar

    difference_str: StringVar

    _autosave: bool

    def __init__(self):
        self.total_str = StringVar()
        self.target_str = StringVar()
        self.difference_str = StringVar()
        self._changes = []

        if os.path.isfile(GLOBAL_SETTINGS_FILE):
            self._pkSettings = pk.load(open(GLOBAL_SETTINGS_FILE, "rb"))
            self._datafile_name = self._pkSettings["datafile"]
        else:
            # Init settings file
            self._datafile_name = "data.pk"
            self._pkSettings = {"datafile": self._datafile_name}

            pk.dump(self._pkSettings, open(GLOBAL_SETTINGS_FILE, "wb"),
                    protocol=pk.HIGHEST_PROTOCOL)

        if os.path.isfile(f"data/{self._datafile_name}"):
            self._pkData = pk.load(open(f"data/{self._datafile_name}", "rb"))

            self._sort_reversed = self._pkData["sort_reversed"]
            self._autosave = self._pkData["autosave"]

            self._individuals = self._pkData["individuals"]
            self._target = self._pkData["target"]

        else:
            # Init data file
            self._sort_reversed = False
            self._autosave = False

            self._individuals = {}
            self._target = 4500 * 100

            self._pkData = {"sort_reversed": self._sort_reversed,
                            "autosave": self._autosave,
                            "individuals": self._individuals,
                            "target": self._target}

        self.sort_individuals()
        self.update_values()

        self.save()

    def get_total(self) -> int:
        return self._total

    def get_individuals(self) -> dict:
        return self._individuals.copy()

    def sort_individuals(self) -> None:
        self._individuals = dict(sorted(self._individuals.items(), key=lambda x: x[1], reverse=self._sort_reversed))
        self._sort_reversed = not self._sort_reversed

    def update_values(self):
        self._total = sum(self._individuals.values())
        total_str = str(self._total)
        target_str = str(self._target)
        difference = self._target - self._total
        difference_str = str(difference)

        self.total_str.set(f"{total_str[:-2] if self._total > 1 else '0'},{total_str[-2:]} DKK")
        self.target_str.set(f"{target_str[:-2] if self._target > 1 else '0'},{target_str[-2:]} DKK")
        self.difference_str.set(f"{difference_str[:-2] if difference > 1 else '0'},{difference_str[-2:]} DKK")

    def add_member(self, name: str) -> bool:
        if name in self._individuals.keys():
            return False

        self._individuals[name] = 0
        return True

    def remove_member(self, name: str) -> bool:
        if name not in self._individuals.keys():
            return False

        del self._individuals[name]
        return True

    def register_payment(self, name: str, payment: int) -> bool:
        if name not in self._individuals.keys():
            return False

        self._individuals[name] += payment
        return True

    def get_datafile(self) -> str:
        return self._datafile_name

    def change_datafile(self, filename: str) -> None:
        self._datafile_name = filename
        self._pkSettings["datafile"] = filename

        self._load()
        pk.dump(self._pkSettings, open(GLOBAL_SETTINGS_FILE, "wb"), pk.HIGHEST_PROTOCOL)


    def save(self) -> None:
        self._pkData["individuals"] = self._individuals
        self._pkData["target"] = self._target
        self._pkData["autosave"] = self._autosave

        pk.dump(self._pkData, open(f"data/{self._datafile_name}", "wb"), pk.HIGHEST_PROTOCOL)

    def _load(self) -> None:
        if self._autosave:
            self.save()

        self._pkData = pk.load(open(f"data/{self._datafile_name}", "rb"))
        self._individuals = self._pkData["individuals"]
        self._target = self._pkData["target"]
        self._autosave = self._pkData["autosave"]

    def toggle_autosave(self, mode: bool = None) -> bool:
        if mode is not None:
            self._autosave = mode
            return mode

        self._autosave = not self._autosave
        return self._autosave

    def __del__(self) -> None:
        if self._autosave:
            self.save()
