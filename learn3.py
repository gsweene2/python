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

testString = "I took my dog for a walk in the park"
indexE = testString.index("p")
print("The first occurance of the letter 'p' in the string, %s , is the character at index %s!" % (testString, indexE))

number1 = 7
number2 = 9

if number1 < number2 and number1 > 0:
    #print("%s is between 0 and %s" (number1, number2))
    print("The statement is true")
else:
    print("the statement is false")

# Functions

def garretts_first_function():
    print("This is garrett's first function. It has no parameters!")

# How to call a function    
garretts_first_function()

def garretts_first_function_with_paramss(parameter1, parameter2):
    print("This is garrett's second function. It has 2 parameters, %s and %s!" % (parameter1, parameter2))

garretts_first_function_with_paramss("yay","hooray")