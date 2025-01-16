#count- returns the count of an object
l=[100,23,34,1,23,5,23]
print(l.count(23))#3

#append- insert the element at the last of list
l.append(45)
print(l)

#index- return the index of list occurence of an object
print(l.index(23))

#pop- remove element from the last
l.pop()
print(l)

# remove- removes the given object from our list
print(l.remove(1))

#sort- sort an arr in descending ar ascending
l.sort()
print(l)

#insert - insert an ele at a given index
arr=['siya','tiya','jiya']
arr.insert(1,'Hi')
print(arr)

a=[1,2,3,4]
a2=[2,3]
# a+=a2
a.append(a2)
print(a)

a1=[]
a1+=[12,3]
print(a1)
a1+=arr[3]
print(a1)
a1+=[5]
print(a1)

#extend

arr=[1,23,4]
arr1=[4,2,3]
arr.extend(arr1)
print(arr)

#Heterogeneous list- it contain different type of data in it
arr=[1,'jiya',3.4]
print(arr)