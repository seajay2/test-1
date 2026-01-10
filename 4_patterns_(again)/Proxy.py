class RealService:
    def request(self):
        print("Выполнение запроса реальным сервисом")


class ServiceProxy:
    def __init__(self):
        self.real_service = None

    def request(self):
        if self.real_service is None:
            self.real_service = RealService()
        print("Прокси: проверка доступа")
        self.real_service.request()
