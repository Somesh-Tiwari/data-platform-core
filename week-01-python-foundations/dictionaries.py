#Day 4 - Dictionaries

student = { 'name': 'Somesh', 'age': 20, 'courses': ['Big Data', ' AI', 'Data Science'] }
print(student)
print(student['name'])

print(student.get('phone', 'Not Found')) #if key is not found, return Not Found

student['phone'] = '555-5555'
print(student)

student.update({'name': 'John', 'age': 25, 'phone': '555-5555'})
print(student)

del student['age']
age = student.pop('age', 'Not Found') #if key is not found, return Not Found
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)