class Notifier:
    def send(self, message):
        print(f"Sending message: {message}")


# Step 2: Decorator Base Class
class NotifierDecorator:
    def __init__(self, notifier):
        self.notifier = notifier  # Store the wrapped object

    def send(self, message):
        self.notifier.send(message)  # Delegate to the original notifier


# Step 3: Concrete Decorators (Email & SMS)
class EmailNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Sending email: {message}")


class SMSNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Sending SMS: {message}")


# Step 4: Using the Decorators
notifier = Notifier()
email_notifier = EmailNotifier(notifier)
sms_notifier = SMSNotifier(email_notifier)  # Stacking decorators

sms_notifier.send("Hello, Rozz!")
