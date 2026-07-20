from dataclasses import dataclass
from legume import Vegetables


@dataclass
class LineOrderBasket:
    vegetables_ordered: Vegetables
    quantity_ordered: int
    sub_total: float


def __init__(self: LineOrderBasket, vegetables: Vegetables):
    self.vegetables = vegetables
