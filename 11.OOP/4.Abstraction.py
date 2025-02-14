'''Abstraction in Python
Abstraction is one of the key principles of Object-Oriented Programming (OOP). It involves hiding the internal details and showing only the essential features of an object. By using abstraction,
we simplify complex systems by breaking them down into more manageable parts and hiding unnecessary details.

- In Python, abstraction is achieved using abstract classes and interfaces. 
- Python uses the abc module to implement abstract classes and methods.

Key Features of Abstraction:
- Simplification: It hides the complex implementation details and shows only the necessary information.
- Modularity: By dividing the program into independent modules, it makes maintenance and updating easier.
- Reusability: Abstract classes can be extended to other classes, enhancing code reusability.
- Maintainability: Since complex logic is hidden, the system becomes easier to maintain.

# Types of Abstraction
There are two types of abstraction in programming:

1. Data Abstraction: Focuses on what data an object should have and hides how this data is maintained or manipulated. For instance, in a bank application, the user is aware of the functionalities like deposit, withdraw, etc., but doesn't know the internal working of these operations.

2. Control Abstraction: Focuses on hiding how an object does something and instead describes what should be done. It allows users to interact with objects or systems by calling methods, without needing to understand the detailed logic behind them.

# Abstract Classes in Python
- An abstract class is a class that cannot be instantiated directly. It contains one or more abstract methods, which are methods declared but contain no implementation. These classes are designed to be inherited, and the derived classes must implement the abstract methods.

How to Create an Abstract Class:
To create an abstract class in Python:

Import the abc module.
Use ABC as a base class for your abstract class.
Define methods with the @abstractmethod decorator.'''


from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("This animal sleeps.")

# Concrete class
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!
dog.sleep()         # Output: This animal sleeps.

'''In this example:

Animal is an abstract class with the abstract method sound().
Dog and Cat are concrete classes that inherit from Animal and implement the sound() method.
Why Use Abstract Classes?
Enforce a Contract: Abstract classes enforce that subclasses must implement certain methods, ensuring consistency across related classes.
Polymorphism: Subclasses can provide different implementations of abstract methods, offering flexibility through polymorphism.
'''


'''Real-Life Problem Solved Using Abstraction
Let’s consider a real-life example involving vehicles. You want to create a system where vehicles like cars and motorcycles can perform actions like starting and stopping, but the details of how they perform these actions will vary depending on the type of vehicle.

Problem: Vehicle System
You want to design a system where:

All vehicles should have start() and stop() methods.
Cars and motorcycles will have different ways to start and stop, but all vehicles should adhere to this structure.'''

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    
    def showNecessaryInfo():
        print(f"this is the necessary info")

# Concrete class for Car
class Car(Vehicle):
    def start(self):
        print("Starting the car engine.")
    
    def stop(self):
        print("Stopping the car engine.")

# Concrete class for Motorcycle
class Motorcycle(Vehicle):
    def start(self):
        print("Starting the motorcycle engine.")

    def stop(self):
        print("Stopping the motorcycle engine.")

# Usage
def operate_vehicle(vehicle):
    vehicle.start()
    vehicle.stop()

# Instantiating the concrete classes
car = Car()
motorcycle = Motorcycle()

# Operating vehicles
operate_vehicle(car)         # Output: Starting the car engine. Stopping the car engine.
operate_vehicle(motorcycle)  # Output: Starting the motorcycle engine. Stopping the motorcycle engine.


'''In this example:

Abstraction is used to define the high-level functionality (start and stop) for all types of vehicles.
The abstract class Vehicle ensures that every vehicle must implement these methods.
Concrete classes Car and Motorcycle implement their specific logic for starting and stopping the vehicle.
Advantages of Abstraction in Problem Solving:
Simplification: The Vehicle abstract class allows you to define the necessary structure without worrying about how individual vehicles start or stop.
Extensibility: You can easily add new types of vehicles (e.g., Truck, Bicycle) by extending the Vehicle class and implementing their specific behaviors.
Maintainability: Since the core structure is defined in one place, adding or modifying functionality becomes easier.
Reusability: The start() and stop() methods are reusable for all vehicle types without repeating code.

'''

from abc import ABC, abstractmethod

# Abstract Class (Hides Complex Logic)
class Bank(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Store account number
        self.balance = balance  # Store balance
        self.transactions = []  # Store transaction history

    @abstractmethod
    def deposit(self, amount):
        """Abstract method for deposit - Must be implemented in subclasses"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method for withdrawal - Must be implemented in subclasses"""
        pass

    def show_balance(self):
        """Show the current account balance"""
        print(f"Account {self.account_number} - Your balance is: ${self.balance}")

    def show_transactions(self):
        """Show the transaction history"""
        print(f"\nTransaction History for Account {self.account_number}:")
        if not self.transactions:
            print("No transactions yet!")
        else:
            for transaction in self.transactions:
                print(transaction)

# Concrete Class (Actual Implementation)
class MyBank(Bank):
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            print("Deposit amount must be greater than zero!")
        else:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}. New Balance: ${self.balance}")
            print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
        elif self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}. New Balance: ${self.balance}")
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            self.transactions.append(f"Failed withdrawal of ${amount} due to insufficient funds.")
            print("Insufficient funds!")

