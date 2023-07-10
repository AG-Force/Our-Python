# Boolean operators

age = 26  # Assigning a value of 26 to the variable 'age'
country = "Egypt"  # Assigning the string "Egypt" to the variable 'country'
rank = 10  # Assigning a value of 10 to the variable 'rank'

# Checking if age is greater than 16
print(age > 16)  # Output: True

# Checking if country is equal to "Egypt"
print(country == "Egypt")  # Output: True

print("-" * 50)  # Printing a line of dashes for visual separation

# Checking multiple conditions using 'and' operator
print(age > 16 and country == "Egypt" and rank > 0)  # Output: True
print(age > 16 and country == "Egypt" and rank == 0)  # Output: False

print("-" * 50)  # Printing a line of dashes for visual separation

# Checking multiple conditions using 'or' and 'and' operators
print(age > 16 or country == "Egypt" and rank > 0)  # Output: True
print(age > 40 and country == "KSA" or rank > 20)  # Output: False
print(age > 40 or country == "Egypt" or rank > 20)  # Output: True

# Negating a condition using 'not' operator
print(not age > 16)  # Output: False

print("-" * 50)  # Printing a line of dashes for visual separation
