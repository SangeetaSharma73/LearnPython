'''Inheritance is a key concept in Object-Oriented Programming (OOP) that allows a class to inherit attributes and methods from another class. 
This promotes code reuse and the creation of a hierarchical relationship between classes.'''

'''Key Concepts:
Parent Class (Base Class): The class whose attributes and methods are inherited.
Child Class (Derived Class): The class that inherits from the parent class.
'''

# Parent Class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return f"{self.name} makes a sound."

# Child Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # Inheriting from Animal class
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

# Usage example
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy barks.

# Parent Class (Super Class)
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child Class (Sub Class)
class Dog(Animal):
    def bark(self):
        print("Dog barks 🐶")

# Creating object of Dog class
d = Dog()
d.sound()  # Inherited method from Animal class
d.bark()   # Own method of Dog class


'''Inheritance with a Real-World Problem
Problem: Creating a School Management System
Scenario: You are building a simple school management system where you need to represent different types of people associated with the school: students, teachers, and staff members. You want to reuse common attributes like name, age, and gender across all of them but also want to define specific attributes for each type.

Solution: Using Inheritance
Step 1: Define the Parent Class (Person)

This class will hold common attributes like name, age, and gender.
Step 2: Define Child Classes (Student, Teacher, Staff)

Each child class will inherit from Person and will have additional attributes specific to their roles.
Step 3: Implement Methods to Demonstrate Inheritance

Show how inherited methods and attributes work in these child classes.'''

# Parent Class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# Child Class for Student
class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        super().__init__(name, age, gender)  # Inheriting from Person class
        self.student_id = student_id
        self.major = major

    def get_details(self):
        base_details = super().get_details()  # Reuse get_details from Person
        return f"{base_details}, Student ID: {self.student_id}, Major: {self.major}"

# Child Class for Teacher
class Teacher(Person):
    def __init__(self, name, age, gender, employee_id, subject):
        super().__init__(name, age, gender)  # Inheriting from Person class
        self.employee_id = employee_id
        self.subject = subject
      
    def get_details(self):
        base_details = super().get_details()  # Reuse get_details from Person
        return f"{base_details}, Employee ID: {self.employee_id}, Subject: {self.subject}"

# Child Class for Staff
class Staff(Person):
    def __init__(self, name, age, gender, role):
        super().__init__(name, age, gender)  # Inheriting from Person class
        self.role = role

    def get_details(self):
        base_details = super().get_details()  # Reuse get_details from Person
        return f"{base_details}, Role: {self.role}"

# Usage example
student = Student("Alice", 20, "Female", "S12345", "Computer Science")
teacher = Teacher("Mr. Smith", 40, "Male", "T9876", "Mathematics")
staff = Staff("John Doe", 35, "Male", "Administrator")

# Print details for each
print(student.get_details())
# Output: Name: Alice, Age: 20, Gender: Female, Student ID: S12345, Major: Computer Science

print(teacher.get_details())
# Output: Name: Mr. Smith, Age: 40, Gender: Male, Employee ID: T9876, Subject: Mathematics

print(staff.get_details())
# Output: Name: John Doe, Age: 35, Gender: Male, Role: Administrator


#optional
'''How Inheritance Solves the Problem
Code Reuse: By creating a Person class that contains shared attributes (name, age, gender), you avoid repeating the same code in each child class (Student, Teacher, Staff).

Maintainability: If you need to add or modify common attributes or methods (e.g., changing how get_details works), you can do so in one place (the Person class), and all derived classes will inherit these changes.

Extensibility: Adding new types of people (e.g., Principal) is easy. You can create a new class that inherits from Person and add any specific attributes or methods.

Customization: While all child classes inherit the get_details method, they can customize it by overriding the method to add specific details relevant to their type (e.g., Student ID, Subject).'''


# 2️⃣ Multiple Inheritance
# 👨‍👩‍👦 One Child, Two (or more) Parents
# A child class inherits from multiple parent classes.

# Parent Class 1
class Father:
    def work(self):
        print("Father goes to work 👨‍💼")

# Parent Class 2
class Mother:
    def cook(self):
        print("Mother cooks food 🍲")

# Child Class (Inherits from both Father and Mother)
class Child(Father, Mother):
    def play(self):
        print("Child plays games 🎮")

# Creating object of Child class
c = Child()
c.work()  # Inherited from Father
c.cook()  # Inherited from Mother
c.play()  # Own method of Child

# Father goes to work 👨‍💼
# Mother cooks food 🍲
# Child plays games 🎮

# 📌 Why is it useful?

# The child inherits properties from both parents.
# Example: A baby can have dad’s eyes and mom’s smile! 😊

# 3️⃣ Multilevel Inheritance
# 👴➡️👨➡️👦 Grandfather → Father → Son
# One class inherits from another class, which then inherits from another class.

# Grandparent Class
class Grandfather:
    def wisdom(self):
        print("Grandfather is wise 👴")

# Parent Class (inherits from Grandfather)
class Father(Grandfather):
    def strength(self):
        print("Father is strong 💪")

# Child Class (inherits from Father)
class Son(Father):
    def fun(self):
        print("Son loves to play 🎮")

# Creating object of Son class
s = Son()
s.wisdom()  # Inherited from Grandfather
s.strength()  # Inherited from Father
s.fun()  # Own method of Son

# Grandfather is wise 👴
# Father is strong 💪
# Son loves to play 🎮

# 📌 Why is it useful?

# The child inherits features generation by generation, just like a family tree! 🌳

# 4️⃣ Hierarchical Inheritance
# 👨 One Parent, Many Children
# Multiple child classes inherit from a single parent class.


# Parent Class
class Vehicle:
    def move(self):
        print("Vehicles help us travel 🚗🚀🚲")

# Child Class 1 (inherits from Vehicle)
class Car(Vehicle):
    def wheels(self):
        print("A car has 4 wheels 🚗")

# Child Class 2 (inherits from Vehicle)
class Bike(Vehicle):
    def wheels(self):
        print("A bike has 2 wheels 🚲")

# Creating objects
c = Car()
b = Bike()

c.move()  # Inherited from Vehicle
c.wheels()

b.move()  # Inherited from Vehicle
b.wheels()

# Vehicles help us travel 🚗🚀🚲
# A car has 4 wheels 🚗
# Vehicles help us travel 🚗🚀🚲
# A bike has 2 wheels 🚲

# 📌 Why is it useful?

# We don’t repeat the move() method in Car and Bike. They inherit it from Vehicle.

# 5️⃣ Hybrid Inheritance
# 🌀 A Mix of Different Inheritance Types
# A combination of multiple types of inheritance in one program.

# Parent Class
class A:
    def method_A(self):
        print("Method from A")

# Child Class (Single Inheritance from A)
class B(A):
    def method_B(self):
        print("Method from B")

# Another Parent Class
class C:
    def method_C(self):
        print("Method from C")

# Child Class (Multiple Inheritance from B and C)
class D(B, C):
    def method_D(self):
        print("Method from D")

# Creating object of D
d = D()
d.method_A()  # Inherited from A
d.method_B()  # Inherited from B
d.method_C()  # Inherited from C
d.method_D()  # Own method


# Method from A
# Method from B
# Method from C
# Method from D

# 📌 Why is it useful?

# We can combine different types of inheritance to make our code more powerful! 💪


