print("Today I'll be learning python!")

# I can use variables without declaring them
undeclared = 2018
print(undeclared)

# I can define strings in multiple ways
stringVar = 'my string variable'
stringVar2 = "my other string variable"
print(stringVar)
print(stringVar2)

# Holy, you can assign mult vars on one line!
var1, var2 = "hello", "3"
print("var1: " + var1)
print("var2: " + var2)

# You can make a list out of all these vars and iterate through them!
print()
print()
print("Proceeding to print a list")
newList = []
newList.append(undeclared)
newList.append(stringVar)
newList.append(stringVar2)
newList.append(var1)
newList.append(var2)

for x in newList:
    print(x)

# I can get the length of a list
lengthList = len(newList)
print("The length of the list is %s objects" % lengthList)

thisIndex = 2
thirdObjectLength = len(newList[thisIndex])
print("The length of the object at index %s is %s characters" % (thisIndex, thirdObjectLength))