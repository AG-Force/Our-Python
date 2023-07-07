# setdefault()
user = {
    "name": "Osama"
}
print(user)  # Print the initial 'user' dictionary
print(user.setdefault("name", "Ahmed"))  # Get the value for the key "name" (which exists) and print it
print(user)  # Print the 'user' dictionary after the setdefault() operation
print(user.setdefault("age", 22))  # Get the value for the key "age" (which doesn't exist) and print the default value
print(user)  # Print the 'user' dictionary after the setdefault() operation
print("=" * 100)  # Print a line of 100 '=' characters

# popitem()
member = {
    "name": "Osama",
    "skill": "ps4"
}
member.update({"age": 22})  # Add the key-value pair "age": 22 to the 'member' dictionary
print(member)  # Print the 'member' dictionary
print(member.popitem())  # Remove and return an arbitrary key-value pair from the 'member' dictionary and print it
print("=" * 100)  # Print a line of 100 '=' characters

# items()
view = {
    "name": "Osama",
    "skill": "XBox"
}
allItems = view.items()  # Get a view object of all key-value pairs in the 'view' dictionary
print(view)  # Print the 'view' dictionary
view["age"] = 22  # Add the key-value pair "age": 22 to the 'view' dictionary
print(allItems)  # Print the previously created view object (it should reflect the changes in the 'view' dictionary)
print("=" * 100)  # Print a line of 100 '=' characters

# fromkeys()
a = ('Mykeyone', 'Mykeytow', 'Mykeythree')
b = "X"
print(dict.fromkeys(a, b))  # Create a new dictionary using the keys from 'a' and the value 'b' and print it
