#2d list- A 2D list in Python is a list of lists. It's a data structure that represents a table or a grid with rows and columns, where each element in the outer list represents a row, and each element in the inner lists represents an individual element within that row
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l=[l1,l2,l3]
print(l)

#append the list into list
l.append([5,8,6])
print(l)

#accessing the 2d list element
print(l[2])#accessing fifth rows
print(l[1][1])#accessing first row first index element


#using loop
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j],end=' ')
    print()
        
        
#list comprehension
for i in range(10):
    print(i)

l=[]
for i in range(10):
    l.append(i)
print(l)

l=[i for i in range(10)]
print(l)

a=[i**2 for  i in range(5)]
print(a)


#Q1-Given a list of population sensus done by gol. you need to find the total population
l=[4,5,6,7,5,4,3]
#access all the elements of this list
for i in l:
    print(i,end=' ')
print()

population=0
for i in l:
    population+=i
print(population)