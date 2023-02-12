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
