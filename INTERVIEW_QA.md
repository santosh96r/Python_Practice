# Python Automation Interview — Questions & Answers
### Target: 4 Years Experience | Intermediate → Advanced

---

> **How to use this file:**
> - Read each question and attempt your own answer first
> - Then check the detailed answer below
> - Code blocks show patterns you should be able to write from memory
> - Questions marked `[CODING]` expect you to write code live on a whiteboard/shared editor

---

## Table of Contents

1. [Python Fundamentals](#1-python-fundamentals)
2. [OOP — Classes & Objects](#2-oop--classes--objects)
3. [OOP — Inheritance & MRO](#3-oop--inheritance--mro)
4. [OOP — Encapsulation & Access Modifiers](#4-oop--encapsulation--access-modifiers)
5. [OOP — Polymorphism & Duck Typing](#5-oop--polymorphism--duck-typing)
6. [OOP — Abstraction (ABC)](#6-oop--abstraction-abc)
7. [OOP — Class Methods, Static Methods & Properties](#7-oop--class-methods-static-methods--properties)
8. [OOP — Magic / Dunder Methods](#8-oop--magic--dunder-methods)
9. [Functional Programming — Lambda, Map, Filter](#9-functional-programming--lambda-map-filter)
10. [Closures & Decorators](#10-closures--decorators)
11. [Iterators](#11-iterators)
12. [Generators](#12-generators)
13. [File Handling & OS Module](#13-file-handling--os-module)
14. [Exception Handling](#14-exception-handling)
15. [JSON & Data Processing](#15-json--data-processing)
16. [API Testing with `requests`](#16-api-testing-with-requests)
17. [Logging](#17-logging)
18. [Threading & Multiprocessing](#18-threading--multiprocessing)
19. [Data Structures — Linked List](#19-data-structures--linked-list)
20. [Advanced Python — Metaclasses, Memory Model & Internals](#20-advanced-python--metaclasses-memory-model--internals)

---

## 1. Python Fundamentals

---

**Q1. What is CPython, and what happens when you run a `.py` file?**

**Answer:**
CPython is the reference implementation of Python written in C. When you run a `.py` file:
1. The source code is parsed and compiled to **bytecode** (`.pyc` files stored in `__pycache__`).
2. The bytecode is executed by the **Python Virtual Machine (PVM)**.

This compile-once, interpret-many approach is why Python is called an interpreted language — you never compile directly to native machine code (unless you use tools like Cython or PyPy).

---

**Q2. What is CPython's small integer caching? What are the implications in automation code?**

**Answer:**
CPython pre-allocates integer objects for values in the range **-5 to 256**. Assignments to these values share the same object in memory.

```python
a = 100
b = 100
print(a is b)   # True  — same object (cached)

a = 1000
b = 1000
print(a is b)   # False — different objects (NOT cached)
```

**Automation implication:** Never use `is` to compare values — always use `==`. Using `is` for equality checks on integers/strings outside the cache range produces unpredictable `False` results. Test IDs from APIs are often large integers where `is` would silently fail.

---

**Q3. Explain short-circuit evaluation with `and` / `or`. How can it cause bugs in test assertions?**

**Answer:**
Python evaluates `and`/`or` lazily and **returns the actual value, not a boolean**.

```python
# and: returns first falsy value, or last value if all truthy
0 and print("won't run")    # →  0  (stops at 0)
1 and "hello"               # →  "hello"

# or: returns first truthy value, or last value if all falsy
None or "default"           # →  "default"
"user" or "default"         # →  "user"
```

**Bug example in automation:**
```python
# WRONG — truthy/falsy confusion
response_data = api.get_user()
assert response_data and response_data["status"] == "active"
# If response_data = {} (empty dict), this silently passes because
# {} is falsy and `and` short-circuits, never checking status!

# CORRECT
assert response_data is not None and len(response_data) > 0
assert response_data["status"] == "active"
```

---

**Q4. `find()` vs `index()` on strings — when would each cause a subtle bug?**

**Answer:**

| Method | Not Found Behavior | Return Type |
|--------|-------------------|-------------|
| `find()` | Returns `-1` | `int` |
| `index()` | Raises `ValueError` | `int` |

```python
log = "ERROR: connection refused"
pos = log.find("WARNING")  # -1 — no exception, easy to miss
pos = log.index("WARNING") # raises ValueError immediately

# Automation bug with find():
if log.find("ERROR"):      # WRONG! -1 is truthy! This always passes.
    ...

# Correct:
if log.find("ERROR") != -1:
    ...
# Or use 'in':
if "ERROR" in log:
    ...
```

---

**Q5. [CODING] Parse this log line and extract structured fields:**
```
"2024-01-15 10:32:45 | ERROR | auth_service | msg=Login failed | user=john_doe | code=401"
```
Extract: timestamp, level, service, message, user, code.

**Answer:**
```python
log = "2024-01-15 10:32:45 | ERROR | auth_service | msg=Login failed | user=john_doe | code=401"

parts = [p.strip() for p in log.split("|")]
timestamp = parts[0]
level     = parts[1]
service   = parts[2]

kv_fields = {}
for field in parts[3:]:
    key, _, value = field.partition("=")
    kv_fields[key.strip()] = value.strip()

print(timestamp)      # 2024-01-15 10:32:45
print(level)          # ERROR
print(kv_fields)      # {'msg': 'Login failed', 'user': 'john_doe', 'code': '401'}
```

**Why `partition()` over `split("=", 1)`?** `partition()` always returns a 3-tuple even if `=` is not found, preventing `ValueError` on malformed lines — safer for real log parsers.

---

**Q6. What is the difference between mutable and immutable types? Give a real automation example where this bites you.**

**Answer:**
- **Immutable**: `int`, `float`, `str`, `tuple`, `frozenset` — operations return new objects
- **Mutable**: `list`, `dict`, `set`, custom class instances — modified in-place

**Classic automation bug — mutable default argument:**
```python
# WRONG — list is created ONCE when the function is defined
def add_header(key, value, headers={}):
    headers[key] = value
    return headers

r1 = add_header("Content-Type", "application/json")
r2 = add_header("Authorization", "Bearer xyz")
print(r2)  # {'Content-Type': 'application/json', 'Authorization': 'Bearer xyz'}
# r2 contains r1's headers! They share the same dict object.

# CORRECT
def add_header(key, value, headers=None):
    if headers is None:
        headers = {}
    headers[key] = value
    return headers
```

---

**Q7. What is `is` vs `==`? When should use each in automation?**

**Answer:**
- `==` checks **value equality** (`__eq__` method called)
- `is` checks **identity** — same object in memory (`id(a) == id(b)`)

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b    # True  — same values
a is b    # False — different objects

c = a
c is a    # True  — same object
```

**In automation:**
- Use `is` only for `None` checks: `if response is None:`
- Use `==` for all value comparisons
- NEVER: `if response == None:` (works but semantically wrong; `__eq__` could be overridden)

---

## 2. OOP — Classes & Objects

---

**Q8. What is the difference between class attributes and instance attributes? Can a class attribute be shadowed?**

**Answer:**
- **Class attribute**: shared across all instances, defined at class body level
- **Instance attribute**: unique per instance, defined in `__init__` via `self`

```python
class Employee:
    company = "TechCorp"        # class attribute
    headcount = 0

    def __init__(self, name):
        Employee.headcount += 1
        self.name = name        # instance attribute

e1 = Employee("Alice")
e2 = Employee("Bob")

print(Employee.headcount)   # 2
print(e1.company)           # "TechCorp" — reads class attribute

# Shadowing: assigning to instance creates a new instance attribute
e1.company = "StartupX"
print(e1.company)           # "StartupX" — instance attribute shadows class attribute
print(e2.company)           # "TechCorp" — unchanged; still reads class attribute
print(Employee.company)     # "TechCorp" — class attribute untouched
```

**Interview trick:** Mutating a mutable class attribute (like a list) via one instance affects all — because you're modifying the same object, not reassigning.

```python
class Config:
    tags = []

c1 = Config()
c2 = Config()
c1.tags.append("smoke")   # mutates the shared list
print(c2.tags)             # ["smoke"] — c2 is affected!
```

---

**Q9. [CODING] Create an `Employee` class with a factory classmethod that builds an instance from a hyphen-separated string like `"Alice-Engineer-75000"`.**

**Answer:**
```python
class Employee:
    raise_percent = 1.05  # class attribute

    def __init__(self, name, role, salary):
        self.name   = name
        self.role   = role
        self.salary = salary

    @classmethod
    def from_string(cls, emp_string):
        name, role, salary = emp_string.split("-")
        return cls(name, role, int(salary))   # cls not Employee — supports subclasses

    @classmethod
    def set_raise(cls, percent):
        cls.raise_percent = percent

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percent)

    def __repr__(self):
        return f"Employee(name={self.name!r}, role={self.role!r}, salary={self.salary})"

e = Employee.from_string("Alice-Engineer-75000")
print(e)  # Employee(name='Alice', role='Engineer', salary=75000)
```

**Why `cls(...)` instead of `Employee(...)`?** If a subclass calls `Employee.from_string(...)`, `cls` will be the subclass. Using `Employee(...)` would break polymorphism — the subclass would get an `Employee` instance instead of its own type.

---

**Q10. What does `__doc__` return, and how is it useful in automation frameworks?**

**Answer:**
`__doc__` returns the docstring of any class, method, function, or module.

```python
class LoginPage:
    """Page Object for the Login page of the application under test."""

    def enter_credentials(self, username, password):
        """
        Enters username and password into login form.
        :param username: str
        :param password: str
        """
        pass

print(LoginPage.__doc__)
print(LoginPage.enter_credentials.__doc__)
```

**Automation use case:** Many test reporting frameworks (pytest, Allure) use docstrings as test descriptions. The `__doc__` attribute also enables dynamic test discovery and self-documenting test helpers.

---

## 3. OOP — Inheritance & MRO

---

**Q11. What is Method Resolution Order (MRO) and how does Python compute it?**

**Answer:**
MRO defines the order in which base classes are searched when looking up a method or attribute. Python uses the **C3 Linearization (C3 superclass linearization)** algorithm.

```python
class A:
    def show(self): print("A")

class B(A):
    def show(self): print("B")

class C(A):
    def show(self): print("C")

class D(B, C):
    pass

D.__mro__
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

D().show()  # "B" — B comes before C in MRO
```

**Key rules of C3:**
1. A class always appears before its parents
2. If a class is inherited by multiple paths, it appears after all classes that inherit it
3. Order of base classes in class definition is preserved

---

**Q12. When would you use `super()` vs explicit parent class call? What problem does `super()` solve in multiple inheritance?**

**Answer:**

**With explicit call** — breaks cooperative inheritance:
```python
class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, role):
        self.role = role

class Employee(Job, Person):
    def __init__(self, name, role):
        Person.__init__(self, name)   # explicit — fine for single inheritance
        Job.__init__(self, role)      # but with diamond inheritance, A.__init__ runs twice
```

**With `super()`** — follows MRO, each `__init__` called exactly once:
```python
class A:
    def __init__(self):
        print("A init")
        super().__init__()   # passes control to next in MRO

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()   # calls B, B calls C (via MRO), C calls A — each once

D()
# D init → B init → C init → A init
```

**Rule of thumb:** In production OOP code, always use `super()`. Use explicit class calls only when you intentionally want to skip MRO (very rare).

---

**Q13. Explain `isinstance()` vs `issubclass()` with an example.**

**Answer:**
```python
class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass

rex = Dog()

isinstance(rex, Dog)      # True  — rex is a Dog instance
isinstance(rex, Animal)   # True  — Dog is a subclass of Animal
isinstance(rex, Cat)      # False

issubclass(Dog, Animal)   # True
issubclass(Dog, Cat)      # False
issubclass(Animal, object) # True — all classes inherit from object

# isinstance() accepts a tuple for multiple type checks:
isinstance(rex, (Dog, Cat))  # True — rex is Dog or Cat
```

**Automation use:** In API test frameworks, `isinstance(response_data, dict)` guards against unexpected data types from deserialized JSON before accessing nested keys.

---

**Q14. What is the diamond problem and how does Python solve it?**

**Answer:**
The diamond problem occurs when a class inherits from two classes that both inherit from a common base — creating a diamond-shaped inheritance graph.

```
       A
      / \
     B   C
      \ /
       D
```

Without MRO, `A.__init__()` would be called twice. Python's C3 linearization ensures each class in the hierarchy is visited **exactly once**, in the correct order.

```python
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    def hello(self):
        return "B -> " + super().hello()   # calls next in MRO

class C(A):
    def hello(self):
        return "C -> " + super().hello()   # calls A (next in MRO for C)

class D(B, C):
    def hello(self):
        return "D -> " + super().hello()   # calls B (next in MRO for D)

print(D().hello())   # "D -> B -> C -> Hello from A"
# MRO: D → B → C → A → object
```

---

## 4. OOP — Encapsulation & Access Modifiers

---

**Q15. What are Python's three access levels and how are they enforced?**

**Answer:**

| Convention | Syntax | Enforcement |
|---|---|---|
| Public | `self.name` | No restriction — accessible anywhere |
| Protected | `self._name` | Convention only — still accessible externally |
| Private | `self.__name` | Name mangling — `_ClassName__name` — accessed externally only via mangled name |

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner   = owner          # public
        self._limit  = 10000          # protected — "internal use" convention
        self.__balance = balance       # private — name mangled to _BankAccount__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount   # accessible inside class

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 5000)
print(acc.owner)                        # "Alice"   — OK
print(acc._limit)                       # 10000     — works but violates convention
print(acc.__balance)                    # AttributeError!
print(acc._BankAccount__balance)        # 5000      — name mangling bypass (for debugging only)
```

**Interview point:** Python has no true private access. Name mangling is a **name-collision prevention** mechanism for subclasses, not a security feature. The single underscore `_` is a gentlemen's agreement.

---

**Q16. Name mangling — why does it exist? Give an inheritance example where it prevents a bug.**

**Answer:**
Name mangling's primary purpose is to prevent accidental attribute name collision in subclasses:

```python
class Base:
    def __init__(self):
        self.__secret = "base_secret"   # stored as _Base__secret

    def get_secret(self):
        return self.__secret            # reads _Base__secret

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__secret = "child_secret"  # stored as _Child__secret — different attribute!

    def get_child_secret(self):
        return self.__secret            # reads _Child__secret

c = Child()
print(c.get_secret())         # "base_secret"  — reads _Base__secret
print(c.get_child_secret())   # "child_secret" — reads _Child__secret
# Without mangling, Child.__init__ would overwrite Base's __secret
```

---

## 5. OOP — Polymorphism & Duck Typing

---

**Q17. Explain duck typing. How does it differ from static-typed polymorphism? Give an automation example.**

**Answer:**
> "If it walks like a duck and quacks like a duck, it is a duck."

Python doesn't check an object's type — it checks whether the object has the required method/attribute.

```python
# No common base class needed — just needs a .click() method
class SeleniumButton:
    def click(self): print("Selenium click via WebDriver")

class AppiumElement:
    def click(self): print("Appium tap via mobile driver")

class MockElement:
    def click(self): print("Mock click — no browser needed")

def perform_click(element):
    element.click()   # Duck typing — works with any object that has .click()

perform_click(SeleniumButton())   # works
perform_click(AppiumElement())    # works
perform_click(MockElement())      # works — great for unit testing!
```

**Why this matters in automation:** You can swap real browser drivers with mock objects in unit tests without changing the page object code — as long as the interface (method names) matches.

---

**Q18. What is operator overloading? Implement a `Response` class where `==` compares status codes.**

**Answer:**
Operator overloading lets you define how Python operators behave for custom classes through dunder methods.

```python
class Response:
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body        = body

    def __eq__(self, other):
        if isinstance(other, Response):
            return self.status_code == other.status_code
        if isinstance(other, int):         # also support: response == 200
            return self.status_code == other
        return NotImplemented

    def __repr__(self):
        return f"Response(status={self.status_code})"

    def __bool__(self):
        return 200 <= self.status_code < 300   # truthy if 2xx

r1 = Response(200, {"user": "alice"})
r2 = Response(200, {"user": "bob"})

print(r1 == r2)    # True  — both 200, body ignored
print(r1 == 200)   # True
print(bool(r1))    # True
print(bool(Response(404, {})))  # False
```

---

**Q19. What does `NotImplemented` mean vs `NotImplementedError`? When do you return it from `__eq__`?**

**Answer:**

| | `NotImplemented` | `NotImplementedError` |
|---|---|---|
| Type | Singleton object (not an exception) | Exception class |
| Used in | Dunder methods (`__eq__`, `__add__`) | Abstract methods, `raise` statements |
| Effect | Tells Python to try the reflected operation on the other operand | Raises an exception immediately |

```python
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented    # let Python try other.__eq__(self)
    return self.value == other.value
```

When `__eq__` returns `NotImplemented`, Python tries `other.__eq__(self)`. If that also returns `NotImplemented`, Python falls back to identity comparison (`is`).

---

## 6. OOP — Abstraction (ABC)

---

**Q20. What is an Abstract Base Class? Why can't you instantiate one? Show the enforcement mechanism.**

**Answer:**
An ABC defines a contract — a set of methods that all concrete subclasses **must** implement. Python enforces this at instantiation time, not definition time.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount): ...         # must implement

    @abstractmethod
    def refund(self, amount): ...      # must implement

    def receipt(self, amount):         # concrete method — inherited as-is
        return f"Receipt: ${amount} processed via {self.__class__.__name__}"

class PayPal(PaymentGateway):
    def pay(self, amount):
        return f"PayPal charged ${amount}"
    def refund(self, amount):
        return f"PayPal refunded ${amount}"

# PaymentGateway()  →  TypeError: Can't instantiate abstract class ...
# Incomplete subclass would also fail at instantiation, not at creation!

class Stripe(PaymentGateway):
    def pay(self, amount): ...
    # missing refund()

# Stripe()  →  TypeError: Can't instantiate ... with abstract method refund
```

**Automation use:** Define a `BaseDriver(ABC)` with abstract methods `open()`, `close()`, `find_element()`. Then implement `ChromeDriver`, `FirefoxDriver`, `MockDriver` — each forced to fulfill the contract.

---

**Q21. What is the difference between an interface and an abstract class in Python?**

**Answer:**
Python doesn't have a formal `interface` keyword (unlike Java/C#), but you can model interfaces with ABC:

| | Abstract Class (Python) | Pure Interface (ABC pattern) |
|---|---|---|
| Concrete methods | Yes — can have implementations | No — all methods abstract |
| Constructor | Can have `__init__` with logic | Usually empty or sets interface |
| State | Can have instance attributes | Typically stateless |
| Multiple inheritance | Supported | Commonly used with multiple inheritance |

```python
# Pure interface style — all methods abstract
class Clickable(ABC):
    @abstractmethod
    def click(self): ...

class Visible(ABC):
    @abstractmethod
    def is_visible(self) -> bool: ...

# Multiple interface inheritance — composition over inheritance
class WebElement(Clickable, Visible):
    def click(self): print("clicked")
    def is_visible(self): return True
```

---

## 7. OOP — Class Methods, Static Methods & Properties

---

**Q22. When do you use `@classmethod` vs `@staticmethod` vs `@property`? Give one practical use case for each.**

**Answer:**

| Decorator | Receives | Use when |
|---|---|---|
| `@classmethod` | `cls` (the class itself) | Factory methods, modifying class state, subclass-aware constructors |
| `@staticmethod` | Nothing | Utility/helper functions logically grouped with the class, no class/instance state needed |
| `@property` | `self` | Computed attributes, validation on assignment, read-only attributes |

```python
import re

class TestConfig:
    _env = "staging"

    def __init__(self, base_url, timeout):
        self.base_url = base_url
        self._timeout = timeout    # raw value in seconds

    # Factory classmethod — creates from environment file line
    @classmethod
    def from_env_string(cls, env_str):
        # "base_url=https://staging.api.com,timeout=30"
        parts = dict(p.split("=") for p in env_str.split(","))
        return cls(parts["base_url"], int(parts["timeout"]))

    @classmethod
    def set_env(cls, env):
        cls._env = env

    # Utility method — no state needed, but logically belongs here
    @staticmethod
    def is_valid_url(url):
        return bool(re.match(r'https?://.+', url))

    # Property — computed, with validation
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        if value <= 0:
            raise ValueError("Timeout must be positive")
        self._timeout = value

cfg = TestConfig.from_env_string("base_url=https://api.com,timeout=30")
print(TestConfig.is_valid_url("https://api.com"))   # True — no instance needed
cfg.timeout = 60      # setter called
cfg.timeout = -1      # ValueError!
```

---

**Q23. [CODING] Implement a `Temperature` class with `celsius` and `fahrenheit` properties where setting either one updates the other.**

**Answer:**
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius   # store in ONE unit internally

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"Temperature below absolute zero: {value}")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9   # converts and stores via celsius setter (validation reused)

    def __repr__(self):
        return f"Temperature({self._celsius:.2f}°C / {self.fahrenheit:.2f}°F)"

t = Temperature(100)
print(t)              # Temperature(100.00°C / 212.00°F)
t.fahrenheit = 32
print(t.celsius)      # 0.0
t.celsius = -300      # ValueError
```

---

## 8. OOP — Magic / Dunder Methods

---

**Q24. What is the difference between `__str__` and `__repr__`? When is each called?**

**Answer:**

| Method | Purpose | Called by |
|---|---|---|
| `__repr__` | Developer/debug representation — unambiguous, ideally `eval(repr(x)) == x` | `repr()`, REPL, logging, `!r` in f-strings |
| `__str__` | Human-readable — for display | `str()`, `print()`, `format()`, `!s` in f-strings |

```python
class APIEndpoint:
    def __init__(self, method, url):
        self.method = method
        self.url    = url

    def __repr__(self):
        return f"APIEndpoint({self.method!r}, {self.url!r})"   # valid constructor call

    def __str__(self):
        return f"[{self.method}] {self.url}"

ep = APIEndpoint("GET", "https://api.example.com/users")
print(ep)          # [GET] https://api.example.com/users  (calls __str__)
repr(ep)           # APIEndpoint('GET', 'https://api.example.com/users')  (calls __repr__)
f"{ep!r}"          # calls __repr__
f"{ep}"            # calls __str__
```

**Rule:** Always implement `__repr__`. Implement `__str__` only when you want a different human-readable form.

---

**Q25. [CODING] Implement a `TestSuite` class that supports `len()`, indexing `[]`, and `in` operator for test case names.**

**Answer:**
```python
class TestSuite:
    def __init__(self, name):
        self.name   = name
        self._tests = []

    def add(self, test_name):
        self._tests.append(test_name)
        return self   # enables chaining: suite.add("t1").add("t2")

    def __len__(self):
        return len(self._tests)

    def __getitem__(self, index):
        return self._tests[index]    # supports slicing too: suite[1:3]

    def __contains__(self, test_name):
        return test_name in self._tests

    def __iter__(self):
        return iter(self._tests)     # enables for-loop

    def __repr__(self):
        return f"TestSuite({self.name!r}, tests={self._tests})"

suite = TestSuite("Regression")
suite.add("test_login").add("test_checkout").add("test_logout")

print(len(suite))                    # 3
print(suite[0])                      # "test_login"
print("test_checkout" in suite)      # True
print("test_signup" in suite)        # False
for test in suite:
    print(test)
```

---

**Q26. What does `__call__` enable? Implement a callable retry mechanism.**

**Answer:**
`__call__` makes an instance callable like a function. Enables objects that maintain state between calls — perfect for retry logic, rate limiters, or counters.

```python
import time

class Retry:
    def __init__(self, max_attempts=3, delay=1):
        self.max_attempts = max_attempts
        self.delay        = delay
        self.call_count   = 0

    def __call__(self, func, *args, **kwargs):
        self.call_count += 1
        last_exception = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                print(f"Attempt {attempt} failed: {e}")
                if attempt < self.max_attempts:
                    time.sleep(self.delay)
        raise last_exception

retry = Retry(max_attempts=3, delay=0.5)

def flaky_api():
    import random
    if random.random() < 0.7:
        raise ConnectionError("API unavailable")
    return {"status": "ok"}

result = retry(flaky_api)   # retry is called like a function
print(callable(retry))      # True
```

---

## 9. Functional Programming — Lambda, Map, Filter

---

**Q27. What are Python's limitations of `lambda`? When should you prefer a named `def`?**

**Answer:**
Lambda limitations:
1. Single expression only — no statements (`if/else` ternary OK, but not `if/elif/else` blocks)
2. No docstrings
3. No type annotations
4. Harder to test in isolation
5. Stack traces show `<lambda>` — hard to debug

```python
# OK for simple operations
sorted_data = sorted(users, key=lambda u: u["age"])
filtered    = list(filter(lambda x: x > 0, values))

# Use def when logic is complex or reused
def extract_status_code(response_tuple):
    """Extract numeric status code from (url, response) tuple."""
    url, resp = response_tuple
    return resp.get("status_code", 0)

results = sorted(api_responses, key=extract_status_code)
```

---

**Q28. [CODING] Given a list of API response dicts, use `map` and `filter` to extract only successful (2xx) response bodies.**

**Answer:**
```python
responses = [
    {"status": 200, "body": {"user": "alice"}, "url": "/users/1"},
    {"status": 404, "body": {"error": "not found"}, "url": "/users/99"},
    {"status": 201, "body": {"id": 42}, "url": "/posts"},
    {"status": 500, "body": {"error": "server error"}, "url": "/orders"},
    {"status": 200, "body": {"order": "shipped"}, "url": "/orders/5"},
]

is_success  = lambda r: 200 <= r["status"] < 300
get_body    = lambda r: r["body"]

successful_bodies = list(map(get_body, filter(is_success, responses)))
# [{'user': 'alice'}, {'id': 42}, {'order': 'shipped'}]

# More readable with list comprehension (preferred in real code):
successful_bodies = [r["body"] for r in responses if 200 <= r["status"] < 300]
```

---

**Q29. When would you choose `map/filter` over a list comprehension?**

**Answer:**

| | `map` / `filter` | List Comprehension |
|---|---|---|
| Readability | Lower for multi-step | Higher |
| Performance | Lazy (returns iterator) | Eager (creates list) |
| Composability | Easy to chain without materializing | Must nest or use intermediate list |
| Parallel use | Natural with `multiprocessing.Pool.map()` | Less natural |

```python
# Chaining map+filter is lazy — no list created until consumed
pipeline = map(get_body, filter(is_success, filter(has_data, api_stream)))
for item in pipeline:   # processes one at a time — memory efficient for large streams
    process(item)

# Use map/filter when: dealing with large iterables, feeding into other iterators
# Use comprehension when: code clarity matters, result is a list you need immediately
```

---

## 10. Closures & Decorators

---

**Q30. What is a closure? What are the three conditions for a closure to exist?**

**Answer:**
A closure is a function that **remembers variables from its enclosing scope even after that scope has finished executing**.

**Three conditions:**
1. There must be a nested (inner) function
2. The inner function must reference variables from the outer function's scope
3. The outer function must return the inner function (not call it)

```python
def make_multiplier(factor):         # outer function
    def multiply(n):                 # inner function
        return n * factor            # 'factor' is a "free variable" captured in closure
    return multiply                  # return function, not result

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20 — factor=2 is remembered even though make_multiplier() has returned
print(triple(10))  # 30

# Inspect closure variables:
print(double.__closure__[0].cell_contents)   # 2
```

---

**Q31. [CODING] Write a decorator that logs the function name, arguments, return value, and execution time.**

**Answer:**
```python
import time
import functools
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

def log_call(func):
    @functools.wraps(func)              # preserves func.__name__, __doc__, __module__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        logger.debug(f"CALL {func.__name__}(args={args}, kwargs={kwargs})")
        try:
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            logger.debug(f"RETURN {func.__name__} → {result!r} in {elapsed:.4f}s")
            return result
        except Exception as e:
            elapsed = time.perf_counter() - start
            logger.error(f"EXCEPTION {func.__name__} raised {type(e).__name__}: {e} after {elapsed:.4f}s")
            raise
    return wrapper

@log_call
def api_call(endpoint, method="GET"):
    time.sleep(0.1)   # simulate I/O
    return {"status": 200, "data": []}

api_call("/users", method="POST")
```

**Why `functools.wraps`?** Without it, `wrapper.__name__` would be `"wrapper"` — breaking test reports, logging, and debugging. Always use it in decorators.

---

**Q32. [CODING] Implement a memoization decorator using a closure dict. Then explain when Python's `functools.lru_cache` is better.**

**Answer:**
```python
def memoize(func):
    cache = {}                          # closed-over dict — persists between calls
    @functools.wraps(func)
    def wrapper(*args):                 # args must be hashable (no dicts/lists as args)
        if args not in cache:
            cache[args] = func(*args)   # compute and store
        return cache[args]
    wrapper.cache = cache               # expose cache for inspection/clearing
    return wrapper

@memoize
def fetch_user(user_id):
    print(f"  [DB hit] fetching user {user_id}")
    return {"id": user_id, "name": f"user_{user_id}"}

fetch_user(1)   # DB hit
fetch_user(1)   # cache hit — no print
fetch_user(2)   # DB hit
```

**When `lru_cache` is better:**
```python
from functools import lru_cache

@lru_cache(maxsize=128)   # bounded cache — won't grow forever (memory safe)
def expensive_computation(n):
    return n ** 2

expensive_computation.cache_info()    # CacheInfo(hits=0, misses=1, maxsize=128, currsize=1)
expensive_computation.cache_clear()   # reset
```
Use `lru_cache` in production — it's thread-safe, bounded, and exposes cache statistics. Use a manual dict cache only when you need custom eviction logic.

---

**Q33. What is `functools.wraps` and what breaks if you forget it?**

**Answer:**
`@functools.wraps(func)` copies the wrapped function's metadata to the wrapper:
- `__name__`
- `__qualname__`
- `__doc__`
- `__module__`
- `__annotations__`
- `__dict__`

**What breaks without it:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def test_login():
    """Tests the login flow."""
    pass

print(test_login.__name__)  # "wrapper"  — wrong!
print(test_login.__doc__)   # None       — docstring lost!

# Pytest collects test functions by __name__ — all would be named "wrapper"
# Allure reports would show "wrapper" instead of the real test name
# help(test_login) would show wrapper's non-existent docstring
```

---

**Q34. Write a parameterized decorator `@retry(max=3, delay=1)` that retries a function on exception.**

**Answer:**
```python
import time
import functools

def retry(max_attempts=3, delay=0, exceptions=(Exception,)):
    """Parameterized decorator factory."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    print(f"[retry] {func.__name__} attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts and delay:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5, exceptions=(ConnectionError, TimeoutError))
def call_api(url):
    # simulate flaky API
    import random
    if random.random() < 0.8:
        raise ConnectionError("Connection refused")
    return {"status": 200}

result = call_api("https://api.example.com/data")
```

**Key insight:** `@retry(...)` is a **decorator factory** — it returns a decorator, which then wraps the function. Three levels of nesting are required for parameterized decorators.

---

## 11. Iterators

---

**Q35. What is the iterator protocol? What is the difference between an iterable and an iterator?**

**Answer:**

| | Iterable | Iterator |
|---|---|---|
| Definition | Can produce an iterator | Has both `__iter__` and `__next__` |
| Has `__iter__` | Yes — returns an iterator | Yes — returns `self` |
| Has `__next__` | No | Yes — returns next value, raises `StopIteration` when done |
| Reusable | Yes — each `iter()` call produces a fresh iterator | No — exhausted after one pass |
| Examples | `list`, `tuple`, `str`, `dict` | `list_iterator`, generator, file objects |

```python
my_list = [1, 2, 3]       # iterable
it = iter(my_list)        # iterator
print(next(it))           # 1
print(next(it))           # 2
print(next(it))           # 3
print(next(it))           # StopIteration!

# A for loop is equivalent to:
it = iter(my_list)
while True:
    try:
        value = next(it)
        # loop body
    except StopIteration:
        break
```

---

**Q36. [CODING] Implement a custom `PaginatedAPI` iterator that fetches pages lazily.**

**Answer:**
```python
import requests

class PaginatedAPI:
    """Lazily iterates over all pages of a paginated REST API."""

    def __init__(self, base_url, page_size=10):
        self.base_url  = base_url
        self.page_size = page_size
        self._page     = 1
        self._buffer   = []
        self._exhausted = False

    def __iter__(self):
        return self    # iterator IS the iterable

    def __next__(self):
        if not self._buffer:
            if self._exhausted:
                raise StopIteration
            self._fetch_next_page()
        if not self._buffer:
            raise StopIteration
        return self._buffer.pop(0)

    def _fetch_next_page(self):
        # In real code, replace with actual HTTP call
        # response = requests.get(self.base_url, params={"page": self._page, "size": self.page_size})
        # data = response.json()

        # Simulated:
        if self._page > 3:
            self._exhausted = True
            return
        data = [{"id": (self._page - 1) * self.page_size + i} for i in range(self.page_size)]
        self._buffer.extend(data)
        self._page += 1

for user in PaginatedAPI("https://api.example.com/users"):
    print(user)        # fetches pages 1, 2, 3 lazily
```

---

## 12. Generators

---

**Q37. What is a generator? How does `yield` differ from `return`?**

**Answer:**

| | `return` | `yield` |
|---|---|---|
| Function type | Regular function | Generator function |
| Execution | Runs to completion | Suspends and resumes |
| Values produced | One value then terminates | Multiple values, one at a time |
| State | No state between calls | Full local state preserved between `yield`s |
| Memory | Builds entire result | Lazy — one value at a time |

```python
def return_squares(n):
    return [i**2 for i in range(n)]   # builds entire list in memory

def yield_squares(n):
    for i in range(n):
        yield i**2                     # returns one, suspends, resumes on next()

gen = yield_squares(5)
print(type(gen))      # <class 'generator'>
print(next(gen))      # 0
print(next(gen))      # 1
list(gen)             # [4, 9, 16] — consumes remaining
# gen is now exhausted
```

---

**Q38. [CODING] Write a generator to read a large log file line by line and yield only ERROR lines with parsed fields.**

**Answer:**
```python
def parse_error_logs(filepath):
    """
    Memory-efficient log reader — never loads entire file.
    Yields dicts for ERROR-level log lines only.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line or "ERROR" not in line:
                continue
            try:
                parts = [p.strip() for p in line.split("|")]
                yield {
                    "line":      line_num,
                    "timestamp": parts[0],
                    "level":     parts[1],
                    "service":   parts[2],
                    "message":   parts[3] if len(parts) > 3 else ""
                }
            except (IndexError, ValueError) as e:
                yield {"line": line_num, "parse_error": str(e), "raw": line}

# Usage — processes millions of lines without loading into memory
for error in parse_error_logs("app.log"):
    if error.get("service") == "auth_service":
        print(error)
```

---

**Q39. What is a generator expression? When is it better than a list comprehension?**

**Answer:**
Generator expressions use `()` instead of `[]` and produce values lazily.

```python
# List comprehension — eager, allocates full list
squares_list = [x**2 for x in range(1_000_000)]     # ~8 MB in memory

# Generator expression — lazy, O(1) memory
squares_gen  = (x**2 for x in range(1_000_000))      # tiny memory footprint

# When generator expressions are BETTER:
# 1. Feeding into aggregation functions
total = sum(x**2 for x in range(1_000_000))          # sum() consumes generator directly

# 2. Chaining transformations
pipeline = (
    " ".join(line.upper().split())
    for line in open("log.txt")
    if "ERROR" in line
)

# 3. Parsing — generator expression into dict()
log = "user=alice status=active role=admin"
parsed = dict(item.split("=") for item in log.split())
# {'user': 'alice', 'status': 'active', 'role': 'admin'}
```

**Use list comprehension when:** you need to reuse the result, index into it, check length, or iterate more than once.

---

**Q40. What is `yield from`? When would you use it?**

**Answer:**
`yield from` delegates to a sub-generator — transparently forwards all values, exceptions, and the final return value.

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)   # delegate recursively
        else:
            yield item

data = [1, [2, 3, [4, 5]], 6, [[7], 8]]
print(list(flatten(data)))   # [1, 2, 3, 4, 5, 6, 7, 8]

# Without yield from — verbose and doesn't forward .send()/.throw()
def flatten_manual(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            for value in flatten_manual(item):   # manual forwarding
                yield value
        else:
            yield item
```

---

## 13. File Handling & OS Module

---

**Q41. What is a context manager? Why is `with open(...)` preferred over manual `close()`?**

**Answer:**
A context manager handles setup and teardown via `__enter__` and `__exit__` methods. The `with` statement guarantees `__exit__` is called **even if an exception occurs**.

```python
# BAD — file not closed if exception occurs between open() and close()
f = open("data.txt", "r")
data = f.read()     # if this raises, f.close() is never called
f.close()

# GOOD — guaranteed close even on exception
with open("data.txt", "r") as f:
    data = f.read()
# f is automatically closed here

# Multiple files — single with statement
with open("input.txt") as fin, open("output.txt", "w") as fout:
    fout.write(fin.read().upper())
```

---

**Q42. `read()` vs `readline()` vs `readlines()` — when to use each?**

**Answer:**

| Method | Returns | When to use |
|---|---|---|
| `read()` | Entire file as one string | Small files, need full content at once |
| `readline()` | One line per call | Manual streaming, parsing line-by-line |
| `readlines()` | List of all lines | Need to access lines by index, small-medium files |
| `for line in f` | One line per iteration | **Best for large files** — no memory spike |

```python
# readlines() — loads all into memory
with open("large.log") as f:
    lines = f.readlines()   # might exceed RAM for 10GB files

# Generator approach — one line at a time, O(1) memory
def read_lines(path, chunk_size=1000):
    with open(path) as f:
        batch = []
        for line in f:
            batch.append(line.strip())
            if len(batch) >= chunk_size:
                yield batch
                batch = []
        if batch:
            yield batch
```

---

**Q43. [CODING] Walk a directory tree and return a dict mapping file extensions to list of absolute paths.**

**Answer:**
```python
import os
from collections import defaultdict

def categorize_files(root_dir):
    """Returns {'.py': [...], '.json': [...], ...}"""
    result = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            ext = ext.lower() or "(no extension)"
            abs_path = os.path.join(dirpath, filename)
            result[ext].append(abs_path)
    return dict(result)

categories = categorize_files("C:/Users/z041329/Documents/PythonPractice")
for ext, paths in sorted(categories.items()):
    print(f"{ext}: {len(paths)} files")
```

---

**Q44. What is `os.walk()` vs `os.scandir()` vs `os.listdir()`?**

**Answer:**

| Function | Depth | Returns | Performance |
|---|---|---|---|
| `os.listdir(path)` | One level | List of names (strings) | Fast, minimal info |
| `os.scandir(path)` | One level | Iterator of `DirEntry` objects | Fast, has `.is_file()`, `.stat()` without extra syscall |
| `os.walk(path)` | Recursive | `(dirpath, dirnames, filenames)` tuples | Convenient for deep traversal |

```python
import os

# scandir — best when you need file attributes without extra stat() calls
with os.scandir("./data") as entries:
    for entry in entries:
        if entry.is_file() and entry.name.endswith(".json"):
            print(entry.name, entry.stat().st_size)

# walk — best for recursive operations
for root, dirs, files in os.walk("./project"):
    level = root.replace("./project", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    for f in files:
        print(f"{indent}  {f}")
```

---

## 14. Exception Handling

---

**Q45. Explain `try/except/else/finally`. What is the `else` block for — most candidates miss this.**

**Answer:**
```python
def read_config(path):
    try:
        f = open(path)
    except FileNotFoundError:
        print("Config not found — using defaults")
        return {}
    else:
        # Runs ONLY if NO exception was raised in try block
        # Great for code that should only run on success
        # Keeps try block minimal (only potentially-raising code)
        data = f.read()
        f.close()
        return data
    finally:
        # ALWAYS runs — even if return/break/continue in try or except
        # Used for cleanup regardless of outcome
        print("read_config completed")
```

**Why `else` matters:**
- Code in `else` is not protected — exceptions there propagate normally
- Without `else`, you'd put success code inside `try`, accidentally catching exceptions from that code too
- Makes intent explicit: "this code runs only on success"

---

**Q46. What is exception chaining? What does `raise X from Y` do?**

**Answer:**
Exception chaining preserves the original cause of an error while raising a more meaningful exception.

```python
class APIError(Exception):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

def fetch_user(user_id):
    try:
        response = requests.get(f"https://api.example.com/users/{user_id}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout as e:
        raise APIError(f"User fetch timed out for id={user_id}", status_code=408) from e
        # 'from e' attaches original exception as __cause__
        # Traceback shows: "The above exception was the direct cause of..."
    except requests.exceptions.HTTPError as e:
        raise APIError(f"HTTP error for user {user_id}: {e}") from e

# raise X from None — suppresses the original exception in traceback
try:
    int("abc")
except ValueError as e:
    raise ValueError("Invalid user ID format") from None  # hides original traceback
```

---

**Q47. [CODING] Write a custom exception hierarchy for an API test framework.**

**Answer:**
```python
class AutomationError(Exception):
    """Base exception for all automation errors."""
    pass

class APIError(AutomationError):
    def __init__(self, message, status_code=None, url=None):
        super().__init__(message)
        self.status_code = status_code
        self.url         = url

    def __str__(self):
        parts = [super().__str__()]
        if self.status_code: parts.append(f"status={self.status_code}")
        if self.url:         parts.append(f"url={self.url}")
        return " | ".join(parts)

class AuthenticationError(APIError):
    """Raised when auth token is missing or invalid (401/403)."""
    pass

class ResourceNotFoundError(APIError):
    """Raised when resource does not exist (404)."""
    pass

class RateLimitError(APIError):
    """Raised when rate limit is exceeded (429)."""
    def __init__(self, message, retry_after=None, **kwargs):
        super().__init__(message, **kwargs)
        self.retry_after = retry_after

def handle_response(response):
    if response.status_code == 401:
        raise AuthenticationError("Unauthorized", 401, response.url)
    if response.status_code == 404:
        raise ResourceNotFoundError("Resource not found", 404, response.url)
    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", 60))
        raise RateLimitError("Rate limited", retry_after=retry_after, status_code=429, url=response.url)
    if not response.ok:
        raise APIError(f"Unexpected error", response.status_code, response.url)
    return response.json()

# Usage in tests:
try:
    data = handle_response(response)
except AuthenticationError:
    pytest.skip("Auth token expired — skipping test")
except RateLimitError as e:
    time.sleep(e.retry_after)
    data = handle_response(retry_response)
except APIError as e:
    pytest.fail(f"API error: {e}")
```

---

## 15. JSON & Data Processing

---

**Q48. `json.load()` vs `json.loads()` — when do you use each? Same for `dump` / `dumps`.**

**Answer:**

| Function | Input/Output | Use case |
|---|---|---|
| `json.load(file_obj)` | Reads from file | Config files, test fixtures, loading saved responses |
| `json.loads(string)` | Reads from string | API response bodies, parsing in-memory data |
| `json.dump(obj, file_obj)` | Writes to file | Saving test data, writing results |
| `json.dumps(obj)` | Returns string | Logging, request bodies, HTTP payloads |

```python
import json

# Reading
with open("config.json") as f:
    config = json.load(f)                         # file → dict

response_body = '{"status": 200, "data": []}'
data = json.loads(response_body)                  # string → dict

# Writing
with open("output.json", "w") as f:
    json.dump(config, f, indent=4, sort_keys=True)   # dict → file

payload = json.dumps({"user": "alice"})           # dict → string for HTTP body
requests.post(url, data=payload, headers={"Content-Type": "application/json"})
# or: requests.post(url, json={"user": "alice"})  # auto-serializes and sets header
```

---

**Q49. How do you serialize a custom Python object to JSON? Implement a custom encoder.**

**Answer:**
```python
import json
from datetime import datetime, date

class APIResponse:
    def __init__(self, status, data, timestamp):
        self.status    = status
        self.data      = data
        self.timestamp = timestamp  # datetime object

# Method 1: Custom default function
def encode_custom(obj):
    if isinstance(obj, APIResponse):
        return {
            "__type__": "APIResponse",
            "status":    obj.status,
            "data":      obj.data,
            "timestamp": obj.timestamp.isoformat()
        }
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

resp = APIResponse(200, {"user": "alice"}, datetime.now())
print(json.dumps(resp, default=encode_custom, indent=2))

# Method 2: Subclass JSONEncoder (better for complex cases with multiple types)
class AutomationEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if hasattr(obj, "__dict__"):
            return obj.__dict__   # serialize any object's instance attributes
        return super().default(obj)

print(json.dumps(resp, cls=AutomationEncoder, indent=2))
```

---

**Q50. [CODING] Given a deeply nested states JSON, remove the `area_codes` key from every state and save to a new file.**

**Answer:**
```python
import json

def clean_states(input_path, output_path):
    with open(input_path, "r") as f:
        data = json.load(f)

    for state in data:                         # iterate list of states
        state.pop("area_codes", None)          # None default avoids KeyError if missing
        # If nested deeper: state.get("details", {}).pop("area_codes", None)

    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Cleaned data written to {output_path}")

clean_states("data/states.json", "data/new_state.json")
```

---

## 16. API Testing with `requests`

---

**Q51. What is the difference between `requests.get(url, json=...)`, `data=...`, and `params=...`?**

**Answer:**

| Parameter | Placement | Content-Type set? | Use for |
|---|---|---|---|
| `params={"key": "val"}` | URL query string `?key=val` | No | GET filters, pagination |
| `json={"key": "val"}` | Request body (auto-serialized) | `application/json` | POST/PUT REST APIs |
| `data={"key": "val"}` | Request body (form-encoded) | `application/x-www-form-urlencoded` | HTML forms, legacy APIs |
| `data=raw_string` | Request body as-is | Not set (must provide manually) | Raw payload |

```python
import requests

# GET with query params
resp = requests.get("https://api.example.com/users", params={"role": "admin", "page": 2})
# GET https://api.example.com/users?role=admin&page=2

# POST with JSON body
resp = requests.post(
    "https://api.example.com/users",
    json={"name": "Alice", "email": "alice@example.com"},
    headers={"Authorization": "Bearer my_token"}
)

# Best practice: set a timeout ALWAYS
resp = requests.get(url, timeout=10)   # seconds; without this, can hang forever
```

---

**Q52. [CODING] Write a complete CRUD API test helper class with GET, POST, PUT, DELETE.**

**Answer:**
```python
import requests
import json
import logging

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url, token=None, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout  = timeout
        self.session  = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        self.session.headers.update({"Content-Type": "application/json"})

    def _url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _log_response(self, resp):
        logger.debug(f"{resp.request.method} {resp.url} → {resp.status_code}")

    def get(self, endpoint, params=None):
        resp = self.session.get(self._url(endpoint), params=params, timeout=self.timeout)
        self._log_response(resp)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint, body):
        resp = self.session.post(self._url(endpoint), json=body, timeout=self.timeout)
        self._log_response(resp)
        resp.raise_for_status()
        return resp.json()

    def put(self, endpoint, body):
        resp = self.session.put(self._url(endpoint), json=body, timeout=self.timeout)
        self._log_response(resp)
        resp.raise_for_status()
        return resp.json()

    def delete(self, endpoint):
        resp = self.session.delete(self._url(endpoint), timeout=self.timeout)
        self._log_response(resp)
        assert resp.status_code == 204, f"Expected 204, got {resp.status_code}"

# Usage
client = APIClient("https://gorest.co.in/public/v2", token="your_token")

# Create user
new_user = client.post("/users", {"name": "Alice", "email": "alice@test.com", "gender": "female", "status": "active"})
user_id = new_user["id"]

# Read
user = client.get(f"/users/{user_id}")
assert user["name"] == "Alice"

# Update
updated = client.put(f"/users/{user_id}", {"name": "Alice Updated", "email": "alice@test.com", "gender": "female", "status": "active"})
assert updated["name"] == "Alice Updated"

# Delete
client.delete(f"/users/{user_id}")
```

---

**Q53. What is `requests.Session()`? Why use it over individual `requests.get/post` calls?**

**Answer:**
`Session` is a persistent TCP connection that reuses settings and cookies across requests.

**Benefits:**
1. **Connection pooling** — HTTP keep-alive; reuses TCP connection, reducing latency
2. **Persistent headers** — set once, applied to every request (auth token, content type)
3. **Cookie persistence** — session cookies maintained across requests (web scraping, login flows)
4. **Retry adapter** — can attach `HTTPAdapter` with retry logic to the session

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
session.headers.update({"Authorization": "Bearer token123"})

# Attach retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=1,                   # wait 1s, 2s, 4s between retries
    status_forcelist=[429, 500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

# All requests now auto-retry and include auth header
response = session.get("https://api.example.com/data")
```

---

**Q54. How do you handle API authentication with Bearer tokens? What is the difference between Bearer and Basic auth?**

**Answer:**

```python
import requests
from requests.auth import HTTPBasicAuth
import base64

# Bearer Token (OAuth 2.0 / JWT)
headers = {"Authorization": f"Bearer {token}"}
resp = requests.get(url, headers=headers)

# Basic Auth (username:password, Base64 encoded)
resp = requests.get(url, auth=HTTPBasicAuth("user", "password"))
# equivalent: auth=("user", "password")

# API Key in header
resp = requests.get(url, headers={"X-API-Key": api_key})

# API Key as query param (less secure)
resp = requests.get(url, params={"api_key": api_key})
```

| Auth Type | How | When |
|---|---|---|
| Basic Auth | `Authorization: Basic base64(user:pass)` | Legacy systems, simple APIs |
| Bearer Token | `Authorization: Bearer <token>` | OAuth 2.0, JWT, modern REST APIs |
| API Key | Header or query param | Service-to-service, developer APIs |

**Security note:** Never log or print Authorization headers. Store tokens in env vars or a secrets manager, never in code.

---

**Q55. How do you validate a nested JSON API response in automation?**

**Answer:**
```python
def assert_user_response(response, expected_name, expected_email):
    """Validate user API response structure and values."""
    # 1. Status check
    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}: {response.text}"

    body = response.json()

    # 2. Top-level structure
    assert isinstance(body, dict), f"Expected dict, got {type(body).__name__}"
    required_keys = {"id", "name", "email", "status", "created_at"}
    missing = required_keys - body.keys()
    assert not missing, f"Missing keys in response: {missing}"

    # 3. Value assertions
    assert body["name"] == expected_name, \
        f"Name mismatch: expected {expected_name!r}, got {body['name']!r}"
    assert body["email"] == expected_email, \
        f"Email mismatch: expected {expected_email!r}, got {body['email']!r}"

    # 4. Type assertions
    assert isinstance(body["id"], int), f"id should be int, got {type(body['id'])}"

    # 5. Nested validation
    if "address" in body:
        assert "city" in body["address"], "address.city is missing"

    return body

# Schema validation with jsonschema library (production approach):
from jsonschema import validate, ValidationError

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "email"],
    "properties": {
        "id":    {"type": "integer"},
        "name":  {"type": "string", "minLength": 1},
        "email": {"type": "string", "format": "email"},
    },
    "additionalProperties": True
}

try:
    validate(instance=body, schema=USER_SCHEMA)
except ValidationError as e:
    pytest.fail(f"Schema validation failed: {e.message}")
```

---

## 17. Logging

---

**Q56. Explain Python's logging hierarchy and how log levels work.**

**Answer:**
Python logging has a hierarchy of loggers connected in a parent-child relationship separated by dots: `root → myapp → myapp.api → myapp.api.users`.

**Log levels (ascending severity):**
| Level | Numeric | Use case |
|---|---|---|
| `DEBUG` | 10 | Detailed diagnostic info — variable values, flow |
| `INFO` | 20 | General operational events — start/stop, config |
| `WARNING` | 30 | Something unexpected but not an error |
| `ERROR` | 40 | Error — operation failed but app continues |
| `CRITICAL` | 50 | Serious error — app may be unable to continue |

```python
import logging

# Root logger — global default
logging.basicConfig(level=logging.INFO)
logging.warning("This logs")   # root logger
logging.debug("This does NOT log — below INFO threshold")

# Named logger — recommended for libraries/frameworks
logger = logging.getLogger("myapp.api")  # child of "myapp", child of root
logger.setLevel(logging.DEBUG)           # override threshold for this logger
```

---

**Q57. [CODING] Create a logger with both console and file handlers, different formats, and which doesn't propagate to root.**

**Answer:**
```python
import logging
import os
from logging.handlers import RotatingFileHandler

def create_logger(name, log_file, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False   # don't pass to root logger — avoids duplicate prints

    if logger.handlers:   # avoid adding handlers if already configured (e.g., on reload)
        return logger

    # Console handler — INFO and above, concise format
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    ))

    # File handler — DEBUG and above, detailed format, rotates at 5MB
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

logger = create_logger("api_test", "logs/api_test.log")
logger.debug("Request payload: %s", payload)    # only to file
logger.info("Test started: test_create_user")   # to console and file
logger.error("Assertion failed: %s", error)
```

---

**Q58. What is the difference between `logging.basicConfig()` and using a logger with handlers? When would you use each?**

**Answer:**

| | `basicConfig()` | Named logger + handlers |
|---|---|---|
| Setup | One line | Several lines |
| Scope | Root logger — affects all loggers | Specific to one logger |
| Multiple outputs | Can configure file OR stream, not both easily | Both simultaneously, different levels |
| Production use | Scripts, quick tests | Libraries, frameworks, production apps |
| Reconfiguration | No effect after first call | Can be updated at runtime |

```python
# basicConfig — fine for simple scripts
logging.basicConfig(
    level=logging.DEBUG,
    filename="run.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s"
)

# Named logger with handlers — production/framework code
# (see previous question for full implementation)
```

**Automation framework best practice:** Use a named logger per module (`logger = logging.getLogger(__name__)`). Configure handlers in your test session entry point (e.g., pytest `conftest.py`), never inside test files.

---

## 18. Threading & Multiprocessing

---

**Q59. What is the GIL (Global Interpreter Lock)? How does it affect threading in Python?**

**Answer:**
The GIL is a mutex in CPython that allows only **one thread to execute Python bytecode at a time**, even on multi-core systems.

**Impact:**

| Workload | Threading | Multiprocessing |
|---|---|---|
| I/O-bound (network, disk, DB) | Effective — GIL released during I/O | Overkill — threads work fine |
| CPU-bound (calculations, data processing) | No speedup — GIL blocks parallel execution | Effective — separate processes, each with own GIL |

```python
import threading
import time

def io_task(n):
    time.sleep(2)   # simulates network call — GIL released during sleep

# Sequential: 4 seconds
for i in range(4): io_task(i)

# Threaded: ~2 seconds — I/O tasks overlap
threads = [threading.Thread(target=io_task, args=(i,)) for i in range(4)]
for t in threads: t.start()
for t in threads: t.join()
```

**In automation:** API tests are I/O-bound — threading (or `asyncio`) is the right tool. Never use multiprocessing for simple HTTP request parallelism.

---

**Q60. [CODING] Run 5 API requests in parallel using threading. Time the sequential vs parallel execution.**

**Answer:**
```python
import threading
import time
import requests
from typing import List, Dict

def fetch_user(user_id: int, results: List, index: int):
    """Worker function — stores result in shared list at index."""
    try:
        resp = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=5
        )
        results[index] = resp.json()
    except Exception as e:
        results[index] = {"error": str(e)}

user_ids = [1, 2, 3, 4, 5]

# Sequential
start = time.perf_counter()
seq_results = [None] * len(user_ids)
for i, uid in enumerate(user_ids):
    fetch_user(uid, seq_results, i)
seq_time = time.perf_counter() - start
print(f"Sequential: {seq_time:.2f}s")

# Parallel with threads
start = time.perf_counter()
par_results = [None] * len(user_ids)
threads = [
    threading.Thread(target=fetch_user, args=(uid, par_results, i))
    for i, uid in enumerate(user_ids)
]
for t in threads: t.start()
for t in threads: t.join()
par_time = time.perf_counter() - start
print(f"Parallel:   {par_time:.2f}s — {seq_time / par_time:.1f}x speedup")
```

---

**Q61. When would you use `multiprocessing` over `threading` in an automation context?**

**Answer:**
Use `multiprocessing` when:
1. **CPU-bound report generation** — parsing large log files, comparing screenshots pixel-by-pixel
2. **Process isolation** — test suites that can't share state (different DB connections, different browsers)
3. **Bypassing GIL** — heavy data transformations on test result data

```python
import multiprocessing
import os

def run_test_suite(suite_name):
    print(f"Running {suite_name} in PID {os.getpid()}")
    # Each suite runs in its own process — completely isolated
    return {"suite": suite_name, "status": "passed"}

if __name__ == "__main__":   # REQUIRED for multiprocessing on Windows
    suites = ["smoke_tests", "regression_tests", "api_tests", "ui_tests"]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(run_test_suite, suites)

    for r in results:
        print(r)
```

---

**Q62. What is a race condition? How do you prevent it with a `Lock`?**

**Answer:**
A race condition occurs when multiple threads read and write shared state, and the outcome depends on thread execution order.

```python
import threading

# RACE CONDITION — counter may not reach 10000
counter = 0
def increment():
    global counter
    for _ in range(10000):
        counter += 1   # read-modify-write — not atomic!

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)   # likely less than 100000 — race condition!

# FIXED — with Lock
lock    = threading.Lock()
counter = 0

def safe_increment():
    global counter
    for _ in range(10000):
        with lock:      # acquires lock, releases in __exit__
            counter += 1

threads = [threading.Thread(target=safe_increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)   # always 100000
```

**In automation:** Shared report writers, result aggregators, and database connections all need locking when accessed from multiple test threads.

---

## 19. Data Structures — Linked List

---

**Q63. Implement a singly linked list with `insert_at_end`, `insert_at_beginning`, `delete`, and `display`.**

**Answer:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        print(" → ".join(values) + " → None")

    def reverse(self):
        prev    = None
        current = self.head
        while current is not None:
            nxt          = current.next
            current.next = prev
            prev         = current
            current      = nxt
        self.head = prev

ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(5)
ll.display()           # 5 → 10 → 20 → 30 → None
ll.delete(10)
ll.display()           # 5 → 20 → 30 → None
ll.reverse()
ll.display()           # 30 → 20 → 5 → None
```

---

**Q64. [CODING] Detect a cycle in a linked list (Floyd's Tortoise and Hare).**

**Answer:**
```python
def has_cycle(head):
    """Floyd's cycle detection — O(n) time, O(1) space."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next          # moves 1 step
        fast = fast.next.next     # moves 2 steps
        if slow is fast:
            return True           # they meet → cycle exists
    return False

# Create a cycle for testing
ll = SinglyLinkedList()
for i in [1, 2, 3, 4, 5]:
    ll.insert_at_end(i)

# Manually create cycle: node 5 points back to node 3
node5 = ll.head
while node5.next: node5 = node5.next   # reach last node
node3 = ll.head
for _ in range(2): node3 = node3.next  # reach node 3

node5.next = node3   # create cycle

print(has_cycle(ll.head))   # True
```

---

## 20. Advanced Python — Metaclasses, Memory Model & Internals

---

**Q65. What is a metaclass? What does `type` have to do with it?**

**Answer:**
A metaclass is a class whose instances are classes. By default, every Python class is an instance of `type`.

```python
# Every class is an instance of type
class MyClass:
    pass

print(type(MyClass))     # <class 'type'>
print(type(int))         # <class 'type'>
print(type(type))        # <class 'type'>  — type is its own metaclass!

# type() can CREATE classes dynamically:
# type(name, bases, dict)
Dog = type("Dog", (object,), {
    "species": "Canis lupus familiaris",
    "bark": lambda self: f"{self.name} says Woof!"
})
rex = Dog()
rex.name = "Rex"
print(rex.bark())   # Rex says Woof!

# Custom metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connected = True

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)   # True — same instance (Singleton)
```

---

**Q66. What is the Singleton pattern? Implement it three different ways in Python.**

**Answer:**
Singleton ensures only one instance of a class exists throughout the application lifetime.

```python
# Method 1: Metaclass (shown above)

# Method 2: __new__ method
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        # __init__ is called every time — use guard or store in __new__
        if not hasattr(self, "_initialized"):
            self.value        = value
            self._initialized = True

s1 = Singleton("first")
s2 = Singleton("second")
print(s1 is s2)   # True
print(s1.value)   # "first" — init only ran once

# Method 3: Module-level (most Pythonic — modules are singletons by nature)
# config.py
class Config:
    debug = False
    base_url = "https://api.example.com"

config = Config()   # create once at module level

# In tests:
# from config import config — always gets the same object
```

---

**Q67. What are `__slots__`? When would you use them in an automation framework?**

**Answer:**
`__slots__` replaces the instance `__dict__` with a fixed set of attribute names, reducing memory and preventing typo-attribute creation.

```python
class TestResult:
    __slots__ = ("test_name", "status", "duration", "error_message")

    def __init__(self, test_name, status, duration, error_message=None):
        self.test_name     = test_name
        self.status        = status
        self.duration      = duration
        self.error_message = error_message

# Benefits:
r = TestResult("test_login", "PASS", 0.5)
r.typo_attribute = "oops"   # AttributeError! — caught at runtime, not silently created

# Memory comparison:
class A:           pass     # has __dict__ — ~200 bytes per instance overhead
class B:
    __slots__ = ("x","y")   # ~50 bytes per instance

# For test result objects in a large test run (10k tests), __slots__ can save significant memory
```

---

**Q68. Explain Python's garbage collection. What are reference cycles and how does the cyclic GC handle them?**

**Answer:**
Python uses **reference counting** as its primary garbage collection strategy — every object keeps a count of how many references point to it. When count reaches 0, the object is immediately deallocated.

```python
import sys
a = [1, 2, 3]
print(sys.getrefcount(a))   # 2 (a + the getrefcount argument)
b = a
print(sys.getrefcount(a))   # 3 (a, b, getrefcount argument)
del b
print(sys.getrefcount(a))   # 2 again
```

**Reference cycles** defeat reference counting:
```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b   # a → b
b.ref = a   # b → a — reference cycle!

del a
del b
# Both objects still have refcount=1 (from each other) — leak with pure refcounting
```

**Cyclic GC (module `gc`)** runs periodically to find and collect unreachable cycles:
```python
import gc
gc.enable()                # usually on by default
gc.collect()               # force a collection cycle
print(gc.get_count())      # (gen0, gen1, gen2) — generational counts

# In long-running automation processes, circular references in page objects can cause leaks
# Use weakref for back-references:
import weakref
class Parent:
    def __init__(self):
        self.child = None

class Child:
    def __init__(self, parent):
        self.parent = weakref.ref(parent)   # weak reference — doesn't increment refcount
```

---

**Q69. What are context managers? Implement a custom one using both `__enter__`/`__exit__` and `contextlib.contextmanager`.**

**Answer:**
```python
# Method 1: Class-based context manager
class DatabaseTransaction:
    def __init__(self, connection):
        self.conn = connection

    def __enter__(self):
        self.conn.begin()
        return self.conn   # value bound to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
            # Return False (or None) to re-raise exception
            # Return True to suppress exception
        return False

with DatabaseTransaction(conn) as transaction:
    transaction.execute("INSERT INTO users ...")

# Method 2: contextlib.contextmanager — cleaner for simple cases
from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield          # code in 'with' block runs here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed:.4f}s")

with timer("API call"):
    requests.get("https://api.example.com/users")

# In automation — mock context manager
@contextmanager
def mock_response(status_code, body):
    """Replace requests.get with a mock for unit testing."""
    original = requests.get
    requests.get = lambda *a, **kw: MockResponse(status_code, body)
    try:
        yield
    finally:
        requests.get = original
```

---

**Q70. What is `__init__.py` and how does it affect imports in a test framework? Explain relative vs absolute imports.**

**Answer:**
`__init__.py` marks a directory as a **Python package**. It can be empty or contain package-level initialization.

```
tests/
    __init__.py
    conftest.py
    unit/
        __init__.py
        test_api_client.py
    integration/
        __init__.py
        test_user_flow.py
    utils/
        __init__.py
        helpers.py
```

```python
# Absolute import (recommended — explicit, works from any location)
from tests.utils.helpers import generate_test_user
from tests.unit.test_api_client import APIClient

# Relative import (intra-package — fragile if package structure changes)
from ..utils.helpers import generate_test_user    # two levels up, then utils
from .helpers import generate_test_user           # same package

# In __init__.py — control public API of your package
# tests/utils/__init__.py
from .helpers import generate_test_user, clean_test_data
# Now: from tests.utils import generate_test_user
```

**Best practice for pytest:** Keep `__init__.py` files in test directories to prevent import conflicts when module names collide across test directories.

---

## Bonus: Automation-Specific Scenario Questions

---

**Q71. An API test that was passing suddenly started failing intermittently. How do you diagnose and fix it?**

**Answer (structured approach):**

1. **Gather data first:**
   - Check failure frequency: once? always? certain times of day?
   - Look at the exact error: `AssertionError`, `ConnectionError`, `TimeoutError`, `JSONDecodeError`?
   - Review CI/CD logs for patterns

2. **Common causes and fixes:**

   ```python
   # Race condition — API not ready
   # FIX: add polling/wait
   def wait_for_status(client, resource_id, expected_status, max_wait=30):
       deadline = time.time() + max_wait
       while time.time() < deadline:
           data = client.get(f"/resources/{resource_id}")
           if data["status"] == expected_status:
               return data
           time.sleep(0.5)
       raise TimeoutError(f"Status never became {expected_status}")

   # Hardcoded delays — brittle
   # time.sleep(5)  # BAD
   # Use explicit waits instead (above)

   # Timeout too low — occasional slow responses
   # FIX: tune timeout, add retry
   @retry(max_attempts=3, delay=1, exceptions=(Timeout,))
   def get_user(client, user_id):
       return client.get(f"/users/{user_id}", timeout=10)

   # Test order dependency — test relies on state from previous test
   # FIX: each test creates its own data, cleans up in fixture teardown
   @pytest.fixture
   def test_user(client):
       user = client.post("/users", {"name": "temp", "email": f"temp-{uuid.uuid4()}@test.com"})
       yield user
       client.delete(f"/users/{user['id']}")   # teardown
   ```

---

**Q72. How would you design a Page Object Model (POM) in Python using OOP concepts you've learned?**

**Answer:**
```python
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class BasePage(ABC):
    """Abstract base for all page objects."""

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def is_loaded(self) -> bool:
        """Verify the page is fully loaded."""
        ...

    def wait_for_load(self, timeout=10):
        import time
        deadline = time.time() + timeout
        while not self.is_loaded():
            if time.time() > deadline:
                raise TimeoutError(f"{self.__class__.__name__} did not load in {timeout}s")
            time.sleep(0.5)
        return self   # method chaining

    def _find(self, locator):
        logger.debug(f"Finding element: {locator}")
        return self.driver.find_element(*locator)

    def _click(self, locator):
        element = self._find(locator)
        logger.info(f"Clicking: {locator}")
        element.click()

class LoginPage(BasePage):
    USERNAME_INPUT = ("id", "username")
    PASSWORD_INPUT = ("id", "password")
    LOGIN_BUTTON   = ("css selector", "button[type='submit']")
    ERROR_MESSAGE  = ("class name", "error-msg")

    def is_loaded(self):
        try:
            return self._find(self.LOGIN_BUTTON).is_displayed()
        except Exception:
            return False

    def login(self, username, password):
        self._find(self.USERNAME_INPUT).send_keys(username)
        self._find(self.PASSWORD_INPUT).send_keys(password)
        self._click(self.LOGIN_BUTTON)
        return self   # return self for chaining, or return DashboardPage(self.driver)

    @property
    def error_message(self):
        try:
            return self._find(self.ERROR_MESSAGE).text
        except Exception:
            return None

# Usage
login_page = LoginPage(driver)
login_page.wait_for_load().login("alice", "password123")
```

---

**Q73. How would you use generators to implement a lazy test data factory?**

**Answer:**
```python
import itertools
import uuid

def user_factory(base_name="testuser", base_email_domain="test.com"):
    """Infinite generator of unique test users."""
    counter = itertools.count(1)
    while True:
        n = next(counter)
        yield {
            "name":   f"{base_name}_{n}",
            "email":  f"{base_name}_{n}@{base_email_domain}",
            "id":     str(uuid.uuid4()),
            "active": True
        }

def take(n, generator):
    """Take first n items from a generator."""
    return [next(generator) for _ in range(n)]

users = user_factory()
ten_users = take(10, users)
single_user = next(users)   # continues from where it left off

# Parameterized test data via generator
def api_test_cases():
    for method in ["GET", "POST", "PUT", "DELETE"]:
        for status in [200, 400, 401, 403, 404, 500]:
            yield {"method": method, "status": status}

import pytest
@pytest.mark.parametrize("case", list(api_test_cases()))
def test_response_handler(case):
    ...
```

---

**Q74. Explain how decorators are used in popular Python test frameworks (pytest, unittest).**

**Answer:**
```python
import pytest
import functools

# pytest.mark.* — built-in decorator markers
@pytest.mark.smoke
@pytest.mark.parametrize("username,password,expected", [
    ("admin", "admin123", True),
    ("guest", "wrong", False),
    ("", "", False),
])
def test_login(username, password, expected):
    ...

# Custom decorator to add Allure step
def allure_step(title):
    """Wraps function as an Allure test step."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import allure
            with allure.step(title):
                return func(*args, **kwargs)
        return wrapper
    return decorator

@allure_step("Enter login credentials")
def enter_credentials(page, username, password):
    page.username.send_keys(username)
    page.password.send_keys(password)

# Fixture as decorator (pytest)
@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url=os.getenv("API_BASE_URL"))
    yield client
    client.session.close()   # teardown

@pytest.fixture(autouse=True)
def log_test_name(request):
    logger.info(f"=== START: {request.node.name} ===")
    yield
    logger.info(f"=== END: {request.node.name} ===")
```

---

*End of Interview Q&A*

---

> **Study tip:** For each question, try to code the answer from memory first, then compare. Focus on the "why" behind each concept — interviewers probe depth, not just syntax.
