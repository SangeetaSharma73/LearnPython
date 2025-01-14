#ord and chr
print(ord('a'),ord('z'))#ASCII value
print(ord('A'),ord('Z'))#ASCII value
print(ord('🎉'))

name='Sangeeta Sharma'
#accessing the element
for i in range(len(name)):
    print(name[i],end=' ')
print()

#Slicing: 

print(name[0:3:2])
print(name[:2:-2])

#this will give whole string
print(name[:])

#negative slicing
print(name[::-1])
print('test',name[1:2:-1])
