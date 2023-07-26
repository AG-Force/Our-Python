###############################lesson27 according youtube.  Lists###############################

# clear
a = {1, 2, 3}
a.clear()
print(a)

# union()
b = {"One", "Tow", "Three"}
c = {"1", "2", "3"}
x = {"One", "Cool"}
print(b | c)  # Prints the union of sets b and c
print(b.union(c, x))  # Prints the union of sets b, c, and x

# add()
d = {1, 2, 3, 4, 5}
d.add(5)  # Adds element 5 to set d
d.add(6)  # Adds element 6 to set d
print(d)

# copy()
e = {1, 2, 3}
f = e.copy()  # Creates a copy of set e and assigns it to f
print(e)
print(f)
e.add(6)  # Adds element 6 to set e
print(e)
print(f)  # The copy of set e (set f) remains unchanged
f = e.copy()  # Creates a new copy of set e and assigns it to f
print(f)

# remove()
g = {1, 2, 3, 4}
g.remove(1)  # Removes element 1 from set g
g.remove(4)  # Removes element 4 from set g
print(g)

# discard()
h = {1, 2, 3, 4}
h.discard(1)  # Removes element 1 from set h
h.discard(7)  # If element 7 exists in set h, removes it (no error if it doesn't exist)
print(h)

# pop()
i = {"A", True, "Hallo", 1, 2, 3}
print(i.pop())  # Removes and returns an arbitrary element from set i

# update()
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(k)  # Adds all elements from set k to set j
print(j)
j.update(["HTML", "CSS"])  # Adds the elements "HTML" and "CSS" to set j
print(j)
