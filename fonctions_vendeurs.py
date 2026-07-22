from vendeur import Merchant
from legume import Vegetableperpiece, Vegetablebykg
from functions_customers import add_vegetable_to_order_basket_customer
from customer import Customer
from re import match


def input_client_vegetable(text, merchant: Merchant) -> str:
    text_user = input(text)
    while text_user not in merchant.vegetable:
        text_user = input(text)
    return text_user


def input_client_kg(text, vegetable: Vegetablebykg) -> float:
    text_user = input(text)
    if bool(match(r"^\d+([;,]\d*)?$", text_user)):
        text_user = float(text_user)
    else:
        text_user = 1000000
    while vegetable.weigth >= text_user:
        text_user = input(text)
        if bool(match(r"^\d+([;,]\d*)?$", text_user)):
            text_user = float(text_user)
        else:
            text_user = 1000000
    return text_user


def input_client_piece(text, vegetable: Vegetableperpiece) -> int:
    text_user = input(text)
    if text_user.isdigit():
        text_user = int(text_user)
    else:
        text_user = 1000000
    while vegetable.unit >= text_user:
        text_user = input(text)
        if text_user.isdigit():
            text_user = int(text_user)
        else:
            text_user = 1000000
    return text_user
