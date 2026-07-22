from vendeur import Merchant
from legume import init_vegetables
from functions_customers import get_arrival_customer
from fonctions_vendeurs import input_client


def main():
    merchant = Merchant(name="Théodore", list_vegetable=init_vegetables())
    customer = get_arrival_customer()
    merchant.offer()
    input_client(merchant, customer)


if __name__ == "__main__":
    main()
