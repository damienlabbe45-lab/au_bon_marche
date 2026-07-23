from vendeur import Merchant
from legume import init_vegetables
from customer import Customer
from functions_customers import get_arrival_customer, print_receipt_customer
from fonctions_vendeurs import input_client, input_principal_menu

def main():

    merchant = Merchant(name="Théodore", list_vegetable=init_vegetables())

    choix = 0
    # On ne sort pas du programme tant que l'utilisateur ne l'a pas spécifié
    while (choix != 3):
        # Au début du programme, l'utilisateur a le choix entre :
        # -1 : Gérer l'arrivée d'un client
        # -2 : Editer le bilan de la journée
        # -3 : Quitter le programme
        choix = input_principal_menu()

        # Menu de l'application
        # Arrivée d'un client
        if (choix == 1):
            print("Arrivée d'un nouveau client")
            customer = get_arrival_customer()
            merchant.offer()
            input_client(merchant, customer)
            # Affichage du ticket de caisse
            print_receipt_customer(customer)

        # Affichage du bilan de la journée
        elif (choix == 2):
            print("Bilan de la journée")
            print("Clients et leurs achats du jour : ")
            print(Customer.get_print_list_customers())
            print("Stock restant disponible : ")
            merchant.end_journey()

        elif (choix == 3):
            print("Merci, et à bientôt! ")


if __name__ == "__main__":
    main()
