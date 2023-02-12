
class Price:

    def __init__(self, possible_update: bool, amount: int):
        self.possible_update = possible_update
        self.amount = amount

    def can_update(self):
        return self.possible_update

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount


class UpdatePrice:

    @staticmethod
    def update(price: Price, multiplier: int):

        if price.can_update():
            new_price = price.get_amount() * multiplier
            price.set_amount(new_price)

        return price
