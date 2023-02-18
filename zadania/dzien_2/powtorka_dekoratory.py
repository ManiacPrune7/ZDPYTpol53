"""
    Co nieco o dekoratorach
"""


def print_author(func):

    def wrapper(*args, **kwargs):
        print("Autor: Ja jestem autorem!")
        temp = func(*args, **kwargs)  # add(5, 5)
        print("Dzieki za wywolanie mojej funkcji")
        return temp

    return wrapper


@print_author
def add(a, b):
    # print("Autor: Ja jestem autorem!")
    return a+b


def subtract(a, b):
    # print("Autor: Ja jestem autorem!")
    return a - b


# add = print_author(add)
# subtract = print_author(subtract)


print(add(2, 3))
# print(new_add(5, 5))

