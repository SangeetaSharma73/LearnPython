#set 
#Unique collection
#unordered
#unindexed
#Mutable


lst=[1,2,3,1,1]
print(lst)


#creating a set

#empty set 
s={}
print(s,type(s),id(s))

s=set()
print(s,type(s),id(s))

#non empty set
s={1,1,2,3,4}
print(s)

st='hello'
print(set(st))
print(st[1])

#iteration
s={'a','h','r','u'}
for i in s:
    print(i)

# for i in range(len(s)): TypeError: 'set' object is not subscriptable
#     print(s[i])

#convert list into set
lst=[2,3,4,2]
sett=set(lst)
print(lst,type(lst),sett,type(sett),id(lst),id(sett))
