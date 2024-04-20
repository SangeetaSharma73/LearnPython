#Lambda Function- These are mainly used when we need nameless functions for short period of time

def add(a,b):
    return a+b
add(3,4)
a=add(4,5)
print(a)

ans=(lambda a,b:a+b)(33,4)
print(ans)
fuct=lambda a,b:a+b
print(type(fuct),fuct(5,4))

def larger(a,b):
    if a>b:
        return a
    else:
        return b
largest=larger(43,5)
print(largest)

funct=lambda x,y:x if x>y else y
print(funct(43,58))

lst=[(12,56),(2,4),(5,3)]
lst.sort()
print(lst) #[(2,4),(5,3),(12,56)]

def k(x):
    return x[1]
lst.sort(key=k)
print(lst)#[(5,3),(2,4),(12,56)]

lst=[(12,56),(2,4),(5,3)]
lst.sort(key=lambda x:x[1])
print(lst)


#print all even no

input=[1,3,4,5,6,7,8]
def even(li):
    for i in li:
        if i%2==0:
            print(i,end=' ')
even(input)

lst=[1,2,3,1,2,4]
def unique(li):
    new=[]
    for i in li:
        if i not in new:
            new.append(i)
    
    print(new)
a=unique(lst)
print(a)




