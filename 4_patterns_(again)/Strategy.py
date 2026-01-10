from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Оплата картой: {amount}")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Оплата через PayPal: {amount}")


class Order:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount: float) -> None:
        self.strategy.pay(amount)
