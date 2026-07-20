from dataclasses import dataclass
from line_order_basket import LineOrderBasket


@dataclass
class OrderBasket:
    list_line_order: list[LineOrderBasket]
    total: float
