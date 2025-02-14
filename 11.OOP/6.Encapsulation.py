'''Encapsulation in Python
Encapsulation is a fundamental concept in Object-Oriented Programming (OOP) that refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. It also restricts direct access to some of an object's components, which is a way of preventing accidental interference and misuse of the internal workings of an object.

In simpler terms, encapsulation allows an object to hide its internal data and control how it's accessed or modified through methods, protecting the integrity of that data.'''


'''Key Concepts of Encapsulation
Data Hiding: It prevents the direct access to the object's internal state, only allowing it to be changed through methods.
Controlled Access: Through encapsulation, you can control how the attributes of a class are accessed and modified.
Security: Sensitive data can be kept private within an object, ensuring that it is only accessible in controlled ways.'''

'''Types of Encapsulation
In Python, there are three levels of access control:

Public Members:
Attributes and methods that are accessible from anywhere.
Example: self.name.
Protected Members:
Attributes and methods that are accessible within the class and its subclasses, but not outside.
Marked with a single underscore _attribute.
Example: self._name.
Private Members:
Attributes and methods that are only accessible within the class where they are defined, not from outside or even subclasses.
Marked with a double underscore __attribute.
Example: self.__name.
'''


# Example of Encapsulation in Python
# Here’s an example demonstrating all three types of access modifiers:

class Car:
    def __init__(self, brand, year):
        # Public attribute
        self.brand = brand
        
        # Protected attribute
        self._year = year
        
        # Private attribute
        self.__owner = "John Doe"
    
    # Public method
    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self._year}")
    
    # Private method
    def __private_method(self):
        print("This is a private method.")
    
    # Method to modify the private attribute
    def set_owner(self, new_owner):
        self.__owner = new_owner
    
    # Method to access the private attribute
    def get_owner(self):
        return self.__owner

# Creating an object of Car
car = Car("Toyota", 2022)

# Accessing the public attribute
print(car.brand)  # Output: Toyota

# Accessing the protected attribute
print(car._year)  # Output: 2022

# Accessing the public method
car.display_info()  # Output: Brand: Toyota, Year: 2022

# Trying to access the private attribute directly will cause an error
# print(car.__owner)  # Raises AttributeError

# Accessing the private attribute using the method
print(car.get_owner())  # Output: John Doe

# Trying to access private method directly will cause an error
# car.__private_method()  # Raises AttributeError

# Modifying private attribute using setter method
car.set_owner("Alice")
print(car.get_owner())  # Output: Alice


'''Explanation:
Public Attributes/Methods: The brand attribute and display_info() method can be accessed from anywhere.
Protected Attributes: The _year attribute is meant to be accessed within the class or a subclass but can still be accessed directly (though it's not recommended).
Private Attributes/Methods: The __owner attribute and __private_method() are private and cannot be accessed directly from outside the class. They can only be accessed through getter/setter methods like get_owner() and set_owner().'''


'''Benefits of Encapsulation
Security: Sensitive data is protected and cannot be directly accessed from outside the class.
Control: You can control how the data is accessed or modified by exposing only relevant methods.
Flexibility: Internal details can be changed without affecting other parts of the code that depend on the encapsulated class.
Ease of Use: It simplifies the understanding of how data is managed, as users only see what’s necessary for them to interact with.'''



# Real-Life Example of Encapsulation
# Let's say you have a bank account system where certain data such as balance should be hidden, and it can only be modified or accessed through controlled methods like deposit or withdrawal:

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")
    
    def get_balance(self):
        return self.__balance

# Creating an object of BankAccount
account = BankAccount("123456789", 1000)

# Accessing the balance through the getter method
print(account.get_balance())  # Output: 1000

# Depositing money
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Trying to withdraw more than the balance
account.withdraw(2000)  # Output: Invalid withdrawal amount.

# Withdrawing money
account.withdraw(300)
print(account.get_balance())  # Output: 1200
# Here, the __balance is a private attribute, and it's only modified through methods like deposit() and withdraw().


'''🔍 What is Encapsulation?
💡 Encapsulation means "hiding important data and allowing only safe access."

Think about your piggy bank (moneybox) 🐷.

You put money inside 💰, but no one can directly take it out.
There is only one way to access it—by opening it properly.
This keeps your money safe!
👉 That’s encapsulation! We hide data and provide secure access.
'''

'''🏦 Real-Life Example: ATM Machine (Banking System)
Imagine you have a bank account.

Can anyone take money from your account? ❌ NO!
You need a PIN (password) to access your money. 🔑
The bank keeps your account details hidden (private).
👉 This is Encapsulation—hiding account details and giving safe access!
'''
# 📌 Encapsulation in Python (Bank System Example)

