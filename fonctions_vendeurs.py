from vendeur import Merchant
from legume import Vegetableperpiece, Vegetablebykg
from functions_customers import add_vegetable_to_order_basket_customer
from customer import Customer
from re import match
from operator import attrgetter


def input_client_vegetable(text: str, merchant: Merchant) -> str:
    text_user = input(text)
    while text_user not in list(map(attrgetter("name"), merchant.vegetable)):
        text_user = input(text)
    return text_user


def input_client_kg(text: str, vegetable: Vegetablebykg) -> float:
    text_user = input(text)
    if bool(match(r"^\d+([;,]\d*)?$", text_user)):
        text_user = float(text_user)
    else:
        text_user = 1000000
    while vegetable.weight < text_user:
        text_user = input(text)
        if bool(match(r"^\d+([;,]\d*)?$", text_user)):
            text_user = float(text_user)
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


def input_client(merchant:Merchant, customer:Customer) -> None:
    vegetable_customer = input_client_vegetable("Veillez choisir un légume parmis " +
                                                f"{', '.join(
                                                    f'{vege for vege in list(map(attrgetter("name"), merchant.vegetable))}"})
