

#difference()
a = {1, 2, 3, 4}
b = {1, 2, "Osama", "Ahmed"}
print(a)
print(a.difference(b)) # a-b
b = {1, 2, "Osama", "Ahmed",3 }
print(a.difference(b))
b = {1, 2, "Osama", "Ahmed",3,4 }
print(a.difference(b))
#########################
print("=" * 40) # seperator
c = {1, 2, 3, 4,5,6}
d = {1, 2, 3, 4, 5}
c.difference_update(d)
print(c)
#########################
print("=" * 40) # seperator
#intersection()
e = {1, 2, 3, 4,5,6,"e"}
f = {1, 2, 3, 4, 5, "x","e"}
print(e.intersection(f)) # e & f
print(e)