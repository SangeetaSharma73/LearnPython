#string formatting

name='Rahul'
age=25
print('Hey my name is {} . my age is {}'.format(name,age))

print('Hey my name is {name}.My age is {age}.')
print(f"hey my name is {name} and my age is {age}")

#string concatenation
str1='sang'
str2='eeta'
print(str1+str2)

str1=123
str2='Sangeeta'
print(str2+str(str1))


#Q1-Print all vowels of a given string

text='The quick brown fox jumps over the lazy dog'
for i in text:
    if i in 'aeiou':
        print(i,end='')
print()


#Q2- print str is palindrome or not
string='radar'
if string==string[::-1]:
    print('Yes')
else:
    print('No')