"""
03 - Encapsulation
===================
Covers: public, protected (_), private (__) attributes and methods,
        name mangling, controlled access via public interface
"""

# ==================== ACCESS LEVELS ====================
#
# Public    : self.name        → accessible everywhere
# Protected : self._salary     → convention: "internal use only" (still accessible)
# Private   : self.__balance   → name-mangled to _ClassName__balance (hard to access)


# ==================== EXAMPLE: Employee (access levels) ====================

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name        # public
#         self._salary = salary   # protected (convention)
#
#     def show(self):
#         print(f"Employee {self.name}, salary: {self._salary}")
#
#     def get_salary(self):
#         return self._salary
#
# e1 = Employee("skr", 10000)
# print(e1.name)            # OK — public
# print(e1._salary)         # Works, but discouraged — protected
# print(e1.get_salary())    # Preferred way


# ==================== EXAMPLE: BankAccount (private methods) ====================

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount  # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()  # Accessing protected method
        else:
            print("Invalid deposit amount!")


account = BankAccount()
account._show_balance()  # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)  # Uses both methods internally