from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing card payment: {amount}")


class BankTransfer(Payment):
    def process_payment(self, amount):
        print(f"Processing bank transfer: {amount}")


payment = CardPayment()
payment.process_payment(100)

transfer = BankTransfer()
transfer.process_payment(250)