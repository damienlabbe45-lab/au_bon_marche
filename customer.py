from dataclasses import dataclass


@dataclass
class Customer:
    first_name: str
    last_name: str


def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name


def __repr__(self):
    nom = type(self).__name__
    return f"{nom}{self.last_name} - {self.first_name}"

