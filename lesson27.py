################################################################ issuperset()
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # It checks if all elements of b are in a
print(a.issuperset(c))  # It checks if all elements of c are in a
################################################################issubset()
print("=" * 100)
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}
print(d.issubset(e))  # It checks if all elements of d are in e
print(d.issubset(f))  # It checks if all elements of d are in f
print("=" * 100)

################################################################isdisjoint()
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}
print(g.isdisjoint(h))  # It checks if g and h have no common elements
print(g.isdisjoint(i))  # It checks if g and i have no common elements
