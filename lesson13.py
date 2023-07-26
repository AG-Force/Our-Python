a = " I love python"

print(a.index("p"))                # Output: 7
print(a.index("p", 0, 10))         # Output: 7
# print(a.index("p", 0, 5))        # This line is commented out

print(a.find("p"))                 # Output: 7
print(a.find("p", 0, 10))          # Output: 7
print(a.find("p", 0, 4))           # Output: -1

c = "Osama"
print(c.rjust(20))
print(c.rjust(20, "#"))
print(c.ljust(10, "#"))

d = """ First line
second line
third line
"""

print(type(d.splitlines()))        # Output: <class 'list'>
print(d.splitlines())               # Output: [' First line', 'second line', 'third line']

f = "First line\nsecond line \nThird line\n"

print(f.splitlines())              # Output: ['First line', 'second line ', 'Third line']

g = "Hello\tworld\t\ti\tlove\tpython"
print(g.expandtabs(2))             # Output: Hello world  i love python

one = "I Love Python An 3D"
print(one.istitle())               # Output: True

tow = ""
print(tow.isspace())               # Output: True

three = "i love python "
print(three.islower())             # Output: True

four = "Gassan_Abdalhamid"
five = "#wewe"
print(four.isidentifier())         # Output: True
print(five.isidentifier())         # Output: False

x = "AAAAABBBB"
print(x.isalpha())                 # Output: True

z = "ss"
print(z.isalnum())                 # Output: True
