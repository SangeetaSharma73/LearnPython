#add: for single element
#update(iterable)

s={1,2,3,3,4,5}
print(s,id(s))

s.add(8)
print(s,id(s))

#update
s={1,2,3,4}
name='Siya'
s.update(name)
print(s)

#Deleting an element
#pop: removes random element. We are not sure what it is
#remove element: Removes particular element

s={1,2,3,4,'R',"a",'t'}
print(s)
print(s.pop())
print(s.pop())
print(s)
#remove
s.remove('a')
print(s)

# print(s.remove('p')) KeyError: 'p'
