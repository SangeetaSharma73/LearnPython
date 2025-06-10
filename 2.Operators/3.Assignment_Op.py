# Initialize a variable for demonstration
a = 10

print("Initial value of a:", a) # Output: Initial value of a: 10

## Add and Assign (+=)
# Adds the right operand to the left operand and assigns the result to the left operand.
# Equivalent to: a = a + 1
a += 1
print("After a += 1, a is:", a) # Output: After a += 1, a is: 11

## Subtract and Assign (-=)
# Subtracts the right operand from the left operand and assigns the result to the left operand.
# Equivalent to: a = a - 1
a -= 1
print("After a -= 1, a is:", a) # Output: After a -= 1, a is: 10

## Multiply and Assign (*=)
# Multiplies the right operand by the left operand and assigns the result to the left operand.
# Equivalent to: a = a * 2
a *= 2
print("After a *= 2, a is:", a) # Output: After a *= 2, a is: 20

## Exponentiate and Assign (**=)
# Raises the left operand to the power of the right operand and assigns the result to the left operand.
# Equivalent to: a = a ** 2
a **= 2
print("After a **= 2, a is:", a) # Output: After a **= 2, a is: 400

## Floor Divide and Assign (//=)
# Divides the left operand by the right operand using floor division (discards the fractional part)
# and assigns the result to the left operand.
# Equivalent to: a = a // 2
a //= 2
print("After a //= 2, a is:", a) # Output: After a //= 2, a is: 200 (400 // 2 = 200)

## Divide and Assign (/=)
# Divides the left operand by the right operand and assigns the result to the left operand.
# The result will always be a float.
# Equivalent to: a = a / 2
a /= 2
print("After a /= 2, a is:", a) # Output: After a /= 2, a is: 100.0 (200 / 2 = 100.0) | After this we get float type

## Modulo and Assign (%=)
# Divides the left operand by the right operand and assigns the remainder to the left operand.
# Equivalent to: a = a % 3
a = 10 # Reset 'a' for a clear modulo example
a %= 3
print("After a %= 3 (with a=10 initially), a is:", a) # Output: After a %= 3 (with a=10 initially), a is: 1 (10 % 3 = 1)