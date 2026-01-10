from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation(self):
        return "Реализация A"


class ConcreteImplementationB(Implementation):
    def operation(self):
        return "Реализация B"


class Abstraction:
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self):
        return f"Абстракция использует ({self.implementation.operation()})"
