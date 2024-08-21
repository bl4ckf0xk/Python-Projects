class MyClass: 
    __hiddenVariable = 0
    
    def add(self, increment): 
        self.__hiddenVariable += increment 
        print(self.__hiddenVariable)

# Driver code 
myObject = MyClass()      
myObject.add(2) 
myObject.add(5) 
  
# Correct way to access the hidden variable
print(myObject._MyClass__hiddenVariable)  # This will work
