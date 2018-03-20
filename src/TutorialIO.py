#input = raw_input("Please input something: ")
#print(input)

#input = input("Please input something: ")
#print(input)

import os

testFile = open("test_file.dat")
print(testFile.name)
print(os.path.getsize("test_file.dat"))#12 bytes
print(os.path.abspath("test_file.dat"))
testFile.close()


testFile = open("test_file.dat")

wholeStr = testFile.read()
print(wholeStr)
testFile.close()

testFile = open("test_file.dat")

for str in testFile.readlines():
    print(str)
testFile.close()


testFile = open("test_file.dat","ab") #append mode
testFile.write("Really?")
testFile.close()

testFile = open("test_file_2.dat","ab")
data = ["Line1", "Line2", "Line3"]
for item in data:
    testFile.writelines(item+"\n")
testFile.close()

os.rename("test_file_2.dat", "test_file_renamed.dat")

print(os.path.abspath(os.curdir)) #/Users/chelseayin/Develop/Test/PythonPractise/src
os.chdir()
