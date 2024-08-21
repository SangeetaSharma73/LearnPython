'''Object oriented programming
   The principles of OOPs are based on 4 pillars apart from class and objects
   A class has attributes and behaviour '''

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