# Using the Bank System
account = MyBank(account_number=123456, balance=500)  # Create a bank account with $500 balance

account.show_balance()        # Show current balance
account.deposit(200)          # Deposit money
account.withdraw(100)         # Withdraw money
account.withdraw(1000)        # Attempt to withdraw more than balance (insufficient funds)
account.deposit(-50)          # Attempt invalid deposit
account.withdraw(-30)         # Attempt invalid withdrawal
account.show_transactions()   # Show all transactions


'''What is Abstraction in Python? 🎭
Hello, young coder! 😊 Imagine you are playing a video game 🎮. You press a button, and your character jumps! But do you know how the game makes the character jump inside the computer? No, right?

You only see the action (jumping), but you don’t see the complex code behind it.

That’s called Abstraction! 🏆'''

# Definition of Abstraction
'''Abstraction means hiding the unnecessary details and showing only the important things. In Python, abstraction helps us use things without worrying about how they work inside.'''

# Real-Life Example: Car 🚗
'''When you drive a car, you only use the steering wheel, brake, and accelerator.
But do you know how the engine, gears, and fuel system work inside? No!
You don’t need to know those details to drive a car. That’s abstraction!'''

# How Abstraction Works in Python? 🐍
'''In Python, we use abstract classes to hide details and show only important things.
To create an abstract class, we use the ABC (Abstract Base Class) module.
'''
# Example: Animal Sounds 🐶🐱

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # No details here, just an idea!

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")  # Only showing the important part

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")  # Only showing the important part

# Creating objects
dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Woof! Woof!
cat.make_sound()  # Output: Meow! Meow!

'''Breaking it Down for You! 🎯
✅ Animal(ABC) → Abstract class (a blueprint).
✅ @abstractmethod → Means this method must be defined in subclasses.
✅ Dog and Cat → Actual classes that show only the important things.
✅ Objects (dog, cat) → We can use them without worrying about how they work inside!'''

'''Why Use Abstraction?
🔹 Hides complexity – You don’t need to know how things work inside.
🔹 Focus on what’s important – Only see the actions you need.
🔹 Makes coding easier – Helps keep your code clean and organized.'''

'''Another Fun Example: TV Remote 📺
When you press a button on a remote, the TV changes channels or increases volume.
But do you know how the TV processes signals inside? No!
That’s abstraction—hiding details and showing only what you need!'''

# Final Thought! 🤔
'''Abstraction helps us use things easily without worrying about the details inside!
Just like you can drive a car 🚗 without knowing how the engine works!'''

# Industry-Standard Example of Abstraction in Python 🏢🚀
# Abstraction is widely used in the software industry to hide complex logic and provide a simple interface for users. A great real-world industry example is a Banking System (ATM Machine).

# 🏦 Example: ATM Machine (Bank System)
# Imagine you go to an ATM to withdraw money.
# Do you need to know how the bank’s servers process your request? No!
# You only interact with the ATM screen, enter your PIN, and get your cash.

# ➡️ The complex logic inside the ATM is hidden from you! That’s abstraction!

# Industry-Standard Python Example: Banking System
# Here’s how abstraction is used in a banking system in Python:


from abc import ABC, abstractmethod

# Abstract Class (Hides Complex Logic)
class Bank(ABC):
    def __init__(self, balance):
        self.balance = balance  # Store balance

    @abstractmethod
    def deposit(self, amount):
        pass  # Only an idea, no implementation

    @abstractmethod
    def withdraw(self, amount):
        pass  # Only an idea, no implementation

    def show_balance(self):  # Concrete method (not abstract)
        print(f"Your balance is: ${self.balance}")

# Concrete Class (Actual Implementation)
class MyBank(Bank):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds!")

# Using the Bank System
account = MyBank(500)  # Create a bank account with $500 balance

account.show_balance()  # Output: Your balance is: $500
account.deposit(200)    # Output: Deposited $200. New Balance: $700
account.withdraw(100)   # Output: Withdrew $100. New Balance: $600
account.withdraw(1000)  # Output: Insufficient funds!

# How This Uses Abstraction? 🎯
# ✅ Bank(ABC) → Abstract class (hides the deposit/withdraw logic).
# ✅ @abstractmethod deposit() & withdraw() → These must be implemented in real banks.
# ✅ show_balance() → A method that is already implemented (no need for change).
# ✅ MyBank(Bank) → A real bank that follows the abstract blueprint.
# ✅ account.deposit(200) → User just calls deposit, without knowing the backend logic!

