###############################lesson25 according youtube.  Lists###############################
myTuple1 = ("Osama")
myTuple2 = "Osama"
print(myTuple1)
print(myTuple1)
print(type(myTuple2))
print(len(myTuple2))

print(type(myTuple1))
#########################
myTuple3 = ("Osama",)
myTuple4 = "Osama",
print(type(myTuple3))
print(type(myTuple4))
print(len(myTuple4))
######################### Tuple concanation################
a = (1, 2, 3, 4)
b = (5, 6)
c = a + b
print(c)
d = a + ("Test",)+ b
print(d)
######################### Tuple, List, String, Repeat(*)################
Mystring = "Gassan"
Mylist = [1,2]
MyTuple = ("A", "B")
print(Mystring * 6)
print(Mylist * 6)
print(MyTuple * 6)
######################### Methods => count()
t = (1,2,3,4,5,6,7,8,9,9,9,9,9)
print(t.count(9))
######################### Methods => index
z = (1,2,3,4,5,6,7,8,9)
print("The position of 7 is: {} ".format(z.index(7)) )
print("The position of 7 is: {:d} ".format(z.index(7)) )
print(f"The position of 7 is: {(z.index(7))} ")
######################### Tuple Destruct

#a = ("A", "B", "C")
#x, y, z1 = "A","B","C"
#print(a)
#print(x)
#print(y)
#print(z1)
######################################
#a = ("A", "B", "C")
#x, y, z1 = a
#print(a)
######################################
a = ("A", "B",4, "C")
x, y,_, z1 = a
print(x)
print(y)
print(z1)



