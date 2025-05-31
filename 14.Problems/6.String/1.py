# Basic String Questions

# 1. What are the different ways to create a string in ?

st = ""
print('my string',st)

st = ''
st = ''' this is multiline string'''
st = """ this is second multiline string """


st = str()
print(st,'st')

# How do you find the length of a string in ?
st1 = 'babita singh'
print(len(st1))


# What is string immutability in ? Can you modify a string after creating it?
# st1[0] = 'S'
# print(st1)


# How do you concatenate two strings in ?
st1 += st
print(st1)

# In , you can concatenate (combine) two or more strings using different methods. Here are some of the most common ways:

# 1. Using the + Operator
# The + operator is the simplest way to concatenate strings.




s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(result)  # Output: Hello World
# 2. Using the += Operator (Augmented Assignment)
# You can use += to append a string to an existing one.




# s = "Hello"
# s += " World"
# print(s)  # Output: Hello World


# 3. Using join() Method
# The join() method is efficient when concatenating multiple strings from a list or tuple.

words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Output: Hello World


# 4. Using format() Method
# The .format() method allows inserting multiple values dynamically.

s1 = "Hello"
s2 = "World"
result = "{} {}".format(s1, s2)
print(result)  # Output: Hello World



# 5. Using f-strings ( 3.6+)
# F-strings provide a clean and modern way to format strings.

s1 = "Hello"
s2 = "World"
result = f"{s1} {s2}"
print(result)  # Output: Hello World



# 6. Using % Formatting (Old Method)
# Older versions of  use % for string formatting.

s1 = "Hello"
s2 = "World"
result = "%s %s" % (s1, s2)
print(result)  # Output: Hello World

# 7. Using reduce() Function (For Large Concatenations)
# If you have a large number of strings, reduce() from functools can be used.

from functools import reduce


words = ["Hello", "this", "World"]
result = reduce(lambda x, y: x + " " + y, words)
print(result)  # Output: Hello this World

# Which method should you use?
# Use + operator for small, simple concatenations.
# Use join() when concatenating multiple strings from a list (more efficient).
# Use f-strings if formatting variables within a string (cleaner and modern).
# Would you like a detailed explanation of any method? 



# How can you access individual characters in a string?

st = 'babita singh'
print(st[0],st[len(st)-1])


# What is the difference between isupper(), islower(), and title() methods?
print(st.title())


# How can you convert a string to uppercase and lowercase?
print(st.upper())

print(st.lower())

# What is the difference between find() and index() in Python?

print('diyad'.find('d')) #if we will find the character or a string or substring which string does not contain then it will return -1 else the first index of that substring 

# print('diyad'.index('s'))  #ValueError: substring not found
print('diyad'.index('d')) 



# How do you replace a substring within a string?

# str = 'thisis my name' 

# # str = 'this is my name'

# newSt = ""

text = "Hello World, Welcome to the World!"
replace = text.replace('World','Universe')
print(replace)

# ✅ Note: By default, it replaces all occurrences.

# Replacing Only a Specific Number of Occurrences
# If you want to replace only the first occurrence, pass the third argument (count):
text = " Hello World, Welcome to the World! "
result = text.replace('World','Universe',1)
print(result)


# How can you remove leading and trailing spaces from a string?

print(text.strip())



# String Slicing and Indexing
# What is string slicing? How does it work in Python?
# print(st[stIndex,lastIndex,Jump])
print(text[2:10:2])
print(text[:])
print(text[::-1])

# How do you reverse a string using slicing?
print(text[::-1])
# How can you extract the first three and last three characters of a string?
text = 'hello world'
print(text[:3]+text[len(text)-3:])
# How can you get every second character from a string?
print(text[1::2])
# What happens when you use negative indexing in a string?
print(text[-3:-5:-1])



# String Formatting
# What is the difference between %, .format(), and f-strings in Python?
var1 = 23
print("my %a" % (var1))
print('my age {} is given here'.format(var1))
print(f"my age {var1} is given")
# How do you format a string to display a float with two decimal places?
val = 23
print(f"{val:.2f}")
# How do you dynamically insert values into a string?

# How do you format a string with multiple placeholders?


# String Searching and Manipulation
# How do you check if a substring exists in a string?
# How can you count the occurrences of a substring in a string?
# How do you split a string into a list of words?
# How do you join a list of words into a single string?
# How can you check if a string starts with or ends with a particular substring?
# How do you remove all occurrences of a given character from a string?


# Regular Expressions in Strings
# How do you check if a string contains only digits?
# How do you extract numbers from a string?
# How do you remove special characters from a string?
# How can you validate an email address using regex?
# How do you replace multiple spaces with a single space in a string?

# Advanced String Problems
# How do you check if two strings are anagrams of each other?
# How do you find the longest common prefix of a list of strings?
# How can you find the most frequent character in a string?
# How do you check if a string is a palindrome?
# How do you compress a string using Run-Length Encoding (RLE)?
# How do you check if one string is a rotation of another?
# How do you remove duplicate characters from a string?
# How do you find the first non-repeating character in a string?
# How do you count the number of vowels and consonants in a string?
# How do you reverse the words in a string while keeping the word order intact?

# Coding Challenges
# Reverse a string without using built-in functions.
# Find the longest word in a given sentence.
# Find the shortest word in a given sentence.
# Check if two strings are permutations of each other.
# Convert a given string to CamelCase or SnakeCase.
# Implement a function to check if a string contains balanced parentheses {} [] ().
# Find all substrings of a string.
# Remove all duplicate words from a given sentence.
# Convert a given sentence to title case (capitalize the first letter of each word).
# Find the longest palindromic substring in a given string.