from abc import ABC, abstractmethod


class Neighbour(ABC):

    @abstractmethod
    def say_hello(self):
        ...


class Alpha:

    def __init__(self, neighbour):
        self.neighbour = neighbour

    @staticmethod
    def get_new_neighbour(beta):
        return Alpha(beta)

    def who_is_your_neighbour(self):
        return self.neighbour

    @staticmethod
    def say_hello_to_neighbour(neighbour):
        neighbour.say_hello()


class Beta(Neighbour):

    @staticmethod
    def say_hello():
        print("HELLO!")
