import abc
import os
import random

import numpy

from test import super_liczba_zawsze_10


def add(a: int, b: int, c: int, d: int,
        e: int, f: int, g: int, h: int, i: int) -> int:
    return a \
           + b \
           + c \
           + d


def subtract(a: int, b: int) -> int:
    return a-b


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


class Human:
    def __init__(uwaga_uwaga_prawie_ze_to_samo_co_self, name, age):
        uwaga_uwaga_prawie_ze_to_samo_co_self._name = name
        uwaga_uwaga_prawie_ze_to_samo_co_self.age = age


bob = Human("Bob", 45)
# print(bob._name, bob.age)

l = "jakas zmienna"  # tak nie nazywamy zmiennych!
O = "inna zmienna"

_var = 1
var_ = 2
dir_ = "...."
open_ = "...."

for _ in range(5):
    print(f"Hello!")
