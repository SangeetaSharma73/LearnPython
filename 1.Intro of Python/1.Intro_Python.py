#Intro Python-
'''Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.
'''

'''What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.
'''

'''
To check if you have python installed on a Windows PC, search in the start bar for Python or run the following on the Command Line (cmd.exe):
python --version
'''

'''
To check the Python version of the editor, you can find it by importing the sys module:
import sys
print(sys.version)
'''

'''
Whenever you are done in the python command line, you can simply type the following to quit the python command line interface:
exit()
'''
#Want to show something as output : use print function
print('Hello World')


#Python Indentation-
'''Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.
'''
# print('yes')
# print()
# print('this')
# Ex-
if 5 > 2:
  print("Five is greater than two!")

# Python will give you an error if you skip the indentation:
# Syntax Error:

'''if 5 > 2:
print("Five is greater than two!")'''

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

if 5>2:
  print('five is greater')
if 5>2:
      print('five is greater')


# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
'''
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
'''


#variable-Variables are placeholders for storing data
#variable name=(Assignment operator) value to be assigned 
# Creating Variables
'''Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.'''
x=10
print(x)

# Casting
'''If you want to specify the data type of a variable, this can be done with casting.'''
x = str(3)    # x will be '3'
y = int("3")    # y will be 3
z = float(3)  # z will be 3.0
p= float("3")
print(p)

#Naming a variable
#1.Variable should start with a letter or the underscore charactor
#2.can't start with no.
#3. variable name are case sensitive-age,Age
#4.don't use keywords as identifiers
#5.alpha numeric can name

# Legal variable names:
'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''

# Illegal variable names:
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''
#Note: Remember that variable names are case-sensitive

#3a= 4  invalid syntax
# help("keywords")
#for=24 invalid syntax


#id function
x=2
print("this is the id",id(x))


#stack /Heap memory

# In Python, memory management involves two key types of memory storage: stack memory and heap memory. These two areas handle different types of data and are used in various ways during a program's execution.


# 1. Stack Memory:
'''The stack memory is where function calls and local variables are stored.
This memory is used for the static allocation of memory and is automatically managed by Python.
'''

# Characteristics of Stack Memory:
'''
Automatic Allocation/Deallocation: Memory is allocated and deallocated automatically when functions are called and return, respectively.
Fast Access: Stack memory is faster than heap memory because of its structure (LIFO - Last In First Out).
Limited Size: Stack memory has a smaller, fixed size, and can cause a stack overflow if too much memory is used (e.g., in deep recursion).
'''

'''
What Gets Stored on the Stack:
Function call details (activation records).
Local variables inside functions.
Function parameters.
'''

# Example of Stack Memory Usage:
def func_a():
  x = 10   # x is stored in the stack
  func_b() # When func_b is called, func_a's variables remain on the stack

def func_b():
  y = 20   # y is stored in the stack

func_a()     # Calls both functions

# In this example, when func_a() is called, x is stored on the stack.
# When func_b() is called,its own variable y is also placed on the stack. 
# Once the function finishes executing, the stack memory for that function is cleared.


# 2. Heap Memory:
'''
The heap memory is used for dynamic memory allocation. Unlike the stack, the heap is used for objects whose size may not be known at compile time and can grow as needed.
'''

# Characteristics of Heap Memory:
'''
Dynamic Allocation: Memory is allocated dynamically as required.
Global Access: Objects stored in the heap are globally accessible. Once allocated, they can be referenced from anywhere in the program.
Slower Access: Accessing heap memory is generally slower than accessing stack memory.
Garbage Collection: Python’s Garbage Collector is responsible for freeing up memory from objects that are no longer in use (unreferenced).
'''

'''
What Gets Stored on the Heap:
Objects such as lists, dictionaries, class instances, etc.
Objects that need to be shared or persist beyond the scope of a single function call.

'''


# Example of Heap Memory Usage:
class Car:
    def __init__(self, brand):
        self.brand = brand  # Stored in heap

car_a = Car("Toyota")
car_b = Car("Honda")



# Multi Words Variable Names
'''
Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:
'''

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variables

'''Python allows you to assign values to multiple variables in one line'''
# x, y, z,t = "Orange", "Banana", "Cherry"
x, y, z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# print(t)#(value error: not enough values to unpack )


#One Value to Multiple Variables
'''And you can assign the same value to multiple variables in one line:'''
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
'''If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.'''

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
'''Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.'''

x = "awesome"

def MyFun():
  print("Python is " + x)

MyFun()  #python is awesome

'''If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.'''

x = "awesome"

def MyFun():
  x = "fantastic"
  print("Python is " + x)  #python is fantastic

MyFun()

print("Python is " + x)  #python is awesome


# The global Keyword
'''Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.'''

def MyFun():
  global x
  x = "fantastic"

MyFun()

print("Python is " + x) #python is fantastic

# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def MyFun():
  global x
  x = "fantastic"

MyFun()

print("Python is " + x) #python is fantastic