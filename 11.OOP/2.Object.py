'''2. Object
An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.
You can think of an object as a real-world entity that is created from the class (template).'''

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




# Creating an object from the Dog class
my_dog = Dog("Buddy", 5)

# Accessing object attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Buddy is barking!




class Demo:
    x=10
    def __init__(self):
        self.y=20

d1=Demo()
d1.y=200
Demo.x=100
d1.x=103
Demo.x=200
print('d1',d1.y,d1.x) #d1 200 103 
d2=Demo()
print('d2',Demo.x) #d2 200

print('d1 dict',d1.__dict__)#d1 dict {'y': 200, 'x': 103}
print(Demo.__dict__)


#various places to declare the static variables

'''
1.In general we can declare static variables within the class directly but from out of any method
'''

class Demo:
    a=10 # Static Variable (belongs to the class)
    def __init__(self):
        Demo.b=20 # Creating a new static variable inside the constructor
        
    def fun1(self):
        Demo.c = 30  # Creating another static variable inside a normal method
        
    @classmethod
    def fun2(cls):
        Demo.d1 = 40  # Creating a static variable
        cls.d2 = 50  # Another way to create a static variable
        
    @staticmethod
    def fun3():
        Demo.e=60 # Creating a static variable
    # A static method can create static variables but doesn’t need an object.
        
Demo.fun2()  # No need to create an object, we call it using the class
print(Demo.d1)  # Output: 40
print(Demo.d2)  # Output: 50

Demo.fun3()  # Calling the static method
print(Demo.e)  # Output: 60


d1 = Demo()  # Creating an object
d1.fun1()  # Now it works!
print(Demo.c)  # Output: 30

# Demo.fun1()
# print(Demo.c)
# print(Demo.__dict__)

# Demo.fun2()
# print(Demo.__dict__)

# Demo.fun3()
# print(Demo.__dict__)

# Demo.f=70
# print(Demo.__dict__)
# print(Demo.__dict__)


'''What is an Object in Python? 🤖
An object is a real-world thing created from a class. If a class is like a blueprint, then an object is the actual thing built from that blueprint.

For example, if a class is a "Car Blueprint", then objects can be "a red Toyota" or "a blue BMW"—both are actual cars made from the blueprint! 🚗
'''
# Example of an Object
# Let’s create a Car class and make objects from it.


class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Object Property (brand)
        self.color = color  # Object Property (color)

    def drive(self):
        print(f"The {self.color} {self.brand} car is driving!")

# Creating objects (cars)
car1 = Car("Toyota", "Red")  # car1 is an object
car2 = Car("BMW", "Blue")    # car2 is another object

# Using the objects
car1.drive()  # Output: The Red Toyota car is driving!
car2.drive()  # Output: The Blue BMW car is driving!
'''Breaking it Down for You! 🎯
✅ Car is a class (the blueprint).
✅ car1 and car2 are objects (real cars created from the class).
✅ Each object has its own brand and color.

💡 Think of a class as a mold for making action figures, and objects are the actual figures! 🎭
'''
# Another Fun Example: Animals! 🦁🐶🐱
# Let’s make an Animal class and create different animal objects.


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"The {self.name} says {self.sound}!")

# Creating objects (animals)
dog = Animal("Dog", "Woof")  
cat = Animal("Cat", "Meow")  

dog.make_sound()  # Output: The Dog says Woof!
cat.make_sound()  # Output: The Cat says Meow!
'''Why Use Objects?
🔹 Objects store real-world data (like a car’s color or an animal’s sound).
🔹 Each object is unique (e.g., different colors, brands, or sounds).
🔹 Objects can perform actions (like driving a car or making an animal sound).

'''