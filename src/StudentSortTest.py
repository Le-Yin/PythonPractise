from Student import Student

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(student_objects[0])

print(sorted(student_objects, key = lambda student: student.age))
print(sorted(student_objects, key = lambda student: student.grade))
print(sorted(student_objects, key = lambda student: student.weighted_grade()))
print(dir(Student))
print(help(Student.weighted_grade))
