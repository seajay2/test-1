import pytest

from domain.order import Order
from domain.order_line import OrderLine
from domain.money import Money
from application.pay_order_use_case import PayOrderUseCase
from infrastructure.in_memory_order_repository import InMemoryOrderRepository
from infrastructure.fake_payment_gateway import FakePaymentGateway


def create_use_case_with_order(order):
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    repo.save(order)
    return PayOrderUseCase(repo, gateway), repo, gateway


def test_successful_payment():
    order = Order(1)
    order.add_line(OrderLine("apple", Money(10), 2))

    use_case, _, gateway = create_use_case_with_order(order)
    result = use_case.execute(1)

    assert result["status"] == "PAID"
    assert result["total"] == 20
    assert gateway.charges == [(1, 20)]


def test_cannot_pay_empty_order():
    order = Order(2)

    use_case, _, _ = create_use_case_with_order(order)
    with pytest.raises(ValueError):
        use_case.execute(2)


def test_cannot_pay_twice():
    order = Order(3)
    order.add_line(OrderLine("book", Money(15), 1))

    use_case, _, _ = create_use_case_with_order(order)
    use_case.execute(3)

    with pytest.raises(ValueError):
        use_case.execute(3)


def test_cannot_modify_paid_order():
    order = Order(4)
    order.add_line(OrderLine("pen", Money(5), 2))

    use_case, _, _ = create_use_case_with_order(order)
    use_case.execute(4)

    with pytest.raises(ValueError):
        order.add_line(OrderLine("pencil", Money(3), 1))


def test_total_amount_calculation():
    order = Order(5)
    order.add_line(OrderLine("a", Money(10), 1))
    order.add_line(OrderLine("b", Money(5), 3))

    assert order.total_amount().amount == 25
