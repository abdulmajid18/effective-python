from typing import Protocol


class NotifierProtocol(Protocol):
    def send(self, message: str) -> None:
        pass


class Notifier:
    def send(self, message: str) -> None:
        print(f"Sending message: {message}")


class EmailDecorator:
    def __init__(self, notifier: NotifierProtocol):
        self.notifier = notifier  # Now type-checked!

    def send(self, message: str) -> None:
        self.notifier.send(message)
        print(f"Sending email: {message}")
