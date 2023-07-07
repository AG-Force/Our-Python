###############################lesson22 according youtube.  Lists###############################
##################################### append()

Myfriends = ["Gassan", "Ahmed", "Zakaria"]
Myoldfriends = ["d", "s", "u"]
print(Myfriends)
Myfriends.append("Abdul")
print(Myfriends)
Myfriends.append(343434)
print(Myfriends)
Myfriends.append(Myoldfriends)
print(Myfriends)
print(Myfriends[5][1])
##################################### extend()
a = [1, 2, 3, 4, 5]
b = ["A", "B", "C"]
c = ["Test"]
a.extend(b)
a.extend(c)
print(a)
##################################### remove()
a2 = [1, 2, 3, 4, 5, "Test", True]
a2.remove("Test")
print(a2)
##################################### sort()
a3 = [1, 2, 3, 4, 5,0,7,8,9,6]
a3.sort()
print(a3)
a3.sort(reverse=True)
print(a3)
a4 = ["Z","B","A"]
a3.sort(reverse=True)
print(a4)

##################################### reverse()
a5 = [1, 2, 3, 4, 5,0,7,8,9,6,True,False,"Gassan"]
a5.reverse()
print(a5)








