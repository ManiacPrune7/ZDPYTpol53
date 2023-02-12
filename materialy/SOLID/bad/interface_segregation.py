"""
    Zbyt duza klasa abstrakcyjna Animal.
"""

import abc


class Animal(abc.ABC):

    @abc.abstractmethod
    def eat(self):
        ...

    @abc.abstractmethod
    def run(self):
        ...

    @abc.abstractmethod
    def fly(self):
        ...

    @abc.abstractmethod
    def swim(self):
        ...

    @abc.abstractmethod
    def give_a_voice(self):
        ...


class Lion(Animal):

    def eat(self):
        ...

    def run(self):
        ...

    def fly(self):
        pass  # !!!!!

    def swim(self):
        ...

    def give_a_voice(self):
        ...