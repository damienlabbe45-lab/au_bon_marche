from legume import Vegetablebykg, Vegetableperpiece
from typing import Self
from customer import Customer


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

    def sold_vegetable(self: Self, vegetable_customer: Vegetableperpiece | Vegetablebykg, number: int | float,
                       customer:Customer) -> float:
        vegetable = self.vegetable.index(vegetable_customer)
        if isinstance(vegetable, Vegetableperpiece):
            gold = vegetable.piecepay(int(number))
        elif isinstance(vegetable, Vegetablebykg):
            gold = vegetable.weightpay(number)
        self.monnaie += gold
        self.sold.append(vegetable)
        return gold





