from legume import Vegetablebykg, Vegetableperpiece
from typing import Self
from customer import Customer


class Merchant:
    """classe pour vendre les fruits et légumes"""

    def __init__(self: Self, name: str, list_vegetable: list[Vegetableperpiece | Vegetablebykg]) -> None:
        self.name = name
        self.vegetable = list_vegetable
        self.receipt: list[Customer] = []
        self.monnaie: float = 0

    def offer(self: Self) -> None:
        for vegetable in self.vegetable:
            print(vegetable.__str__())

    def sold_vegetable(self: Self, vegetable_customer: Vegetableperpiece | Vegetablebykg, number: int | float,
                       customer:Customer) -> None:
        if isinstance(vegetable_customer, Vegetableperpiece):
            gold = vegetable_customer.piecepay(int(number))
            if vegetable_customer.unit == 0:
                self.vegetable.remove(vegetable_customer)
        elif isinstance(vegetable_customer, Vegetablebykg):
            gold = vegetable_customer.weightpay(number)
            if vegetable_customer.weight == 0:
                self.vegetable.remove(vegetable_customer)
        self.monnaie += gold
        self.receipt.append((customer.first_name, customer.last_name))

    def end_journey(self: Self) -> None:
        self.offer()
        print(f"j'ai gagné {self.monnaie} euros aujourd'hui!!!!!!!!! ^^")
        self.monnaie = 0
        print(f"j'ai eu {len(set(self.receipt))} pig... euh clients aujourd'hui ! '^^")





