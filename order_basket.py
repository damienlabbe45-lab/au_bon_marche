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
        self.list_line_order = []


    def add_line_order_basket(self, line_order_basket: LineOrderBasket):
        """ Méthode qui ajoute une ligne de commande au panier"""
        self.list_line_order.append(line_order_basket)


    def print_order_basket(self):
        """ Méthode qui permet d'afficher le panier pour le client """
        order_basket_beautiful = (" Panier \n\n ")
        order_basket_beautiful += "|   Légume choisi  |     Quantité      |\n"
        for line_order_basket in self.list_line_order:
            legume = line_order_basket.vegetable_ordered
            legume_qty = line_order_basket.quantity_ordered
            order_basket_beautiful += f"{legume}       |      {legume_qty:^10}|\n"
        print(order_basket_beautiful)