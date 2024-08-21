'''Understanding Polymorphism in Python
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
