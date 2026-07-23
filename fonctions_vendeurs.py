from vendeur import Merchant
from legume import Vegetableperpiece, Vegetablebykg
from functions_customers import add_vegetable_to_order_basket_customer
from customer import Customer
from re import match
from operator import attrgetter


def is_entry_int_ok(user_input, min_int, max_int):
    """ Fonction qui vérifie la saisie d'un numérique, entre min_int et max_int    """
    cleaned_user_input = user_input.strip()
    if not cleaned_user_input.isdigit():
        return False
    if int(cleaned_user_input) < min_int or int(cleaned_user_input) > max_int:
        return False
    return True


def input_principal_menu():
    """ Fonction qui demande à l'utilisateur de choisir une action
        -Gérer l'arrivée d'un client : 1
        -Editer le bilan de la journée 2
    """
    input_menu = input("Bonjour.Menu :\n 1 Arrivée d'un client\n 2 Afficher le bilan de la journée\n 3 Quitter le programme\n")
    while not is_entry_int_ok(input_menu, 1, 3):
        input_menu = input("Saisie incorrecte. Merci de recommencer : ")
    return int(input_menu)



def input_client_vegetable(text: str, merchant: Merchant) -> Vegetableperpiece | Vegetablebykg:
    text_user = input(text)
    while text_user not in list(map(attrgetter("name_vegetable"), merchant.vegetable)):
        text_user = input(text)
    return next(v for v in merchant.vegetable if v.name_vegetable == text_user)


def input_client_kg(text: str, vegetable: Vegetablebykg) -> float:
    text_user = input(text)
    if bool(match(r"^\d+([;,]\d*)?$", text_user)):
        text_user = float(text_user.replace(",", "."))
    else:
        text_user = 1000000
    while vegetable.weight < text_user:
        text_user = input(text)
        if bool(match(r"^\d+([;,]\d*)?$", text_user)):
            text_user = float(text_user.replace(",", "."))
        else:
            text_user = 1000000
    return text_user


def input_client_piece(text: str, vegetable: Vegetableperpiece) -> int:
    text_user = input(text)
    if text_user.isdigit():
        text_user = int(text_user)
    else:
        text_user = 1000000
    while vegetable.unit < text_user:
        text_user = input(text)
        if text_user.isdigit():
            text_user = int(text_user)
        else:
            text_user = 1000000
    return text_user


def input_client(merchant: Merchant, customer: Customer) -> None:
    is_continue = True
    while is_continue:
        vegetable_customer = input_client_vegetable("Veillez choisir un légume parmis " +
                                                    f"{', '.join(v.name_vegetable for v in merchant.vegetable)}.",
                                                    merchant)
        if isinstance(vegetable_customer, Vegetablebykg):
            number = input_client_kg(
                f" veillez indiquer combien de kg , vous voulez pour {
                vegetable_customer.name_vegetable}" + f" en sachant que c'est maximun {vegetable_customer.weight}.",
                vegetable_customer)
        elif isinstance(vegetable_customer, Vegetableperpiece):
            number = input_client_piece(f"Veillez indiquer combien de {vegetable_customer.name_vegetable}, vous voulez"
                                        + f" en sachant que le maximun c'est {vegetable_customer.unit}",
                                        vegetable_customer)
            add_vegetable_to_order_basket_customer(customer, vegetable_customer, number)
            merchant.sold_vegetable(vegetable_customer, number, customer)
        is_continue = input_bool()

def input_bool() -> bool:
    text: str = ""
    while text not in ["oui", "non"]:
        text = input("voulez vous contunier d'acheter (Oui ou Non)?").lower().strip()
    return text == "oui"