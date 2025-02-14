'''Understanding Polymorphism in Python:
Polymorphism is one of the key concepts in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It also allows a method to perform differently based on the object that is calling it, even though they share the same name.

In Python, polymorphism is achieved through:

Method Overriding (when a subclass provides a specific implementation of a method in the parent class).
Method Overloading (which Python achieves in a loose form through default arguments).
'''

class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def sound(self):
        return "Barks"

class Cat(Animal):
    def sound(self):
        return "Meows"

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())


'''Polymorphism is a core concept in object-oriented programming that allows different types (classes) to be treated in the same way by using a common interface. 
The word polymorphism is derived from Greek, meaning "many shapes" or "many forms". 
In Python, polymorphism allows objects of different classes to respond to the same method in different ways.'''

'''Types of Polymorphism
There are two main types of polymorphism in Python:

Compile-Time Polymorphism (Method Overloading): Achieving polymorphism during compile time (unsupported in Python).
Run-Time Polymorphism (Method Overriding): Achieving polymorphism at runtime using method overriding in subclasses.'''


'''1. Compile-Time Polymorphism (Method Overloading)
In method overloading, multiple methods can share the same name but have different signatures (number or type of parameters).
Python doesn’t support method overloading natively.
However, this can be achieved using default arguments or variable-length arguments (*args or **kwargs).'''

class MathOperations:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

math_obj = MathOperations()
print(math_obj.add(2, 3))         # Output: 5
print(math_obj.add(1, 2, 3))      # Output: 6
print(math_obj.add(10))           # Output: 10
# Here, the same add() method behaves differently depending on the number of arguments passed.


'''2. Run-Time Polymorphism (Method Overriding)
Method overriding is a form of run-time polymorphism where a child class provides a specific implementation of a method that is already defined in its parent class.
The method in the child class overrides the one in the parent class, allowing for different behaviors depending on the object type.'''

# Example of Method Overriding in Python:
class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def sound(self):  # Method overriding
        print("The dog barks.")

class Cat(Animal):
    def sound(self):  # Method overriding
        print("The cat meows.")

# Creating instances
animal = Animal()
dog = Dog()
cat = Cat()

# Polymorphism: The same method 'sound' behaves differently for different objects
animal.sound()  # Output: This animal makes a sound.
dog.sound()     # Output: The dog barks.
cat.sound()     # Output: The cat meows.





'''🎭 What is Polymorphism?
💡 Polymorphism means "one thing, many forms."

Imagine you have a superhero 🦸‍♂️ who can fly, fight, and save people.
Depending on the situation, he can use different powers—that’s polymorphism!

In Python, polymorphism lets us use the same function or method in different ways.
'''
'''
🏀 Real-Life Example of Polymorphism
Think about a boy kicking different things:

He kicks a football → It rolls. ⚽
He kicks a stone → It doesn’t move much. 🪨
He kicks a balloon → It flies up. 🎈
👉 The action is the same ("kick"), but the result is different! That’s polymorphism! 🚀'''

# 📌 Polymorphism in Python (Simple Code Example)

class Dog:
    def speak(self):
        return "Woof! Woof!"  # Dogs bark

class Cat:
    def speak(self):
        return "Meow! Meow!"  # Cats meow

class Cow:
    def speak(self):
        return "Moo! Moo!"  # Cows moo

# Using polymorphism
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())  

# 🔍 Output:

# Woof! Woof!
# Meow! Meow!
# Moo! Moo!
# ✅ Same method name (speak), but different behaviors!
# ✅ Different animals make different sounds using the same method!

# 🎮 Example: Polymorphism with Different Shapes
# Imagine we have a circle, a square, and a triangle.
# Each has a different way to calculate area, but we use the same method name!

import math

class Shape:
    def area(self):
        pass  # Abstract method (to be implemented by subclasses)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius  # Area of a circle

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  # Area of a square

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  # Area of a triangle

# Using polymorphism
shapes = [Circle(7), Square(4), Triangle(6, 3)]

for shape in shapes:
    print(f"Area: {shape.area()}")

# 🔍 Output:
# Area: 153.93804002589985
# Area: 16
# Area: 9.0

# ✅ Same method name (area), but different shapes calculate it differently!
# ✅ This makes code reusable and easy to understand!

# 🏆 Types of Polymorphism in Python
# 1️⃣ Method Overriding (Different Behavior in Child Classes)
# When a child class changes the behavior of a method from a parent class.


class Bird:
    def fly(self):
        print("Most birds can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly!")

# Using polymorphism
sparrow = Bird()
penguin = Penguin()

sparrow.fly()  # Output: Most birds can fly.
penguin.fly()  # Output: Penguins cannot fly!

# ✅ Same method name (fly), but different behavior for different birds!

# 2️⃣ Method Overloading (Same Method, Different Inputs)
# Python doesn’t support method overloading directly, but we can do it using default arguments.

class Math:
    def add(self, a, b, c=0):
        return a + b + c  # If 'c' is not given, it defaults to 0

math = Math()
print(math.add(5, 10))       # Output: 15
print(math.add(5, 10, 20))   # Output: 35
# ✅ Same method (add), but it works with 2 or 3 numbers!

# 🚀 Industry Example: Polymorphism in a Payment System
# Imagine an online shopping app like Amazon.

# Users can pay using Credit Card, PayPal, or Bitcoin.
# The payment method is different, but we use the same function name!

class Payment:
    def pay(self):
        pass  # Abstract method (will be implemented in subclasses)

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card.")

class PayPal(Payment):
    def pay(self):
        print("Paid using PayPal.")

class Bitcoin(Payment):
    def pay(self):
        print("Paid using Bitcoin.")

# Using polymorphism
payments = [CreditCard(), PayPal(), Bitcoin()]

for payment in payments:
    payment.pay()
    
# 🔍 Output:
# Paid using Credit Card.
# Paid using PayPal.
# Paid using Bitcoin.
# ✅ Same method (pay), but different payment methods work differently!

# 🎯 Why is Polymorphism Important?
# ✅ Reusability → We can write one function and use it for different things.
# ✅ Simplicity → Code is cleaner and easier to understand.
# ✅ Flexibility → Allows different objects to behave in their own way.
# ✅ Used in Real-World Applications → Web apps, games, and banking systems.

# 🎮 Fun Challenge for You!
# Try creating a game where different characters (Warrior, Archer, Wizard) have a method attack() but attack differently! 🎯

# Let me know if you need help! 🚀😃