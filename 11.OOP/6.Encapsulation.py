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