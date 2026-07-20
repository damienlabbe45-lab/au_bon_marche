from dataclasses import dataclass
from order_basket import OrderBasket

@dataclass
class Customer:
    """Classe Client"""
    first_name: str
    last_name: str
    orderBasket: OrderBasket


def __init__(self, first_name, last_name):
    """ Méthode pour instancier un nouveau client, paramètres attendus first_name, et last_name """
    self.first_name = first_name
    self.last_name = last_name


def __repr__(self):
    """ Méthode pour représenter un client """
    nom = type(self).__name__
    return f"{nom}{self.last_name} - {self.first_name}"

