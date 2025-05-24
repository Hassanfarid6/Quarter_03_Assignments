# Single responsiblity Principle: SRP,
# Open Closed Principle,
# Liskov Substitution principle (polymorphism mostly),
# interface segregation principle,
# dependency inversion principle,
# ~~~ SOLID DESIGN PRINCIPLE,
from abc import ABC, abstractmethod

class Order():
    def init(self, order_id : str, price : float, weight: float):
        self.order_id = order_id
        self.price = price
        self.weight = weight

class OrderRepository():
    def get(self, order_id:str ) -> Order:
        #imagine a DB fetch here
        return Order(order_id, price=100.0, weight=5.0)

class IPaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount:float) -> dict:
        pass
class IRefundProcessor(ABC):
    @abstractmethod
    def refund(self, amount:float) -> dict:
        pass


class StripeProcessor(IPaymentProcessor, IRefundProcessor):
    def pay(self, amount):
        #processing pay
        return {"status: " f" paid {amount} using stripe"}
    def refund(self, amount):
        #REfurned
        return {"status: " f" Refurned {amount} using stripe"}


class PaypalProcessor(IPaymentProcessor):
    def pay(self, amount):
        #processing pay
        return {"status: " f" paid {amount} using Paypal"}

class BankPaymentProcessor(IPaymentProcessor):
    def pay(self, amount):
        #processing pay
        return {"status: " f" paid {amount} using Banking Payment"}


class OrderCheckout():
    def init(self, order: Order, payment: IPaymentProcessor):
        self.order = order
        self.payment = payment
    def checkout(self , order_id:str):
        order = self.order.get(order_id)
        payment = self.payment.pay(order.price)
        return "order_id {order.order_id} , payment: {payment.order_price}"


order = OrderRepository()
stripePay = StripeProcessor()
paypalPay = PaypalProcessor()
bankpay = BankPaymentProcessor()
order_complete = OrderCheckout(order, stripePay or paypalPay or bankpay)
order_complete.checkout("ABC")
