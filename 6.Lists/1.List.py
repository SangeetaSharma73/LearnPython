# Data Structure-A data structure is a specialized format for organizing, processing, retrieving and storing data.

#list- ordered collection of data
#list are mutable type of data structure
#it can contain multiple type of data
#List are iterable

lst=list()
print(lst,type(lst))
l1=[1,2,3,4,7]
print(type(lst)) # list

#Accessing item using index and index start from 0 
print(l1[0],l1[1],l1[4])

#Access item using neg index
print(l1[-1],l1[-2],l1[-4])

#Basic
arr=[1,2,4,3]
print(id(l1))
arr2=arr
arr2[1]=5
print(arr,arr2,"both value")
arr3 = [1,2,3]
arr4= [1,2,3]
arr4[1]=10
print(arr4,arr3)
print("s1",id(arr2),id(arr))
print(id([]),id([]))
print(id([1]),id([2]))
a=[]
b=[]
print(id(a),id(b))

a1=[1]
a2=[2]
print(id(a1),id(a2))

#mutablity
arr=[14,45,78]
print(id(arr))
arr[2]=34
print(arr,id(arr))

#Accessing all element
for i in range(len(arr)):
    print(arr[i])


#Slicing
l=[1,5,6,4,3]
print(l[0:4])
print(l[::-1])
print(l[:2])
print(l[1:])
print(l[:])