# 🏢 Industry Use Cases of Abstraction
# 🔹 Web Development → Web frameworks (like Django, Flask) abstract database handling.
# 🔹 Machine Learning → Libraries (like TensorFlow, Scikit-learn) hide complex algorithms.
# 🔹 Database Systems → SQL queries abstract internal database operations.
# 🔹 Operating Systems → User interacts with a GUI, but the kernel runs in the background.

# 🎯 Summary: Why Use Abstraction in the Industry?
# ✔️ Simplifies Complex Systems – Users don’t need to understand internal details.
# ✔️ Increases Security – Sensitive logic (like banking transactions) stays hidden.
# ✔️ Encourages Reusability – One abstract class can be used by multiple systems.
# ✔️ Improves Code Maintainability – Changes inside the system don’t affect users.

# 💡 Think of abstraction like driving a car 🚗—you only use the steering, brake, and accelerator, but you don’t see the complex engine working inside!



# 🔍 Understanding the Missing Parts
# In the original code:

# 1. deposit(self, amount) and withdraw(self, amount) were only ideas (pass) in the Bank class.
# 2. They were implemented inside the MyBank class.
# 3. But we can enhance them by adding error handling, transaction history, and more!

# ✅ Completed and Enhanced Code

from abc import ABC, abstractmethod

# Abstract Class (Hides Complex Logic)
class Bank(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Store account number
        self.balance = balance  # Store balance
        self.transactions = []  # Store transaction history

    @abstractmethod
    def deposit(self, amount):
        """Abstract method for deposit - Must be implemented in subclasses"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method for withdrawal - Must be implemented in subclasses"""
        pass

    def show_balance(self):
        """Show the current account balance"""
        print(f"Account {self.account_number} - Your balance is: ${self.balance}")

    def show_transactions(self):
        """Show the transaction history"""
        print(f"\nTransaction History for Account {self.account_number}:")
        if not self.transactions:
            print("No transactions yet!")
        else:
            for transaction in self.transactions:
                print(transaction)

# Concrete Class (Actual Implementation)
class MyBank(Bank):
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            print("Deposit amount must be greater than zero!")
        else:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}. New Balance: ${self.balance}")
            print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
        elif self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}. New Balance: ${self.balance}")
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            self.transactions.append(f"Failed withdrawal of ${amount} due to insufficient funds.")
            print("Insufficient funds!")

# Using the Bank System
account = MyBank(account_number=123456, balance=500)  # Create a bank account with $500 balance

account.show_balance()        # Show current balance
account.deposit(200)          # Deposit money
account.withdraw(100)         # Withdraw money
account.withdraw(1000)        # Attempt to withdraw more than balance (insufficient funds)
account.deposit(-50)          # Attempt invalid deposit
account.withdraw(-30)         # Attempt invalid withdrawal
account.show_transactions()   # Show all transactions

'''🔍 Breakdown of Changes and Enhancements

1. Added account_number → Now each account has a unique number.
2. Added transactions list → To store transaction history (deposit/withdrawal).
3. Improved deposit() method:
- Prevents negative deposits.
- Saves transaction history.
4. Improved withdraw() method:
- Prevents negative withdrawals.
- Checks for sufficient funds.
- Saves failed withdrawal attempts.
5. Added show_transactions() method → Displays all past transactions.

📌 How This Demonstrates Abstraction?
1. Bank(ABC) (Abstract Class)
- Defines what a bank should have (deposit, withdraw, show_balance), but not how it works.
2. MyBank(Bank) (Concrete Class)
- Implements the actual logic of deposits, withdrawals, and transactions.

3. Users Only See the Interface (Not Internal Logic)
- A user calls deposit(200) but doesn’t need to know how the bank updates the balance.
- A user calls withdraw(1000) and just gets an "Insufficient funds!" message.

# 🛠 Example Output
Account 123456 - Your balance is: $500
Deposited $200. New Balance: $700
Withdrew $100. New Balance: $600
Insufficient funds!
Deposit amount must be greater than zero!
Withdrawal amount must be greater than zero!
Transaction History for Account 123456:
Deposited $200. New Balance: $700
Withdrew $100. New Balance: $600
Failed withdrawal of $1000 due to insufficient funds.

💡 Key Takeaways
✅ Abstraction hides complexity (Users don’t see how the deposit/withdraw methods work inside).
✅ Abstract methods force subclasses to implement logic (deposit() and withdraw()).
✅ Concrete class (MyBank) provides actual working logic for a bank system.
✅ Error handling and transaction history make it realistic like a real banking app.
'''