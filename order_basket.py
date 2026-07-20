from dataclasses import dataclass
from line_order_basket import LineOrderBasket


@dataclass
class OrderBasket:
    ref_order_basket: int
    list_line_order: list[LineOrderBasket]
    total: float


def __init__(self, ref_order_basket: int):
    self.ref_order_basket = ref_order_basket
