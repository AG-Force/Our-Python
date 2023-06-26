# Assigning values to the variables
name = "Gassan Abdalhamid"
age = 36
rank = 10

# Printing variables using the string format syntax (using %s and %d)
print("My name is: %s" % "Gassan Abdalhamid \n")  # Printing a literal string
print("My name is: %s and my Age is %s" %(name,age))  # Printing two strings (age is treated as string here)

print("My name is: %s and my Age is %d" %(name,age))  # Printing string and integer (age is treated as integer here)
print("My name is: %s and my Age is %d and my rank is %f" %(name,age,rank))  # Printing string, integer and float

# Assigning new values to the variables
n = "Ghassan"
l = "Python"
y = 10

print("My name is %s I am a %s Developer with %d years of experience " %(n,l,y))  # Printing two strings and an integer

mynumber = 10  # Defining a number variable
print("My number is: %d" %(mynumber))  # Printing an integer
print("My number is: %.2f" %(mynumber))  # Printing a number as float with 2 decimal places

myLongstring = "Hello People "  # Defining a long string
print("First 5 characters of the message is %.5s" %myLongstring)  # Printing first 5 characters of the string
