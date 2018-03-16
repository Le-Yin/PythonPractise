#from com.Student import *
from com.le.yin.test.Student import Student
student_objects = [
    com.Student.Student('john', 'A', 15),
    com.Student.Student('jane', 'B', 12),
    com.Student.Student('dave', 'B', 10),
]

print(student_objects[0])

print(sorted(student_objects, key = lambda student: student.age))
print(sorted(student_objects, key = lambda student: student.grade))
print(sorted(student_objects, key = lambda student: student.weighted_grade()))
print(dir(com.Student.Student))
print(help(com.Student.Student.weighted_grade))
