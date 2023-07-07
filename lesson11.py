a = "I love python"
print(len(a))
# The len() function returns the length of the string.
# Output: 13

a = "     I love python    "
print(a.strip())
# The strip() method removes leading and trailing whitespace characters from the string.
# Output: "I love python"

print(a.rstrip())
# The rstrip() method removes trailing whitespace characters from the string.
# Output: "I love python"

print("test2" + a.lstrip() + "test")
# The lstrip() method removes leading whitespace characters from the string.
# Output: "I love python     "

print(len(a.strip()))
# Output: 13

print(len(a.rstrip()))
# Output: 13

print(len(a.lstrip()))
# Output: 18 (including the trailing whitespace)

a1 = "    #################hier I love python   "
print(a1.strip())
# The strip() method removes leading and trailing "#" characters from the string.
# Output: "I love python"

print(a1.rstrip())
# The rstrip() method removes trailing "#" characters from the string.
# Output: "#################I love python"

print(a1.lstrip())
# The lstrip() method removes leading "#" characters from the string.
# Output: "I love python     "

a2 = "#############@@@@@@@####I love python#####@@@@#################"
print(a2.strip("#@"))
# The strip("#@") method removes leading and trailing "#" and "@" characters from the string.
# Output: "I love python"

print(a2.rstrip("#@"))
# The rstrip("#@") method removes trailing "#" and "@" characters from the string.
# Output: "#############@@@@@@@####I love python"

print(a2.lstrip("#@"))
# The lstrip("#@") method removes leading "#" and "@" characters from the string.
# Output: "I love python#####@@@@#################"

b = "i love your pets 3m"
print(b.title())
# The title() method capitalizes the first character of each word in the string.
# Output: "I Love Your Pets 3M"

b1 = "i love your pets 3g"
print(b1.capitalize())
# The capitalize() method capitalizes only the first character of the string.
# Output: "I love your pets 3g"

c, d, e, f = "1", "11", "111", "1111"
print(c.zfill(3))
# The zfill(3) method pads the string with zeros on the left until it reaches a width of 3.
# Output: "001"

print(d.zfill(3))
# Output: "011"

print(e.zfill(4))
# Output: "0111"

print(f.zfill(5))
# Output: "11111"

g = "osama"
print(g.upper())
# The upper() method converts the string to uppercase.
# Output: "OSAMA"
