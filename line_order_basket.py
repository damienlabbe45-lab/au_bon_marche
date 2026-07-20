from dataclasses import dataclass
from legume import Vegetables


@dataclass
class LineOrderBasket:
    """Class Ligne Panier : représente une ligne d'un panier de commande"""
    vegetables_ordered: Vegetables
    quantity_ordered: int
    sub_total: float


    def __init__(self: LineOrderBasket, vegetables: Vegetables):
        """ Initialisation d'une ligne d'un panier en définissant déjà le fruit ou légume choisi"""
        self.vegetables = vegetables
