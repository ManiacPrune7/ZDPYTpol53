class Alpha:

    def __init__(self, beta):
        self.beta = beta

    @staticmethod
    def get_new_neighbour(beta):
        return Alpha(beta)

    def who_is_your_neighbour(self):
        return self.beta

    @staticmethod
    def say_hello_to_neighbour(beta):
        beta.say_hello()


class Beta:

    @staticmethod
    def say_hello():
        pass
