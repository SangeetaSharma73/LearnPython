# Tuples-like list tuples are also ordered collection of data , unchangeable , iterable, can be heterogeneous
tple=tuple()
print(tple,type(tple))

tp=('mera','name','mona','hai')
print(tp)

for i in range(len(tp)):
    print(tp[i])

tp=('rani',1,True)
print(tp)
# tp[0]='pina' #TypeError: 'tuple' object does not support item assignment
# print(tp)

#creating empty tuple
t=()
print(t,type(t))

t=(4)
print(type(t))

t=(5,)
print(type(t))

tp=('Rahul')
print(tp)
tp=tuple('Rahul')
print(tp)

#mutability
t=(2,3,4)
print(t,t[0])
# t[0]=45 immutable
print(t)

#unpacking tuple
a=2
b=3
c=5
d=4
print(a,b,c,d)
a,b=2,4
print(a,b)

t=(1,2,3,4)
print(t)

a,b,c,d=t
print(a,b,c,d) #this process is known as unpacking

t=(1,2,3,4,1)
print(t)

#count
print(t.count(1))
print(t.count(100))

#index
print(t.index(2))

#iteration
for i in t:
    print(i)
    
t1=(5,6)
t2=t+t1
print(t2)
print(t2*2)

#tuple to list and list to tuple
print(t,type(t),list(t),type(t))

lst=list(t)
print(type(lst))
