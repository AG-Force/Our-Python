###############################lesson21 according youtube.  Lists###############################

myAwesomelist = ["One","Two","One",1,100.5,True,False]
print(myAwesomelist)

print(myAwesomelist[0])

print(myAwesomelist[-1])

print(myAwesomelist[1:4])

print(type(myAwesomelist[1]))

print(myAwesomelist[1:])

print(myAwesomelist[::2])

print(myAwesomelist[::1])

print(myAwesomelist[1::])
###########################################################################
myAwesomelist[1] = 2
print(myAwesomelist)
###########################################################################
myAwesomelist[0:2] = 5,4
print(myAwesomelist)
###########################################################################
myAwesomelist[0:2] = "e","df"
print(myAwesomelist)
###########################################################################
myAwesomelist[0:2] = ["e","df"]
print(myAwesomelist)




