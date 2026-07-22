from legume import Vegetablebykg, Vegetableperpiece
from typing import Self


class Merchant:
    """classe pour vendre les fruits et légumes"""

    def __init__(self: Self, name: str, list_vegetable: list[Vegetableperpiece | Vegetablebykg]) -> None:
        self.name = name
        self.vegetable = list_vegetable
        self.receipt: list[str] = []
        self.monnaie: float = 0
        self.sold: list[Vegetableperpiece | Vegetablebykg] = []

    def offer(self: Self) -> None:
        for vegetable in self.vegetable:
            print(vegetable.__repr__())



