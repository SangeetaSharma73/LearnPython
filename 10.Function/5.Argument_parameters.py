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
