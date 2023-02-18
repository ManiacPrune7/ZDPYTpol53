"""
    Przyklad dzialania klasy abstrakcyjnej
"""

import abc


class Animal(abc.ABC):

    def __init__(self, name):
        self.name = name
        #
        #
        #
        #
        #
        #
        #

    @abc.abstractmethod
    def give_a_sound(self):
        ...

    @staticmethod
    def eat():
        print("OMNOMNONMONMO")


class Lion(Animal):

    def __init__(self, name, power):
        super().__init__(name)
        self.claws_power = power

    def give_a_sound(self):
        print("ROARRRRRRRRR")

    def eat(self):
        print("ZzZzZzzzZzz")
        super().eat()


class Eagle(Animal):

    # def __init__(self, name):
    #     self.name = name

    def give_a_sound(self):
        print("RAAAAAAAAAA")


# animal = Animal("Leon")
lion = Lion("Leon", 30)
lion.give_a_sound()
print(lion.name)
lion.eat()

eagle = Eagle("Tuptus")
eagle.give_a_sound()
