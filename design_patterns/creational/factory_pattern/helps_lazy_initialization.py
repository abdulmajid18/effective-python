from abc import ABC, abstractmethod


# Abstract Product
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Concrete Products
class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotification(Notification):
    def send(self, message):
        return f"SMS sent: {message}"


# Factory Class with Lazy Initialization
class NotificationFactory:
    _instances = {}

    @staticmethod
    def get_notification(type_):
        if type_ not in NotificationFactory._instances:
            print(f"Creating new instance for {type_}")  # Logging instance creation
            if type_ == "email":
                NotificationFactory._instances[type_] = EmailNotification()
            elif type_ == "sms":
                NotificationFactory._instances[type_] = SMSNotification()
            else:
                raise ValueError("Invalid notification type")

        return NotificationFactory._instances[type_]  # Return cached instance


# Client Code
notification1 = NotificationFactory.get_notification("email")
print(notification1.send("Hello!"))

notification2 = NotificationFactory.get_notification("email")
print(notification2.send("Welcome!"))

notification3 = NotificationFactory.get_notification("sms")
print(notification3.send("OTP: 123456"))
