'''Object oriented programming
   The principles of OOPs are based on 4 pillars apart from class and objects
   A class has attributes and behavior '''

'''1. Class:  A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.
It allows you to structure your program into reusable pieces of code.'''

class Dog:
    # Class attributes (properties)
    species = 'Canine'
    
    # Constructor to initialize object attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    # Class method (behavior)
    def bark(self):
        return f"{self.name} is barking!"

''' What is a Class in Python? 🐍
 A class in Python is like a blueprint for creating things (objects). Imagine you want to build a toy car 🚗. You need a design or blueprint that tells you how to make the car. That blueprint is called a class, and each toy car made from it is called an object.'''

# Definition of Class
'''A class is a way to create and organize data and functions in Python. It allows you to make multiple objects that share the same properties and actions.'''

# 💡 Think of a class as a cookie cutter and objects as the cookies made from it! 🍪

# How to Create a Class in Python

class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Property (Attribute)
        self.color = color  # Property (Attribute)

    def drive(self):
        print(f"The {self.color} {self.brand} car is driving!")

# Creating objects (Instances) of the class
car1 = Car("Toyota", "red")
car2 = Car("BMW", "blue")

# Using the class methods
car1.drive()  # Output: The red Toyota car is driving!
car2.drive()  # Output: The blue BMW car is driving!

# Breaking it Down for You!
# ✅ class Car: → This defines a Car class, like a blueprint.
# ✅ __init__(self, brand, color): → This is a special function to initialize the car’s properties.
# ✅ self.brand = brand → Saves the car’s brand (Toyota, BMW, etc.).
# ✅ self.color = color → Saves the car’s color (red, blue, etc.).
# ✅ drive(self): → A function that makes the car drive.

# Real-Life Use Case 🚴
# Let’s say we want to create a Bicycle class. We can define its color, brand, and speed.



class Bicycle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def ride(self):
        print(f"Riding the {self.brand} bicycle at {self.speed} km/h!")

# Creating objects
bike1 = Bicycle("Hero", 20)
bike2 = Bicycle("Giant", 25)

bike1.ride()  # Output: Riding the Hero bicycle at 20 km/h!
bike2.ride()  # Output: Riding the Giant bicycle at 25 km/h!
# Why Use Classes?
# 🔹 Organizes Code – Helps keep code clean and structured.
# 🔹 Reusability – You can create multiple objects from one class.
# 🔹 Encapsulation – Keeps related data and actions together.



''' Constructor in Python Class
 A constructor is a special method used to initialize objects when they are created. In Python, the constructor method is named __init__(). When you create an instance of a class, the constructor is automatically called to initialize the object's attributes with specific values.

Key Points:
The constructor is called automatically when an object is created from a class.
It is used to assign initial values to the object's attributes.'''
class Dog:
   def __init__(self, name, age):  # Constructor method
      self.name = name  # Attribute assignment
      self.age = age  # self refers to the current object
   
   def bark(self):
      print(f"{self.name} is barking!")  # Accessing the instance's name using self

# Creating an object of the class Dog
my_dog = Dog("Buddy", 5)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5

# In this example, the __init__() method (constructor) initializes the name and age attributes of the object my_dog with the values "Buddy" and 5, respectively.

'''self in Constructor
The self parameter in the constructor (and in any method within a class) refers to the current instance of the class. It is used to access the object's attributes and methods from within the class.

self allows you to refer to instance attributes and methods within the class.
While defining a class method, self is the first parameter, and when the method is called, it refers to the instance calling it.'''


'''Why self?
When you create an object, the class needs a way to refer to that specific object. 
self acts as that reference,enabling the constructor (and other methods) 
to manipulate the attributes of the particular instance.'''

