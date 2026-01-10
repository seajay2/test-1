from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        pass


class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("authenticated"):
            return "Ошибка: пользователь не авторизован"
        return self.next_handler.handle(request) if self.next_handler else "OK"


class RoleHandler(Handler):
    def handle(self, request):
        if request.get("role") != "admin":
            return "Ошибка: недостаточно прав"
        return self.next_handler.handle(request) if self.next_handler else "OK"
