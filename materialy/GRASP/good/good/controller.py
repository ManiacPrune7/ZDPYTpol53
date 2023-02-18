
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


class CalculatorController:

    def __init__(self):
        self.calculator = Calculator()

    def add(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return self.calculator.add(a, b)
