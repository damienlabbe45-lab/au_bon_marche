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
        if len(self.vegetable) > 0:
            for vegetable in self.vegetable:
                print(vegetable.__repr__())
        else:
            print("j'ai vendu tout mon stock")

    def sales_journey(self: Self, tickets: str) -> None:
        ticket = tickets.split("-")
        self.receipt.extend(ticket)
        self.monnaie += sum(float(item.split(":")[-1].strip())for item in ticket if item.strip() and ":" in item)
