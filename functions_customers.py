from customer import Customer
""" Séverine Hori Maitrehut
Fonctions qui concernent le menu pour l'arrivée du client
"""

def is_saisie_str_ok(saisie):
    """Fonction qui vérifie si une saisie chaine nom/prénom est correcte"""
    cleaned_saisie = saisie.strip()
    if not cleaned_saisie.isalpha():
        return False
    return True

def get_str_input(prompt):
    """Fonction qui demande au joueur de saisir son nom"""
    input_user = input(prompt)
    while not is_saisie_str_ok(input_user):
        input_user = input("Saisie incorrecte. Merci de recommencer : ")
    return input_user


def get_arrival_customer():
    customer_last_name = get_str_input("Entrez le nom du client: ")
    customer_first_name = get_str_input("Entrez le prénom du client: ")
    customer = Customer(customer_first_name, customer_last_name)
    print(f"Bonjour {customer.first_name} {customer.last_name}")
    return customer
