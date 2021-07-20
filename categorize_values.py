#This lab will define a list with different data types

##List myMixedBagList variable initialization
##[Integer, Integer, float, Bool, String, String]
myMixedBagList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

##Example of a for loop
for item in myMixedBagList:
    print("{} is of data type {}".format(item, type(item)))     