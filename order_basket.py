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


    def get_order_basket(self):
        """ Méthode qui permet d'afficher le panier pour le client """
        line_separ = "-"*58+"\n"
        order_basket_beautiful = " "*25 + "Panier\n"
        order_basket_beautiful += line_separ
        order_basket_beautiful += "|Légume choisi     |      Prix        |    Quantité      |\n"
        order_basket_beautiful += line_separ
        for line_order_basket in self.list_line_order:
            legume = line_order_basket.vegetable_ordered.name_vegetable
            legume_prix = line_order_basket.vegetable_ordered.price
            legume_qty = line_order_basket.quantity_ordered
            order_basket_beautiful += f"|{legume:<18}|{legume_prix:<18}|{legume_qty:<18}|\n"
        order_basket_beautiful += line_separ
        return order_basket_beautiful


    def get_total(self):
        total = 0
        for line in self.list_line_order:
            total += line.get_sub_total_line()
        return total
        
    
    def get_receipt(self):
        receipt = "Ticket de caisse \n"
        for line in self.list_line_order:
            receipt += f"Légume : {line.vegetable_ordered.name_vegetable} - "
            receipt += f"Prix : {line.vegetable_ordered.price} - "
            receipt += f"Quantité commandée : {line.quantity_ordered}\n"
            receipt += f"Sous-total : {line.get_sub_total_line()}\n"
        receipt += f"TOTAL : {self.get_total()}\n"
        return receipt