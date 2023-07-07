name = "Gassan"
age = 22
rank = 10 

print("My name is: %s" % "Gassan Abdalhamid \n")  # Printing a literal string
print("My name is: {}".format(name))  # Printing a literal string
print("My name is: {} and my age is {} and my rank us {}".format(name, age, rank))  # Printing a literal string
###############################################################################################
print("My name is: {:s}  my age is {:d} and my rank us {:.2f}".format(name, age, rank))  # Printing a literal string
##########################################################################################################################
print("My name is: {:s}  my age is {:d} and my rank us {:.2f}".format(name, age, rank))  # Printing a literal string
##########################################################################################################################
print("My name is: {:.2s}  my age is {:d} and my rank us {:.2f}".format(name, age, rank))  # Printing a literal string
##########################################################################################################################
myMoney = 1212121212
print("My Money in bank is: {}".format(myMoney))
print("My Money in bank is: {:,}".format(myMoney))
##########################################################################################################################
a, b, c = "one", "tow", "three"
print("Hello {} {} {}".format(a,b,c))
print("Hello {1} {2} {0}".format(a,b,c))
##########################################################################################################################
x, y, z = 10, 20, 30 
print("Hello {2:d} {1:d} {0:.2f}".format(x,y,z))
##########################################################################################################################
myName = "Ghassan"
myage = 22
print("My name is: {myName} and my age is: {myage}")
print(f"My name is: {myName} and my age is: {myage}")

#####################################Link zu PyFormat##########################################

#https://pyformat.info/