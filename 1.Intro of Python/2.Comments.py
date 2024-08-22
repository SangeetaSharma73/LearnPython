# Python Comments
'''
Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.
'''

# Creating a Comment
'''
Comments starts with a #, and Python will ignore them:
'''
x=23
# print(id(x))

#comments
#this is a single line comment

# Multiline Comments
'''Python does not really have a syntax for multiline comments.
To add a multiline comment you could insert a # for each line:
'''
#This is a comment
#written in
#more than just one line
print("Hello, World!")


#Or, not quite as intended, you can use a multiline string.
# Since Python will ignore string literals that are not assigned to a variable,
# you can add a multiline string (triple quotes) in your code, and place your comment inside it:

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")



# Comments can be placed at the end of a line, and Python will ignore the rest of the line:
print('hello world') #this is a comment



#data types
#int
number=23
print(number)
print(type(number))

#float
n=2.4
print(n)
print(type(n))

#Booleans
b=True
print(type(b))

#strings
s='Rahul 123 @ +'
print(type(s))

s="Rahul 123 @ +"
print(type(s))

#multiline string
a='''
this is the 
multiline string
'''


n=None
print(n)
print(type(n))