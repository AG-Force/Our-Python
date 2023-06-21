a1 = "I love python and php"
print(a1.split())
# The split() method splits the string into a list of substrings at each occurrence of whitespace.
# Output: ['I', 'love', 'python', 'and', 'php']

a2 = "Ilovepythonandphp"
print(a2.split())
# The split() method splits the string into a list of substrings at each occurrence of whitespace.
# Since there is no whitespace in the string, the whole string becomes a single element in the list.
# Output: ['Ilovepythonandphp']

a3 = "I-love-python-and-php"
print(a3.split("-"))
# The split("-") method splits the string into a list of substrings at each occurrence of the hyphen ("-").
# Output: ['I', 'love', 'python', 'and', 'php']

a4 = "I-love-python-and-php"
print(a4.split("-", 2))
# The split("-", 2) method splits the string into a list of substrings at each occurrence of the hyphen ("-"),
# but limits the splitting to a maximum of 2 occurrences.
# Output: ['I', 'love', 'python-and-php']

a4 = "I-love-python-and-php"
print(a4.split("-", 2))
# This line is a duplicate of the previous line and has the same output.

a5 = "I-love-python-and-php"
print(a5.rsplit("-", 2))
# The rsplit("-", 2) method splits the string into a list of substrings at each occurrence of the hyphen ("-"),
# starting from the right side of the string and limiting the splitting to a maximum of 2 occurrences.
# Output: ['I-love-python', 'and', 'php']

a6 = "Osama"
print(a6.center(9))
# The center(9) method centers the string within a string of width 9 by adding spaces on both sides.
# Output: '  Osama  '

print(a6.center(15, "@"))
# The center(15, "@") method centers the string within a string of width 15 by adding "@" on both sides.
# Output: '@@@@Osama@@@@'

a7 = "I love python"
print(a7.count("love"))
# The count("love") method returns the number of occurrences of the substring "love" in the string.
# Output: 1

a8 = "I love python because python is easy to learn"
print(a8.count("python", 0, 35))
# The count("python", 0, 35) method returns the number of occurrences of the substring "python" in the string,
# but only within the specified range from index 0 to index 34 (exclusive).
# Output: 1

a9 = "I love python"
a10 = "i LOVE pYTHON"
print(a9.swapcase())
# The swapcase() method returns a new string where the case of each letter is swapped.
# Output: 'i LOVE PYTHON'

print(a10.swapcase())
# Output: 'I love Python'

a11 = "i love python"
print(a11.startswith("i"))
# The startswith("i") method checks if the string starts with the substring "i".
# Output: True

print(a11.startswith("S"))
# Output: False

a12 = "i love python"
print(a12.startswith("p", 7, 12))
# The startswith("p", 7, 12) method checks if the substring from index 7 to index 11 (exclusive) starts with "p".
# Output: True

a13 = "i love python"
print(a13.endswith("e", 2, 6))
# The endswith("e", 2, 6) method checks if the substring from index 2 to index 5 (exclusive) ends with "e".
# Output: False
