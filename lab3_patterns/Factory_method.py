from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return 'Windows Button'

class MacButton(Button):
    def render(self):
        return 'Mac Button'

class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()

class MacDialog(Dialog):
    def create_button(self) -> Button:
        return MacButton()

if __name__ == '__main__':
    dialogs = [WindowsDialog(), MacDialog()]
    for dialog in dialogs:
        button = dialog.create_button()
        print(button.render())
