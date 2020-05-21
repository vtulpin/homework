from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)


@property
def calculate(self):
    return round((2 * self.param) + 0.3)


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)