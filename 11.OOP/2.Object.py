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
