def myFirstFunction():
    "Doc string for nothing"
    return;


myFirstFunction()


def addMoreElement(listVar):
    listVar.append(1)
    print(listVar)

myList = [4,3,2]
addMoreElement(myList)


def printInfo(age, name):
    print("Age %d, Name %s" %(age, name))


printInfo(name = "Lele", age = 18)


def printInfo(age, name, nationality="China"):
     print("Age %d, Name %s, Nationality %s" %(age, name, nationality))

printInfo(name = "Lele", age = 18)



def printInfo(name, *varTuple):
    print(name)
    for element in varTuple:
        print(element)


printInfo("Lele", 18, "China")

sum = lambda var1, var2: var1+var2

print(sum(10,20))

def returnThings(type):
    if type=="Number":
        return 1
    else:
        return "Hello"

print(returnThings("String"))
