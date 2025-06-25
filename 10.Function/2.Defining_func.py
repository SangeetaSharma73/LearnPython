# Defining a simple function in Python
# A function is defined using the 'def' keyword, followed by the function name and parentheses.
def greet():
    # This is the body of the function
    print('Hey, have a good day!')

# Printing the function object (shows its memory address, not the result of the function)
print('Printing the function object:', greet)

# Calling the function (executes the code inside the function)
greet()

# Example: Function with parameters and return value
def add(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

# Calling the add function and printing the result
result = add(3, 5)
print('The sum of 3 and 5 is:', result)