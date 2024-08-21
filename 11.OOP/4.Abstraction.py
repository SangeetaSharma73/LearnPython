'''Abstraction in Python
Abstraction is one of the key principles of Object-Oriented Programming (OOP). It involves hiding the internal details and showing only the essential features of an object. By using abstraction,
we simplify complex systems by breaking them down into more manageable parts and hiding unnecessary details.

In Python, abstraction is achieved using abstract classes and interfaces. 
Python uses the abc module to implement abstract classes and methods.

Key Features of Abstraction:
Simplification: It hides the complex implementation details and shows only the necessary information.
Modularity: By dividing the program into independent modules, it makes maintenance and updating easier.
Reusability: Abstract classes can be extended to other classes, enhancing code reusability.
Maintainability: Since complex logic is hidden, the system becomes easier to maintain.
Types of Abstraction
There are two types of abstraction in programming:

Data Abstraction: Focuses on what data an object should have and hides how this data is maintained or manipulated. For instance, in a bank application, the user is aware of the functionalities like deposit, withdraw, etc., but doesn't know the internal working of these operations.

Control Abstraction: Focuses on hiding how an object does something and instead describes what should be done. It allows users to interact with objects or systems by calling methods, without needing to understand the detailed logic behind them.

Abstract Classes in Python
An abstract class is a class that cannot be instantiated directly. It contains one or more abstract methods, which are methods declared but contain no implementation. These classes are designed to be inherited, and the derived classes must implement the abstract methods.

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