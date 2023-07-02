###############################lesson23 according youtube.  Lists###############################
##########clear()##########
a = [1, 2, 3, 4, 5,0,7,8,9,6]
a.clear()
print(a)
##########copy()##########
a2 = [1, 2, 3, 4, 0,7,8,9,6]
b = a2.copy()
print(a2)
print(b)
b.append(5)
print(b)
print(a2)
##########count()##########
a3 = [1, 2, 3, 4, 0,7,8,9,6,1,1,1,1]
print(a3.count(1))
##########index()##########
a4 = ["Ghassan", "Ahmed", "Zakaria", "Osman"]
print(a4.index("Ghassan"))
##########insert()##########
a5 = [1, 2, 3, 4, 0,7,8,9,6]
a5.insert(0,"Test")
print(a5)
a5.insert(-1,"nein man")
print(a5)
a5.insert(10,"Ja man")
print(a5)
##########pop()##########
a6 = [1, 2, 3, 4, 0,7,8,9,6]
print(a6.pop(2))
print(a6.pop(-1))




