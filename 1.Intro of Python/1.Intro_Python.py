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
x=10
print(x)
#Naming a variable
#1.Variable should start with a letter or the underscore charactor
#2.can't start with no.
#3. variable name are case sensitive-age,Age
#4.don't use keywords as identifiers
#5.alpha numeric can name

#3a= 4  invalid syntax

# help("keywords")

#for=24 invalid syntax

#stack /Heap memory

#id function

x=2
id(x)