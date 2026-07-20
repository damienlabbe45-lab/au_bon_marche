from typing import Self


class Vegetables:
    """classe des fruits et légumes"""

    def __init__(self: Self, name_vegetable: str, price: float) -> None:
        """on initialise la classe avec son nom et son prix"""
        self.name_vegetable = name_vegetable
        self.price = price

    def __repr__(self: Self):
        """on indique pour le print, on fait juste son nom puis le prix"""
        return f"{self.name_vegetable} \n pour {self.price} euros"


class Vegetablebykg(Vegetables):
    """il s'agit des fruits et légumes qu'on met avec le poids"""

    def __init__(self: Self, name_vegetable: str, price, weight: float) -> None:
        """on appelle la méthode la classe mère puis, on rajoute le poids"""
        super().__init__(name_vegetable, price)
        self.weight = weight

    def __repr__(self: Self):
        """on ajoute le poids puis d'avant d'appeler la méthode de la classe mère"""
        return f"{self.weight} de {super().__repr__()}"

    def weight_minus(self: Self, weight_minus: float) -> None:
        """la méthode permet de diminuer le poids. Sera utile pour actualiser le poids si des clients en prennent """
        if self.weight >= weight_minus:
            self.weight -= weight_minus
        else:
            print(f"il me reste juste que {self.weight}.")

    def weightpay(self: Self, weight: float) -> float | None:
        number_weight = self.weight
        self.weight_minus(weight)
        if number_weight > weight:
            return self.price * weight
        return None


class Vegetableperpiece(Vegetables):
    """on appelle la méthode la classe mère puis on ajoute le nombre d'unités"""

    def __init__(self: Self, name_vegetable: str, price, unit: int) -> None:
        super().__init__(name_vegetable, price)
        self.unit = unit

    def __repr__(self: Self):
        """on met le nombre d'unités puis on appelle la classe mère"""
        return f"{self.unit} {super().__repr__()}"

    def piece_minus(self: Self, piece_minus: int) -> None:
        """méthode pour diminuer le nombre d'unités. Utile pour actualiser le nombre de pieces si des clients en achète
        """
        if self.unit >= piece_minus:
            self.unit -= piece_minus
        else:
            print(f"je n'ai pas assez de d'unités. j'en ai que {self.unit}")

    def piecepay(self: Self, piece: int) -> float | None:
        number_piece = self.unit
        self.piece_minus(piece)
        if number_piece > piece:
            return self.price * piece
        return None
