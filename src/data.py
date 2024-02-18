import pickle as pk
from math import *
from customtkinter import *
import os

GLOBAL_SETTINGS_FILE = "data/settings.pk"


class Data:
    _pkSettings: dict[str, any]
    _pkData: dict[str, any]
    _pickler: pk.Pickler

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

        if os.path.isfile(GLOBAL_SETTINGS_FILE):
            self._pkSettings = pk.load(open(GLOBAL_SETTINGS_FILE, "rb"))
            self._datafile_name = self._pkSettings["datafile"]
        else:
            # Init settings file
            self._datafile_name = "data.pk"
            self._pkSettings = {"datafile": self._datafile_name}

            settings_file = open(GLOBAL_SETTINGS_FILE, "wb")
            pk.dump(self._pkSettings, file=settings_file,
                    protocol=pk.HIGHEST_PROTOCOL)

        if os.path.isfile(f"data/{self._datafile_name}"):
            self._pkData = pk.load(open(f"data/{self._datafile_name}", "rb"))
            self._pickler = pk.Pickler(open(f"data/{self._datafile_name}", "wb"),
                                       protocol=pk.HIGHEST_PROTOCOL)

            self._sort_reversed = self._pkData["sort_reversed"]
            self._autosave = self._pkData["autosave"]

            self._individuals = self._pkData["individuals"]
            self._target = self._pkData["target"]
            self.update_values()

        else:
            # Init data file
            self._sort_reversed = False
            self._autosave = False

            self._individuals = {}
            self._total = 0
            self._target = 10000

            self._pkData = {"sort_reversed": self._sort_reversed,
                            "autosave": self._autosave,
                            "individuals": self._individuals,
                            "target": self._target}

            self.update_values()
            self._pkData["total"] = self._total

            self._pickler = pk.Pickler(open(f"data/{self._datafile_name}", "wb"),
                                       protocol=pk.HIGHEST_PROTOCOL)

        self.sort_individuals()

        self._changes = []
        self.save()

    def get_total(self) -> int:
        return self._total

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

        self.total_str.set(f"{total_str[:-2] if self._total > 1 else '0'},{total_str[-2:]} DKK")
        self.target_str.set(f"{target_str[:-2] if self._target > 1 else '0'},{target_str[-2:]} DKK")
        self.difference_str.set(f"{difference_str[:-2] if difference > 1 else '0'},{difference_str[-2:]} DKK")

    def save(self) -> None:
        self._pickler.dump(self._pkData)

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
