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
print('d1',d1.y,d1.x)
d2=Demo()
print('d2',Demo.x)

print(d1.__dict__)#here static variables will not be visible
# print(Demo.__dict__)


#various places to declare the static variables

'''
1.In general we can declare static variables within the class directly but from out of any method
'''

class Demo:
    a=10
    def __init__(self):
        Demo.b=20
        
    def fun1(self):
        Demo.c=30
        
    @classmethod
    def fun2(cls):
        Demo.d1=40
        cls.d2=50
        
    @staticmethod
    def fun3():
        Demo.e=60
        

print(Demo.__dict__)

Demo.fun1()
print(Demo.__dict__)

Demo.fun2()
print(Demo.__dict__)

Demo.fun3()
print(Demo.__dict__)

Demo.f=70
print(Demo.__dict__)
