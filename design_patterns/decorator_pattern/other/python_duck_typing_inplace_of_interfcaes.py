class Notifier:
    def send(self, message):
        print(f"Sending message: {message}")


class EmailDecorator:
    def __init__(self, notifier):
        self.notifier = notifier  # No enforced interface, just composition

    def send(self, message):
        self.notifier.send(message)
        print(f"Sending email: {message}")


notifier = Notifier()
email_notifier = EmailDecorator(notifier)
email_notifier.send("Hello!")
