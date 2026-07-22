from dataclasses import dataclass
from order_basket import OrderBasket
from datetime import date
from typing import ClassVar


@dataclass
class Customer:
    """Classe Client """
    customers: ClassVar[list['Customer']] = []

    first_name: str
    last_name: str
    order_basket: OrderBasket

    def __init__(self, first_name, last_name):
        """ Méthode pour instancier un nouveau client, paramètres attendus first_name, et last_name """
        self.first_name = first_name
        self.last_name = last_name
        today = str(date.today())
        reference = self.first_name + today
        self.order_basket = OrderBasket(reference)
        Customer.customers.append(self)

    def __repr__(self):
        """ Méthode pour représenter un client """
        nom_classe = type(self).__name__
        return f"{nom_classe} {self.last_name} - {self.first_name}"

    @staticmethod
    def get_print_list_customers():
        """ Fonction qui affiche la liste des clients et le montant total de leurs achats"""
        print_list_customers = ""
        for cust in Customer.customers:
            print_list_customers += f"- {cust.first_name} {cust.last_name} : {cust.order_basket.get_total()}"
        return print_list_customers
