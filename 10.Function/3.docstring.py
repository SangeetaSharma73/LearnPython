#docstring
def funName():
    # docstring tells about function
    """
    this is the function Name 
    """
    print('hi')
funName()

#parameters
'''these are place holders in the function
 when defining them we call them as parameters
 when passing the actual value we call them as Arguments
 '''

def greet(name):  
# name is the parameter in the greet function
    print('hi,How are you',name)

greet('Siya') #Siya is argument

def add(a,b):
    c=a+b
    print(c)
# add(2)TypeError: add() missing 1 required positional argument: 'b'
add(2,3)


#return 
'''A function call ends when return statement is executed 
   It returns the expression back to the function
   the code after return statement are not executed 
   if there is no return value then function returns  None'''

#return vs print
def add(a,b):
    c=a+b
    print(c)
add(3,4)

a=add(3,4)
print(a)
print(type(a))
print(type(print(4)))


def sub(a,b):
    c=a-b
    return c
b=sub(3,4)
print(b,type(b))

#if no return obj then it returns Nonetype
def func():
    return 
func()
c=func()
print(c,type(c))

#code after return statement doesn't get executed
def funct():
    print('before return')
    return 'mname'
    print('after return')
funct()
a=funct()
print(a)

#returning multiple values 
def intro(name,age,hobby):
    return name,age,hobby
# a,b=2,3
# print(a,b)
c,d,e=intro('sona',25,'dancing')
print(c,d,e)

c=intro('siya',23,'song')
print(c,type(c))

#scope of a variable
