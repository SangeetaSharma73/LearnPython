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