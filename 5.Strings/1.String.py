#String- is a sequence of characters
#whatever inside the single,double and triple quotes are called strings

#multiline string- whatever written in triple quotes 

string='I am this'
# arr = [1,2,3]
# arr[1]=5
# print(arr)
# string[0]='S'
print(string)
print(type(string))
string1='''this is the 
multiline string
'''
print(string1)



a='abc'
b='abc'
print(a is b)
# 🔹 Why is a is b Returning True for Strings?
# In Python, small strings are interned (cached) for memory optimization. This means that identical string literals are stored in the same memory location.

a = "abc"
b = "".join(["a", "b", "c"])  # Created dynamically
print(a is b)  # ❌ False (Different objects)
print(a == b)  # ✅ True (Same value)
# 👉 Since b is created at runtime, Python does NOT intern it.

# 📌 Example: Long Strings Are NOT Interned
a = "this_is_a_very_long_string"
b = "this_is_a_very_long_string"
print('long string',a is b)  # ❌ False (Python does not intern long strings)
print('long string',a == b)  # ✅ True (Same value)

# 🔹 Python typically interns short strings (like "abc", "hello"), but long strings may not be cached.



'''In Python, the term "unchangeable" (or "immutable") usually refers to objects whose individual elements cannot be modified after the object is created. However, when we talk about sets in Python, we need to clarify a few important points:

Understanding Set Mutability and "Unchangeable" Nature:
Set Mutability (Modifying the Set Itself):

A set in Python is mutable, meaning you can add or remove elements from the set after its creation. This makes sets modifiable as a collection.
You can add or remove elements, but you cannot modify individual elements within the set.'''

my_set = {1, "apple", (3, 4)}  # All elements are immutable
print(my_set)  # Output: {1, 'apple', (3, 4)}

# my_set = {[1, 2], 3}  # This will raise a TypeError because lists are mutable

'''What Makes Sets Special:

Sets are unordered: The order of elements in a set is not guaranteed. This is why sets are different from lists and tuples.
Sets are unique: A set cannot have duplicate elements. This is why sets are useful when you need to store only unique items.
Mutable but with Immutable Elements: While the set as a collection is mutable (you can add/remove elements), the elements themselves must be immutable.
'''