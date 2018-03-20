#Number operation

int1 = 1
long1 = 1L
float1 = 1.1
float2 = 32.54e-4
complex1 = 1 + 0.2j

print(int1)
print(long1)
print(float1)
print(float2)
print(complex1)

#String operation

str1 = "Hello World"
print(str1[0]) #H
print(str1[-3:])
print(str1[1:]) #ello World
print(str1[1:-1]) #ello Worl
print(str1[1:1]) #empty
print(str1*2) #Hello WorldHello World
print(str1+"Test") #Hello WorldTest


#List operation

list1 = ["abc", 1]
list2 = ["def", 2]

print(list1[0]) #abc
print(list1[1:]) #[1]
print(list1 + list2) #['abc', 1, 'def', 2]

list1[1] = 2
list1[0] = 1
print(list1)

#list[0] = 2 #TODO

#Tuple operation

tuple1 = ("abc", 1)
#tuple1[1] = 2
print(tuple1)

#Dictionary operation

dict1 = {}
dict1["one"] = "hello"
dict1["two"] = 2
print(dict1) #{'two': 2, 'one': 'hello'}
print(dict1.keys()) #['two', 'one']
print(dict1.values()) #[2, 'hello']

#If

var1 = "true";

if var1 == "true":
    print("This is true")
else:
    print("This is false")
print("This is end")

#While
count = 5;
while(count > 0 ):
    print("count: " + str(count));
    count-=1
else:
    print("This is end")

#for
#iterate element in a list
for element in list1:
    print(element)

#iterate element in a list by index
for index in range(len(list1)):
    print(index)
    print(list1[index])

#iterate all char  in a string
for char in "Hello":
    print(char)
else:
    print("This is end")

#Mathematic function
max(1, 2, 3)
min(-1, -2, -3)
abs(-3)
cmp(1, 2) #return  -1

#String operation
print("M" in "Hello")
if ("M" not in "Hello") == True:
    print(True)
else:
    print(False)


print("%s and %s" % ("Hello", "World"))

print("C:\\Disk") #C:\Disk
print(r"C:\\Disk") #C:\\Disk

print(max("abc"))
print("abc".title())

#list operation
list1 = ["opq", "abc", "xyz", "def"]
sortedList = sorted(list1)
print(sortedList) #['abc', 'def', 'opq', 'xyz']

#print(sorted(studentList, key = lambda student: student.age))

list2 = [12, 14, 11]
print(max(list2))

tuple1 = ("abc", "xyz")
print(tuple1)
#del tuple1[0]
print(tuple1)

dict1 = {"One":1, "Two":2}
dict2 = {"One":3, "Four":4}
dict1.update(dict2)
print(dict1)
print(dict1.get("Five"))
