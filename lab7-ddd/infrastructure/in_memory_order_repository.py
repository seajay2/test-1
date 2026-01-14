class InMemoryOrderRepository:
    def __init__(self):
        self._orders = {}

    def get_by_id(self, order_id):
        return self._orders.get(order_id)

    def save(self, order):
        self._orders[order.id] = order
