student = {'name' : 'John', 'age' : 25, 'courses' : ['Math', 'CompSci']}

print(student)

poped = student.pop('age')
print(poped)

print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)