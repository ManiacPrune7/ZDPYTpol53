
class Price:

    def __init__(self, possible_update, amount):
        self.possible_update = possible_update
        self.amount = amount

    def can_update(self):
        return self.possible_update

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def multiply(self, multiplier):

        if self.possible_update is True:
            new_amount = self.get_amount() * multiplier
            return Price(self.possible_update, new_amount)

        return self


class UpdatePrice:

    @staticmethod
    def update(price, multiplier):
        return price.multiply(multiplier)
