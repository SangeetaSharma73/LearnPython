# Initialize variables for demonstration
a = 3
b = 2

## Equality Operator (==)
# Checks if two values are equal.
# Importantly, it checks both the value AND the data type.
print("'2' == 2:", '2' == 2)   # Output: '2' == 2: False (different types: string vs. integer)
print("a == b:", a == b)       # Output: a == b: False (3 is not equal to 2)
print("3 == 3:", 3 == 3)       # Output: 3 == 3: True (3 is equal to 3)

## Inequality Operator (!=)
# Checks if two values are not equal.
print("a != b:", a != b)       # Output: a != b: True (3 is not equal to 2)
print("4 != 4:", 4 != 4)       # Output: 4 != 4: False (4 is equal to 4)

## Less Than or Equal To Operator (<=)
# Checks if the left value is less than or equal to the right value.
print("a <= b:", a <= b)       # Output: a <= b: False (3 is not less than or equal to 2)
print("2 <= 2:", 2 <= 2)       # Output: 2 <= 2: True

## Greater Than or Equal To Operator (>=)
# Checks if the left value is greater than or equal to the right value.
print("a >= b:", a >= b)       # Output: a >= b: True (3 is greater than or equal to 2)
print("3 >= 3:", 3 >= 3)       # Output: 3 >= 3: True

## Less Than Operator (<)
# Checks if the left value is strictly less than the right value.
print("4 < 5:", 4 < 5)         # Output: 4 < 5: True
print("5 < 4:", 5 < 4)         # Output: 5 < 4: False

## Greater Than Operator (>)
# Checks if the left value is strictly greater than the right value.
print("5 > 4:", 5 > 4)         # Output: 5 > 4: True
print("4 > 5:", 4 > 5)         # Output: 4 > 5: False