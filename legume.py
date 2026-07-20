from typing import Self


class Vegetables:
    """classe des fruits et légumes"""

    def __init__(self: Self, name_vegetable: str, price: float) -> None:
        """on initialise la classe avec son nom et son prix"""
        self.name_vegetable = name_vegetable
        self.price = price

    def __repr__(self: Self):
        """on indique pour le print, on fait juste son nom puis ensuite le prix"""
        print(self.name_vegetable)
        print(self.price)


class Vegetablebykg(Vegetables):
    """il s'agit des fruits et légumes qu'on met avec le poids"""

    def __init__(self: Self, name_vegetable: str, price, weight: float) -> None:
        """on appelle la méthode la classe mère puis ensuite, on rajoute le poids"""
        super().__init__(name_vegetable, price)
        self.weight = weight

    def __repr__(self: Self):
        """on appelle la méthode de la classe mère puis on rajoute le poids"""
        super().__repr__()
        print(self.weight)

    def weight_minus(self: Self, weight_minus: float) -> None:
        """la méthode permet de dimunier le poids. sera utile pour actualiser le poids si des clients en prend """
        self.weight -= weight_minus


class Vegetableperpiece(Vegetables):
    def __init__(self: Self, name_vegetable: str, price, unit: int) -> None:
        super().__init__(name_vegetable, price)
        self.unit = unit

    def __repr__(self: Self):
        super().__repr__()
        print(self.unit)

    def piece_minus(self: Self, piece_minus: int) -> None:
        self.unit -= piece_minus
