###############################lesson27 according youtube.  Lists###############################

#clear
a = {1,2,3}
a.clear()
print(a)

#union()

b = {"One", "Tow", "Three"}
c = {"1","2","3"}
x = {"One", "Cool"}
print(b | c)
print(b.union(c, x))
#add()
d = {1,2,3,4,5}
d.add(5)
d.add(6)
print(d)
#copy()
e = {1,2,3}
f = e.copy()
print(e)
print(f)
e.add(6)
print(e)
print(f)
f = e.copy()
print(f)
#remove()
g = {1,2,3, 4}
g.remove(1)
g.remove(4)
print(g)
#discard()
H = {1,2,3, 4}
H.discard(1)
H.discard(7)
print(H)
#pop()
i = {"A",True, "Hallo",1,2,3}
print(i.pop())
#update()
j = {1,2,3}
k = {1, "A", "B", 2}
j.update(k)
print(j)
j.update(["HTMl", "CSS"])
print(j)
