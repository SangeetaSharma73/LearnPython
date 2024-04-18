#Using key
fruit={
    'Apple':12,
    'Banana':34
}

print(fruit,fruit['Apple'])
# print(fruit['Mango'])get an error

#using get we will not get error we will get none if key not exist
print(fruit.get('Guava'))

#print another msg if key not exist 
print(fruit.get('Papaya','Not found'))

# updating the existing value
fruit['Apple']=340
print(fruit)

fruit['guava']=1
print(fruit)

#update
new={'Grapes':120,'oranges':23,'berry':2}

new={'Apple':21,'mango':100,'lichi':1}
fruit.update(new)
print(fruit)

#citizenship check
print('Apple' in fruit)


#dict.pop(key)
fruit.pop('apple')
print(fruit)

#dict.popitem()
fruit.popitem()
print(fruit)

#del object

fruit={'A':2,'B':2,'d':5}
del fruit
print(fruit)
