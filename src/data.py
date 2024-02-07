import pickle as pk
from math import *


_individual: dict[str, int] = {}
_changes: list[str] = []
_total: int = 0
_target: int = 1000

_autosave: bool = False


def get_total() -> int:
    return _total


def get_total_str() -> str:
    string_total = str(_total)
    integer = string_total[:-2]
    decimal = string_total[-2:]

    if integer == "":
        integer = "0"

    return integer + ',' + decimal


def save() -> None:
    pass


def toggle_autosave(mode: bool = None) -> bool:
    global _autosave
    if mode is not None:
        _autosave = mode
        return mode

    _autosave = not _autosave
    return _autosave


def exit_app() -> None:
    if not _autosave:
        exit()

    save()
    exit()
