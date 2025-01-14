# name="mona sharma"
# print(id(name))
# print(name.capitalize(),id(name.capitalize()))#it capitalize the first letter
# name="mona sharma"
# #title
# print(name.title(),id(name.title()))

# name="mona sharma"
# #upper 
# print(name.upper(),id(name.upper()))

name="mona sharma"
# #lower
# print(name.lower(),id(name.lower()))


# #find
print(name.find('Ra'))
# print(name.find('sa'))
print(name.find('a'))

# #count
# print(name.count('a'))

# #index
# print(name.index('a'))

# #replace
# print(name.replace('a','p'),id(name.replace('a','p')))

# #split()
print(name.split(' '))
# print(name.split('e'))

# #isupper()
# print('sangee'.isupper())

# #islower()
# print('SAng'.islower())

# #isnumeric()
# print('Ats'.isnumeric())

# #isalpha()
# print('sang1'.isalpha())

# #isalnum()
# print('sang'.isalnum())


name='mona is a girl who have so many skills'
print(id(name))
print(id(name.title()))
print(id(name.capitalize()))
print(id(name.upper()))
print(id(name.lower()))

# Creating a tuple
my_tuple = (1, 2, 3)

# Attempting to change the first element of the tuple
try:
    my_tuple[0] = 10
except TypeError as e:
    print(e)  # This will print: 'tuple' object does not support item assignment
