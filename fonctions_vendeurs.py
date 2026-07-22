from vendeur import Merchant
from functions_customers import add_vegetable_to_order_basket_customer
from customer import Customer


def input_client_vegetable(text, merchant: Merchant) -> str:
    text_user = input(text)
    while text_user not in merchant.vegetable:
        text_user = input(text)
    return text_user


