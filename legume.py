from typing import Self


class Vegetables():

    def __init__(self: Self, name_vegetable: str) -> None:
        self.name_vegetable = name_vegetable

    def __repr__(self: Self):
        print(self.name_vegetable)


class Vegetablebykg(Vegetables):
    def __init__(self: Self, name_vegetable: str, weight: float) -> None:
        super().__init__(name_vegetable)
        self.weight = weight

    def __repr__(self: Self):
        super().__repr__()
        print(self.weight)

    def weight_minus(self: Self, weight_minus) -> None:
        self.weight -= weight_minus
