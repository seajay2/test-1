class FakePaymentGateway:
    def __init__(self):
        self.charges = []

    def charge(self, order_id, money):
        # Сохраняем данные в формате, ожидаемом тестами
        self.charges.append((order_id, money.amount))

