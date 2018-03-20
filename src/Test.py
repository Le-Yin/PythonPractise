#!/usr/bin/python

print("This line will be printed!")

x = 1
if x == 1:
    #indented four spaces
    print("x is 1")

del x



myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

hello = "hello"
world = "world"
one = 1
helloworld = hello + world + str(one)
print(helloworld)


a, b = 3, 4
print(a, b)

mystring = "hello"
myfloat = 10.0
myint = 20

print("%f and %d" % (myfloat, myint))

mylist = [2, 3]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

print(mylist.count(2))

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3 * 2
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

lotsofhello = "hello" * 10
print(lotsofhello)





even_number = [2,4,6,8]
odd_number = [1,3,5,7]
all_numbers = even_number + odd_number
all_numbers.sort()  # modify original lists in place
print(all_numbers)
all_number_new = sorted(all_numbers) # return a new lists
print(all_number_new)
