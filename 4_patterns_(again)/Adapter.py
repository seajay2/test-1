class OldSystem:
    def old_request(self):
        return "Ответ старой системы"


class Adapter:
    def __init__(self, old_system: OldSystem):
        self.old_system = old_system

    def request(self):
        return self.old_system.old_request()
