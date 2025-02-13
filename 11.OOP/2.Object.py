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
print('d1',d1.y,d1.x)
d2=Demo()
print('d2',Demo.x)

print(d1.__dict__)#here static variables will not be visible
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