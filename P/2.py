class Print:
    
    def __init__(self,name,age,pin):
        self.name=name
        self._age=age
        self.__pin=pin
        
    def __privateFun(self):
        print("it is private Fun")
        
    def _protectedFun(self):
        print("protected fun")
    
    def myName(self):
        print(self.name)
        
obj=Print("Sangeeta",23,123)
print(obj.myName())
# print(obj.__privateFun())
print(obj._protectedFun())