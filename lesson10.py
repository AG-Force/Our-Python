# Indexing
mystring1 = "i love python "
print(mystring1[0])  # Outputs: 'i' - Retrieves the character at index 0

mystring2 = "i love python "
print(mystring2[9])  # Outputs: 't' - Retrieves the character at index 9

mystring3 = "i love python"
print(mystring3[-1])  # Outputs: 'n' - Retrieves the last character using negative indexing

# Slicing
mystring4 = "i love python"
print(mystring4[8:11])  # Outputs: 'pyt' - Retrieves a substring from index 8 to 10 (not inclusive)

mystring5 = "i love python"
print(mystring5[3:4])  # Outputs: 'o' - Retrieves a substring from index 3 to 4 (not inclusive)
print(mystring5[:4])  # Outputs: 'i lo' - Retrieves a substring from the start to index 4 (not inclusive)
print(mystring5[5:])  # Outputs: 'python' - Retrieves a substring from index 5 to the end
print(mystring5[:])  # Outputs: 'i love python' - Retrieves the entire string
print(mystring5[0::1] + " Hier")  # Outputs: 'i love python' - Retrieves the entire string with a step of 1
print(mystring5[::1])  # Outputs: 'i love python' - Retrieves the entire string with a step of 1
print(mystring5[::2])  # Outputs: 'ilv yhn' - Retrieves the string with a step of 2, skipping every other character
print(mystring5[::3])  # Outputs: 'io tn' - Retrieves the string with a step of 3, skipping every two characters
