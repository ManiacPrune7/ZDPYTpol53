"""
    Na podstawie klasy abstrakcyjnej Wielokat, stworz 3 klasy dziedziczace: Kwadrat, Prostokat, Trojkat.
    Kazda z tych klas musi byc konkretna (a nie abstrakcyjna), powinna wiec nadpisywac wszystkie metody
    abstrakcyjne z klasy Wielokat. Kazda konkretna klasa powinna miec definicje konstruktora __init__
    (dla przykładu obiekt typu Kwadrat, powinien miec jeden atrybut self.bok, obiekt prostokat dwa atrybuty:
    self.bok1, self.bok2, a trojkat self.bok, self.wysokosc).
    Na koniec stworz funkcje zarzadzajaca obiektami stworzonych klas, ktora w petli bedzie obliczala pola
    dla kazdego obiektu.
"""

from abc import ABC, abstractmethod
from typing import Union


class Wielokat(ABC):

    @abstractmethod
    def oblicz_pole(self) -> Union[int, float]:  # Union sugeruje ze funkcja moze zwrocic inta albo floata
        """Metoda ma za zadanie obliczyc pole danego obiektu.

        Ze wzgledu na fakt, iz nie wiemy w tym momencie jaki to jest wielokat,
        nie potrafimy obliczyc jego pola. Do redefinicji w klasie dziedziczacej.

        :return: wartosc pola jako liczba calkowita lub wymierna.
        """
        ...


class Kwadrat(Wielokat):

    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok * self.bok


class Prostokat(Wielokat):

    def __init__(self, bok1, bok2):
        self.bok1 = bok1
        self.bok2 = bok2

    def oblicz_pole(self):
        return self.bok1 * self.bok2


class Trojkat(Wielokat):

    def __init__(self, bok, wysokosc):
        self.bok = bok
        self.wysokosc = wysokosc

    def oblicz_pole(self):
        return self.bok * self.wysokosc * 0.5


def licz_pola(wielokaty: list) -> list:
    """Oblicza pola wszystkich wielokatow podanych w liscie.

    :param wielokaty: lista obiektow dziedziczacych po Wielokat.
    :return: lista obliczonych pol.

    """
    pola = []
    for wielokat in wielokaty:
        pola.append(wielokat.oblicz_pole())
    return pola


kwadrat = Kwadrat(5)
prostokat = Prostokat(3, 4)
wielokaty = [kwadrat, prostokat, Trojkat(4, 7)]
pola = licz_pola(wielokaty)
print(pola)
