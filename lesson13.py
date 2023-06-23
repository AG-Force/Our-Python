a = " I love python"

print(a.index("p"))
print(a.index("p", 0, 10))
#print(a.index("p", 0, 5))

###########################################################

print(a.find("p"))
print(a.find("p", 0, 10))
print(a.find("p", 0, 5))

###########################################################
c = "Osama"
print(c.rjust(10))
print(c.rjust(10, "#"))
print(c.ljust(10, "#"))
###########################################################
d = """ First line
second line
third line
"""

print(type(d.splitlines()))
print(d.splitlines())
###########################################################
f = "First line\nsecond line \nThird line\n"

print(f.splitlines())
###########################################################
g = "Hello\tworld\t\ti\tlove\tpython"
print(g.expandtabs(2))
###########################################################
one = "I Love Python An 3D"
print(one.istitle())
###########################################################
tow = ""
print(tow.isspace())
###########################################################
three = "i love python "
print(three.islower())
###########################################################
four = "Gassan_Abdalhamid"
five = "#wewe"
print(four.isidentifier())
print(five.isidentifier())
###########################################################
x = "AAAAABBBB"
print(x.isalpha())
###########################################################
z = "234dsfsdfsdf"
print(z.isalnum())