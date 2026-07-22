from dataclasses import dataclass
from legume import Vegetables


@dataclass
class LineOrderBasket:
    """Class Ligne Panier : représente une ligne d'un panier de commande"""
    vegetable_ordered: Vegetables
    quantity_ordered: int

    def __init__(self: LineOrderBasket, vegetable: Vegetables, quantity_ordered: int):
        """ Initialisation d'une ligne d'un panier en définissant déjà le fruit ou légume choisi"""
        self.vegetable_ordered = vegetable
        self.quantity_ordered = quantity_ordered

    def get_sub_total_line(self):
        """Fonction qui retourne le sous-total de la ligne du panier"""
        subtotal = self.vegetable_ordered.price * self.quantity_ordered
        return subtotal
    