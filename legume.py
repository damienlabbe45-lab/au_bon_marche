from typing import Self

class Vegetables():
    def __init__(self:Self, name_vegatble : str) -> None:
        self.name_vegatble = name_vegatble

    def __repr__(self:Self):
        print(self.name_vegatble)