class Calculator:
    def __init__(self):
        print("Calculator creation...")
        self._a = 0
        self.__b = 0
        self.result = None

    def add(self, x, y):
        self._a = x
        self.__b = y
        self.result = self._a + self.__b

    @staticmethod
    def subtract(l2, o0):
        return l2 - o0

    def multiply_numbers(self):
        return self._a * self.__b

    def DivideTwoNumbers(self, NUMBER, NUMBER1):
        print(
            "In a moment the method called DivideTwoNumbers will"
            "divide two numbers: number/number1, the result will be"
            "printed on a terminal, so you will have a chance to see"
            "it live"
        )
        a = NUMBER / NUMBER1
        print(f"{a}")

    def do_hard_COUNTING(self):
        return 5 * 3 * (-2 + (4 + 5 / 8)) / 4 + 6

    def sqrt(self, jakasliczba):
        import math

        return math.sqrt(jakasliczba)

    def printallnumbers(self, all):

        ALL = []

        for ttt in range(all):
            if ttt == 5:
                if len(ALL) is 0:
                    for tt in range(3):
                        print(ttt)

    def divideZERO(self, zero):
        try:
            return zero / 0
        except Exception:
            return zero / 0


class XYZ:
    def __init__(self):
        self.CALCULATOR = Calculator()

    def add_it(self, a, b, c, d, e, f, g):
        return a + b + c + d + e + f + g

    def add(self, x, y):
        self.CALCULATOR.add(x, y)
