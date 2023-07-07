# Dictionary
user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["HTML", "CSS", "JS"],
    "rating": 10.5
}
print(user)  # Print the 'user' dictionary
print("=" * 100)  # Print a line of 100 '=' characters
print(user['country'])  # Print the value associated with the key 'country' using indexing
print(user.get("country"))  # Print the value associated with the key 'country' using the get() method
print("=" * 100)  # Print a line of 100 '=' characters
print(user.keys())  # Print a view object of all keys in the 'user' dictionary
print(user.values())  # Print a view object of all values in the 'user' dictionary
print("=" * 100)  # Print a line of 100 '=' characters

# Two-Dimensional dictionary
languages = {
    "one": {
        "name": "HTML",
        "progress": "80%"
    },
    "Tow": {
        "name": "CSS",
        "progress": "90%"
    },
    "Three": {
        "name": "JS",
        "progress": "100%"
    }
}

print(languages)  # Print the 'languages' dictionary
print("=" * 100)  # Print a line of 100 '=' characters
print(languages["one"]['progress'])  # Print the value associated with the key 'progress' in the nested dictionary with key 'one'
print(languages["one"]['name'])  # Print the value associated with the key 'name' in the nested dictionary with key 'one'
print("=" * 100)  # Print a line of 100 '=' characters

# Dictionary length
print(len(languages))  # Print the number of key-value pairs in the 'languages' dictionary
print(len(languages["Tow"]))  # Print the number of key-value pairs in the nested dictionary with key 'Tow'
print("=" * 100)  # Print a line of 100 '=' characters

# Create dictionary from variable
frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
}
frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}
frameworkThree = {
    "name": "Angular",
    "progress": "80%"
}

allFrameworks = {
    "One": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree
}

print(allFrameworks)  # Print the 'allFrameworks' dictionary