class BankAccount:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number  # Public Attribute
        self.__balance = balance  # Private Attribute (Hidden)
        self.__pin = pin  # Private Attribute (Hidden)

    def deposit(self, amount):
        """Allow depositing money safely."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Deposit amount must be greater than zero!")

    def withdraw(self, amount, entered_pin):
        """Allow withdrawal only if PIN is correct."""
        if entered_pin == self.__pin:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New Balance: ${self.__balance}")
            else:
                print("Insufficient balance or invalid amount!")
        else:
            print("Incorrect PIN! Access Denied.")

    def get_balance(self, entered_pin):
        """Allow viewing balance only if PIN is correct."""
        if entered_pin == self.__pin:
            print(f"Your balance is: ${self.__balance}")
        else:
            print("Incorrect PIN! Access Denied.")

# Create a Bank Account
my_account = BankAccount(account_number=123456, balance=1000, pin=1234)

# User tries to deposit money
my_account.deposit(500)  # ✅ Deposited $500. New Balance: $1500

# User tries to withdraw money with correct PIN
my_account.withdraw(200, 1234)  # ✅ Withdrew $200. New Balance: $1300

# User tries to withdraw money with incorrect PIN
my_account.withdraw(300, 1111)  # ❌ Incorrect PIN! Access Denied.

# User tries to check balance with correct PIN
my_account.get_balance(1234)  # ✅ Your balance is: $1300

# User tries to check balance with incorrect PIN
my_account.get_balance(0000)  # ❌ Incorrect PIN! Access Denied.

# Trying to access private variables (Not Allowed)
# print(my_account.__balance)  ❌ ERROR! Cannot access private variable
# print(my_account.__pin)      ❌ ERROR! Cannot access private variable


# 🔍 Explanation of Encapsulation in the Code
'''1️⃣ self.__balance and self.__pin are PRIVATE (__ before name)
Cannot be accessed directly from outside.
Only the class methods (deposit, withdraw, get_balance) can access them.

2️⃣ Users can ONLY deposit, withdraw, or check balance using methods
If someone tries to access __balance directly, Python won't allow it! 🚫

3️⃣ PIN is required to withdraw or check balance

Keeps the account secure just like a real ATM! 🔒
🎯 Why Use Encapsulation?
✅ Hides sensitive data (No direct access to __balance or __pin).
✅ Protects data from accidental changes (No one can modify balance directly).
✅ Controls how data is accessed (Users need a PIN for security).
✅ Used in real-world applications like ATMs, banking apps, and password storage.

🔥 Industry Example: Online Payment System
Imagine PayPal or Google Pay.

You cannot directly access your account balance.
You must log in and verify to view or transfer money.
The account balance is private (hidden), and you need secure methods to access it.
👉 Encapsulation makes online banking secure! 🚀'''



# what is the difference betweeen abstraction and encapsulation 

# 🔍 Difference Between Abstraction & Encapsulation in Python
# Abstraction = Hiding complex logic 🛠️
# Encapsulation = Hiding data & controlling access 🔒

'''🎭 Abstraction Example (Hiding Complex Logic)
💡 Imagine driving a car:

You turn the steering wheel → The car moves.
You press the brake → The car stops.
👉 Do you know how the engine works inside? ❌ No!
👉 You only see the buttons & controls → That’s abstraction! 🚗'''

# 📌 Python Code Example: Abstraction

from abc import ABC, abstractmethod

# Abstract Class (Hides Complex Logic)
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass  # Only an idea, no implementation

# Concrete Class (Actual Implementation)
class Car(Vehicle):
    def start(self):
        print("Car engine starts with a key or button!")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick or button!")

# Using the classes
my_car = Car()
my_bike = Bike()

my_car.start()  # Output: Car engine starts with a key or button!
my_bike.start()  # Output: Bike starts with a kick or button!
# ✅ The driver doesn't care HOW the engine starts, just that it works!
# ✅ Hides the complex details of the engine—That’s abstraction!

'''🔒 Encapsulation Example (Hiding Data)
💡 Imagine a bank account:

You cannot see the balance directly.
You must enter a PIN to check it.
👉 The balance is hidden inside the bank system → That’s encapsulation!'''

# 📌 Python Code Example: Encapsulation

class BankAccount:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number  # Public Attribute
        self.__balance = balance  # Private Attribute (Hidden)
        self.__pin = pin  # Private Attribute (Hidden)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount, entered_pin):
        if entered_pin == self.__pin:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New Balance: ${self.__balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect PIN! Access Denied.")

    def get_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print(f"Your balance is: ${self.__balance}")
        else:
            print("Incorrect PIN! Access Denied.")

# Creating a bank account
my_account = BankAccount(account_number=123456, balance=1000, pin=1234)

# Depositing money
my_account.deposit(500)  # ✅ Deposited $500. New Balance: $1500

# Trying to withdraw money with incorrect PIN
my_account.withdraw(200, 1111)  # ❌ Incorrect PIN! Access Denied.

# Trying to check balance with correct PIN
my_account.get_balance(1234)  # ✅ Your balance is: $1500

# Trying to access private variables (Not Allowed)
# print(my_account.__balance)  ❌ ERROR! Cannot access private variable
# ✅ The balance and PIN are hidden inside the system!
# ✅ Only deposit, withdraw, and get_balance can access them!

'''💡 Key Takeaways
🔹 Abstraction
✔ Hides how things work and shows only necessary details
✔ Achieved using abstract classes & methods
✔ Example: Car controls hide engine details

🔹 Encapsulation
✔ Hides sensitive data and protects it from direct access
✔ Achieved using private variables & methods
✔ Example: ATM hides account balance, needs PIN to access

🚀 Industry Example: Banking System
Abstraction 🎭 → You can transfer money using a banking app, but you don’t see the backend code that connects banks.
Encapsulation 🔒 → Your bank balance & PIN are private, and you can access them only through secure functions.

👉 Both are used together in real-world applications! 🚀
'''
