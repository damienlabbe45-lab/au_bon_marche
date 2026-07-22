from vendeur import Merchant
from legume import init_vegetables
from functions_customers import get_arrival_customer

def main():
    merchant = Merchant(name="Théodore", list_vegetable = init_vegetables())
    client = get_arrival_customer()
    merchant.offer()





if __name__ == "__main__":
    main()
