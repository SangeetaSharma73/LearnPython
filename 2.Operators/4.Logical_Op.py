#Logical- and , or, not
print( 3 <5 and 4==3 ) # all condition should be true then true so for part 3 < 5 it is true but second part 4 ==3 is false , in finall we get false
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or

print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not
print( 'Not',not 3)
print(not 0)
print(not 1)
print(not False)
print(not True)
print(not 2<3)
print(not 5==4)

#special operator
name='Riya and Tiya'
print('R' in name)
print('i' in name)

a=2
b=4
c=2
print(a is b)
print('is',id(a) is id(b) )
print(id(a) is id(c))

'''
Feature	        id()	                   is	                        ==
1.Checks?       Memory address             Identity (same              Value 
                of an object               object in memory)           (contents
                                                                        of the object)
2.Returns?      Unique integer              True if both               True if values 
                (memory location)           refer to the                are equal
                                            same object
                
3.Mutable       Can have different         Can be False even            can be True
Objects         ids if modified            if values are the            even if object
                                            the same                    s are diff
                                                                        erent
'''

# 📌 Example 1: id(), is, and == with Integers
a = 10
b = 10
print(id(a), id(b))   # Same memory address (Python caches small integers)
print(a is b)         # ✅ True (Both refer to the same memory location)
print(a == b)         # ✅ True (Values are equal)

# ✅ Python optimizes memory and reuses small integers (-5 to 256), so a and b share the same memory location.

# 📌 Example 2: id(), is, and == with Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1), id(list2))   # Different memory addresses
print(list1 is list2)         # ❌ False (Different objects)
print(list1 == list2)         # ✅ True (Same values)
# ❌ is is False because list1 and list2 are different objects, even though their values are the same.

# 📌 Example 3: is vs. == with Mutability
x = [1, 2, 3]
y = x  # Both point to the same object

print(x is y)  # ✅ True (Same object)
print(x == y)  # ✅ True (Same values)

y.append(4)  # Modifies the list
print(x)  # [1, 2, 3, 4] (Affects both x and y)

# ✅ Since y = x assigns a reference, is returns True. Modifying y also changes x.

# 📌 Example 4: Using id() to Understand Object Identity
a = 500111111
b = 500111111
print(id(a), id(b))   # Different (same) memory addresses (Large integers not cached) because of python version
print(a is b)         # ❌ False # True for this version of python
print(a == b)         # ✅ True

# ❌ Python does NOT cache large integers (outside -5 to 256), so is is False.

a = 500111111
b = int("500111111")  # Creating from string forces a new object
print(id(a), id(b))  # ❌ Different memory addresses
print(a is b)        # ❌ False
print(a == b)        # ✅ True
