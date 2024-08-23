
def fun():
    x='this'
    

fun()
# print('my x var',x)#NameError: name 'x' is not defined


def fun():
    global x
    x='this'
    

fun()
# print('my x var',x)#NameError: name 'x' is not defined