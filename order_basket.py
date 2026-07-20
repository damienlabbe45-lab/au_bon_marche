from dataclasses import dataclass
from line_order_basket import LineOrderBasket


@dataclass
class OrderBasket:
    """Classe Panier pour la commande d'un client"""
    ref_order_basket: str
    list_line_order: list[LineOrderBasket]


    def __init__(self, ref_order_basket):
        """ Initialisation de la commande d'un client avec une référence.
        Les produits seront ajoutés dans un second temps """
        self.ref_order_basket = ref_order_basket
