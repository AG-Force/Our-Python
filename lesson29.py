# clear()
user = {
    "name": "Osama"
}
print(user)  # Print the initial 'user' dictionary
user.clear()  # Remove all key-value pairs from the 'user' dictionary
print("=" * 100)  # Print a line of 100 '=' characters
print(user)  # Print the 'user' dictionary after the clear() operation

# Update()
member = {
    "name": "Osama"
}
print(member)  # Print the initial 'member' dictionary
member["age"] = 36  # Add the key-value pair "age": 36 to the 'member' dictionary
print("=" * 100)  # Print a line of 100 '=' characters
print(member)  # Print the 'member' dictionary after adding the key-value pair
member.update({"country": "egypt"})  # Add the key-value pair "country": "egypt" to the 'member' dictionary
print(member)  # Print the 'member' dictionary after the update() operation

# copy()
main = {
    "name": "Osama"
}
print(main)  # Print the initial 'main' dictionary
b = main.copy()  # Create a shallow copy of the 'main' dictionary and assign it to 'b'
print(b)  # Print the 'b' dictionary (a copy of 'main')
main.update({"skills": "Fighing"})  # Add the key-value pair "skills": "Fighing" to the 'main' dictionary
print(main)  # Print the 'main' dictionary after the update() operation
print(b)  # Print the 'b' dictionary (it remains unchanged)

# keys() + values()
print(main.keys())  # Print a view object of all keys in the 'main' dictionary
print(main.values())  # Print a view object of all values in the 'main' dictionary
