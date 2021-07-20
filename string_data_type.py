#String Data Type Lab
#Initializes value as string
#Prints value to screen >> stdout
#Prints "data type" of initialized variable

##String Data Type Example
myString="This is a string."
print(myString)
print(type(myString))
print(myString + " is of data type " + str(type(myString)))

##Concatenation Example
##Initializing (3) variables, then combining them together
firstString= "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


##Input variable into String from << StdInput
name =input("What is your name? ")
print(name)

##Output variable format String from >> stdout example
##Input values first from end user
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

#concatenated answer to input i.e format () function
print("{}, you like a {} {}!".format(name, color, animal))
