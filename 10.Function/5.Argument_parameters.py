# Parameters: the values we pass while defining a funcion
# Arguments: The actual value of we pass when calling  function
def func(name):
    print('Hey my name is',name)
a=func('Sangeeta')
print(a)#sangeeta is a actual value that we called argument

#positional arguments-The value you pass when calling a function are matched accroding to their positions
def intro(name,hobby):
    print('Hey my name is',name)
    print('And my hobby is',hobby)

intro('Rahul','dancing')
#default arguments 
# giving default values to the parameters
#for these parameters passing value in arguments is optional

def intro(name,hobby='reading'):
    print('hey this is ',name)
    print('And my hobby is',hobby)
intro('Rahul')
intro('prateek','swim')

#default follows non default arguments
# def intro(name='Rahul',hobby): #there will be error if we make default argument before non defulat arguments
#     print('hey this is ',name)
#     print('And my hobby is',hobby)
    
#arbitary arguments
'''when number of values you want to pass is not known
   Like we pass multiple values in print function
   The values are being stored in tuple.
'''
def test(*args):
    print(args)
    print(type(args))
    for i in args:
        print(i,end=' ')
a=test(2,3,4,'riya',2.3)
print(a)
test(2,4,5)
print(type(test))

#keyword arguments
# variable number of key word arguments 
#it stores the data in dictionary format

def intro(**kwargs):
    print(kwargs,type(kwargs))
    for key,values in kwargs.items():
        print(key,values,sep=" : ")
        
intro(name='Ritesh',age=23,hobbies=['Swim','read'])

def mix(a,b,c,age=34,*args,**kwarks):
    print(a,b,c)
    print(age,type(age))
    print(args,type(args))
    print(kwarks,type(kwarks))
# mix(2) #TypeError: mix() missing 2 required positional arguments: 'b' and 'c'
mix(2,4,5)
mix(2,4,5,45,6,8,9,name='mona',hobby='dance')

