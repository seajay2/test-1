from domain.money import Money
from domain.order_status import OrderStatus


class Order:
    def __init__(self, order_id: int):
        self.id = order_id
        self.lines = []
        self.status = OrderStatus.NEW

    def add_line(self, line):
        if self.status == OrderStatus.PAID:
            raise ValueError("cannot modify paid order")
        self.lines.append(line)

    def total_amount(self) -> Money:
        total = Money(0)
        for line in self.lines:
            total += line.total()
        return total

    def pay(self):
        if not self.lines:
            raise ValueError("cannot pay empty order")
        if self.status == OrderStatus.PAID:
            raise ValueError("order already paid")
        self.status = OrderStatus.PAID
