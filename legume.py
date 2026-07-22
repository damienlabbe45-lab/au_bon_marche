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
        return f"{self.weight} kg de {super().__repr__()}"

    def weight_minus(self: Self, weight_minus: float) -> None:
        """la méthode permet de diminuer le poids. Sera utile pour actualiser le poids si des clients en prennent """
        if self.weight >= weight_minus:
            self.weight -= weight_minus
        else:
            print(f"il me reste juste que {self.weight}.")

    def weightpay(self: Self, weight: float) -> float | None:
        """fonction servant à définir ce qu'il faut payer pour un fruit et légume en fonction du poids"""
        number_weight = self.weight
        self.weight_minus(weight)
        if number_weight > weight:
            return self.price * weight
        return None


class Vegetableperpiece(Vegetables):
    """il s'agit des fruits et légumes qu'on met avec le nombre d'unités qu'on a"""
    def __init__(self: Self, name_vegetable: str, price, unit: int) -> None:
        """"on appelle la méthode la classe mère puis on ajoute le nombre d'unités"""
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
        """fonction servant à définir ce qu'il faut payer pour un fruit et légume en fonction du nombre
        d'unité qu'on a pris"""
        number_piece = self.unit
        self.piece_minus(piece)
        if number_piece > piece:
            return self.price * piece
        return None


def init_vegetables() -> list[Vegetablebykg | Vegetableperpiece]:
    """initialise les fruits et légumes"""
    return [
        Vegetablebykg("Clémentine", 2.90, 6),
        Vegetablebykg("Datte", 7.00, 4),
        Vegetablebykg("Grenade", 3.5, 3),
        Vegetablebykg("Kaki", 4.50, 3),
        Vegetablebykg("Kiwi", 3.50, 5),
        Vegetablebykg("Mandarine", 2.80, 6),
        Vegetablebykg("Orange", 1.50, 8),
        Vegetableperpiece("Pamplemousse", 2.00, 8),
        Vegetablebykg("Poire", 2.50, 5),
        Vegetablebykg("Pomme", 1.50, 8),
        Vegetablebykg("Carotte", 1.30, 7),
        Vegetablebykg("Choux de Bruxelles", 4.00, 4),
        Vegetableperpiece("Chou vert", 2.50, 12),
        Vegetableperpiece("Courge butternut", 2.50, 6),
        Vegetablebykg("Endive", 2.50, 5),
        Vegetablebykg("Épinard", 2.60, 4),
        Vegetablebykg("Poireau", 1.20, 5),
        Vegetableperpiece("Potiron", 2.50, 6),
        Vegetableperpiece("Radis Noir", 5.00, 10),
        Vegetablebykg("Salsifis", 2.50, 3)]
