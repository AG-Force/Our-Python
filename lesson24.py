###############################lesson26 according youtube.  Lists###############################
# Not Ordered and not indexed
MySetOne = {"Gassan", "Abdalhamid", 100}
print(MySetOne)
#### tuple example 
myTuple = (1, 2, 3, 4, 5, 6)
print(myTuple[0:3])

# sclicing can't be done  
MySetTow = {"Gassan", "Abdalhamid", 100}
# print(MySetTow[0::3])

# Has only immutable Data Types
######MySetThree = {"Osama", 100, 100.5, True, [1,2,3]} Error: unhashable type: 'list'
######print(MySetThree) Error: unhashable type: 'list'

MySetThree = {"Osama", 100, 100.5, True, (1,2,3)} 
print(MySetThree) 
# Item is unique 
mySetFour = {1,2, "Osama", "One"}
print(mySetFour)
mySetFour = {1,2, "Osama", "One", "Osama"}
print(mySetFour)
