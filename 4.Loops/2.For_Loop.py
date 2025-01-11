# range() function allows users to generate series of numbers
# it is iterable as well
# but last value is excluded from the range function

#range(start_val,end_val,jump_val)

print(list(range(1,5,2))) #[1,3]
print(list(range(10,0,-1)))


#for loop
#i:iterator
#range():iterable

for i in range(1,10,3):
    print(i)

for i in range(10):
    print(i)
    
#Pattern1
n=4
for i in range(n):
    print('# '*n) # # # #

for i in range(n): # 4
    for j in range(n): # i=0,1,2,3 , j=0 , 1
        print('#',end=' ') # # # #
                           # # # #
                           # # # #
                           # # # #
        
    print()


#Pattern 2
for i in range(n):
    for j in range(i+1):
        print('#',end=' ')
    print()
    
