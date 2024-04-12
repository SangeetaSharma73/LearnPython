#while- syntax


#1.Initializing value
#2.Loop COndition
#3.Updating value


# i=1   #initialize
#while condition(i<n): loop condition
    # print('while condition is true it will execute')
    # i+=1  #updating the vlaue

#print in a new line
i=1
while i<=10:
    print(i*5)
    i+=1

#print in a line
i=1
while i<=10:
    print(i*5,end=' ')
    i+=1
print() #by default take new line


#print all even number between 1to 10
i=1
while i<=10:
    if i%2==0:
        print(i,end=' ')
    i+=1
print()

# print the sum of all number from 1 to 5
i=1
add=0
while i<=5:
    add+=i
    i+=1
print(add)
