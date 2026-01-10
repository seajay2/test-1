from domain.money import Money


class OrderLine:
    def __init__(self, product: str, price: Money, qty: int):
        if qty <= 0:
            raise ValueError("qty must be positive")
        self.product = product
        self.price = price
        self.qty = qty

    def total(self) -> Money:
        return Money(self.price.amount * self.qty)
