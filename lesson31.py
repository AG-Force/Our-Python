name = ""  # Initialize the variable 'name' as an empty string

print(name.isspace())  # Check if 'name' consists of only whitespace characters and print the result
print("=" * 100)  # Print a line of 100 '=' characters
print(100 > 200)  # Compare 100 with 200 and print the result
print("=" * 100)  # Print a line of 100 '=' characters

# True values
print(bool("Osama"))  # Check if the string "Osama" is non-empty and print the result
print(bool(100))  # Check if the integer 100 is non-zero and print the result
print(bool(100.95))  # Check if the float 100.95 is non-zero and print the result
print(bool(True))  # Check if the boolean value True is True and print the result
print(bool(False))  # Check if the boolean value False is True and print the result
print(bool([1, 2, 3, 4, 5]))  # Check if the list [1, 2, 3, 4, 5] is non-empty and print the result

# False values
print(bool(0))  # Check if the integer 0 is non-zero and print the result
print(bool(''))  # Check if the empty string is non-empty and print the result
print(bool(""))  # Check if the empty string is non-empty and print the result
print(bool([]))  # Check if the empty list is non-empty and print the result
print(bool({}))  # Check if the empty dictionary is non-empty and print the result
print(bool(False))  # Check if the boolean value False is True and print the result
print(bool(()))  # Check if the empty tuple is non-empty and print the result
print(bool(None))  # Check if the None value is True and print the result
