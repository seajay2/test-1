# Lab 7 — Layered Architecture + DDD-lite (Order Payment)

Проект демонстрирует слоистую архитектуру и подход DDD-lite на примере оплаты заказа.

## Layers
- **Domain**: доменная модель (`Order`, `OrderLine`, `Money`, `OrderStatus`) и бизнес-инварианты.
- **Application**: use-case `PayOrderUseCase`.
- **Infrastructure**: `InMemoryOrderRepository` и `FakePaymentGateway`.
- **Tests**: тесты use-case и доменных правил без реальной базы данных.

## Business rules (invariants)
- Нельзя оплатить пустой заказ.
- Нельзя оплатить заказ повторно.
- После оплаты нельзя изменять строки заказа.
- Итоговая сумма равна сумме строк заказа.
