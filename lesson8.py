#concatantion
msg = "i love "
lang = "Python"

# Concatenates 'msg' and 'lang' using the '+' operator
print(msg + lang)  # Output: "i love Python"

#########################

msg2 = "i love"
lang2 = "Python"

# Concatenates 'msg2', a space, and 'lang2' using the '+' operator
print(msg2 +" "+ lang2)  # Output: "i love Python"

#########################

full = msg2 + " " + lang2

# Concatenates 'msg2', a space, and 'lang2', and assigns the result to the variable 'full'
print(" "+full)  # Output: " i love Python"

#########################

a = "First \
second \
third \
"
b = "a \
b \
c \
"

# Concatenates 'a' and 'b' and prints the result
print(a+b)  # Output: "First second third a b c "

# Concatenates 'a', a line break, and 'b', and prints the result
print(a+ "\n" +b)  # Output:
# "First 
# second 
# third 
# a b c "

# Prints the text "Hello" and a line break, followed by "World"
print("Hello \n World")  # Output:
# "Hello 
# World"
