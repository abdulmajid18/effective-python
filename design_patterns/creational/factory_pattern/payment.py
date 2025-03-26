from abc import ABC, abstractmethod


# Abstract class (Product)
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Product 1
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card"


# Concrete Product 2
class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"


# Concrete Product 3
class BitcoinPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin"


# Factory Class
class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        if method == "credit_card":
            return CreditCardPayment()
        elif method == "paypal":
            return PayPalPayment()
        elif method == "bitcoin":
            return BitcoinPayment()
        else:
            raise ValueError("Invalid payment method")


# Client Code
method = input("Enter payment method (credit_card/paypal/bitcoin): ").strip().lower()
payment = PaymentFactory.get_payment_method(method)
print(payment.pay(100))  # Example amount
