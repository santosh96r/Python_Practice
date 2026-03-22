"""
06 - Abstraction (ABC)
=======================
Covers: Abstract Base Classes, @abstractmethod, enforcing interface contracts
"""

from abc import ABC, abstractmethod


# ==================== ABSTRACT BASE CLASS ====================
# An abstract class CANNOT be instantiated directly.
# It forces subclasses to implement certain methods.

class PaymentGateway(ABC):
    """Abstract base — defines the contract for all payment processors."""

    @abstractmethod
    def pay(self, amount):
        """Subclasses MUST implement this."""
        pass

    @abstractmethod
    def refund(self, transaction_id):
        pass

    def receipt(self, amount):
        """Concrete method — shared by all subclasses."""
        print(f"Receipt: ₹{amount} processed via {self.__class__.__name__}")


class CreditCardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card")
        self.receipt(amount)

    def refund(self, transaction_id):
        print(f"Refunded transaction {transaction_id} to Credit Card")


class UPIPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")
        self.receipt(amount)

    def refund(self, transaction_id):
        print(f"Refunded transaction {transaction_id} to UPI wallet")


# --- Usage ---
# gateway = CreditCardPayment()
# gateway.pay(500)
# gateway.refund("TXN123")

# This would raise TypeError:
# pg = PaymentGateway()   # ← Can't instantiate abstract class


# ==================== WHY USE ABSTRACTION? ====================
# - Enforces a consistent interface across different implementations
# - Prevents incomplete implementations from being used
# - Common in frameworks: define the "what", let subclasses define the "how"


# ==================== PRACTICE ====================

# 1. Create an abstract class `Database` with methods: connect(), query(), close()
#    Implement `MySQLDatabase` and `MongoDBDatabase` subclasses.
#
# 2. Create an abstract class `Notification` with send(message)
#    Implement `EmailNotification`, `SMSNotification`, `PushNotification`
#
# 3. Create an abstract class `Shape` with area() and perimeter()
#    Implement `Triangle`, `Circle`, `Square` — try instantiating Shape directly.
