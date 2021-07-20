# Numeric Data Types
#Lab exercise explaining the different data types
##Line 1 Initializes the value
##Line 2 Retrieves value assignment
##Line 3 Get[returns] "data type" of variable initialized 
##Line 4 Formats value to string data type and resturn to StdOut

##Int Data Type
print("Python has 3 numeric types: int, float, complex")
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of data type " + str(type(myValue)))

##Float Data Type
myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of data type " + str(type(myValue)))

##Complex Data Type
myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of data type " + str(type(myValue)))

#Bool Data Type "fake data type"
myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of data type " + str(type(myValue)))
