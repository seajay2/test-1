class Money:
    def __init__(self, amount: int):
        if amount < 0:
            raise ValueError("Money amount must be non-negative")
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __eq__(self, other):
        return self.amount == other.amount
