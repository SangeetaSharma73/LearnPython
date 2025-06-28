# Defining a simple greeting function
def greet_user(name):
    """
    This function takes a person's name as a parameter and prints a greeting message.
    """
    print(f'Hey, {name}! Have a great day!')

# Example: Printing the function object (not calling it)
print('Function object:', greet_user)

# Calling the function with an argument
greet_user('Alice')

# Example: Function with parameters and a return value
def add_numbers(a, b):
    """
    Takes two numbers as parameters and returns their sum.
    """
    return a + b

# Calling the add_numbers function and printing the result directly
print('Sum of 3 and 5:', add_numbers(3, 5))

# Using main guard for script execution
if __name__ == "__main__":
    # You can call functions here if this script is run directly
    greet_user("Bob")
    total = add_numbers(10, 20)
    print('Total:', total)