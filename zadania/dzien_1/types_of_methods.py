"""
    Przyklad korzystania z staticmethod i classmethod w klasach
"""

global_variable = 10


class Calculator:

    value = 2

    def __init__(self, a, b):
        self.first_no = a
        self.second_no = b

    def add(self):
        return (self.first_no + self.second_no) * Calculator.value

    @staticmethod
    def add_custom(first_no, second_no):
        # print(first_no)
        # print(self.first_no)
        return first_no + second_no

    @classmethod
    def add_custom_cls(cls, first_no, second_no):
        cls.whatever()
        return (first_no + second_no) * cls.value

    @classmethod
    def whatever(cls):
        pass


my_calculator = Calculator(5, 4)
print(my_calculator.add())
print(my_calculator.add_custom(2, 4))
print(Calculator.add_custom(8, 2))
print(Calculator.add_custom_cls(7, 9))
print(my_calculator.add_custom_cls(7, 9))
