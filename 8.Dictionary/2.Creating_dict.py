#creating empty dictionary

d=dict()
print(d,type(d))
print(id(d))
dt={}
print(dt,type(dt))
print(id(dt))


#creating non empty dict
d={1:0,2:4,3:1}
print(d,type(d),id(d))

#zip 
name=['apple','mango','banana']
prices=[120,100,130]
fruit=dict(zip(name,prices))
print(fruit)

#length
print(len(fruit))
