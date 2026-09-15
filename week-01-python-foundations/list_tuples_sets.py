#Day 3

#Lists
courses = ['History', 'Math', 'English', 'Geography', 'Science']
print(courses)
print(courses[2:-1])
print(courses[0:5:3])

courses.append('Art')
print(courses)
courses.insert(0, 'Music')
print(courses)
courses.extend(['PE', 'Drama'])
print(courses)

courses.remove('Math')
courses.pop()
print(courses)

sorted_courses = sorted(courses)
print(sorted_courses)
courses.reverse()
print(courses)

print(courses.index('English'))
print('Math' in courses)

for index, course in enumerate(courses, start=1):
    print(index, course)

#proble with mutable lists
list1 = ['History', 'Math', 'English', 'Geography', 'Science']  
list2 = list1
#but we could do
list3 = list1.copy()
#then we can update the values in list1 without the changing the values of list3

#empty list
empty_list = []


#Tuples
tuple1 = ('Somesh', 'John', 'Jane'
)
tuple2 = (55, 'Smith', 'Johnson')
print(tuple1)
tuple3 = tuple1 + tuple2
print(tuple3)
#empty tuple
empty_tuple = ()



#Sets
school_courses = {'History', 'Math', 'English', 'Geography', 'Science'}
college_courses = {'Math', 'English', 'Art', 'Drama'}
print(school_courses.intersection(college_courses)) #common
print(school_courses.difference(college_courses))   #what is in school but not in college
print(school_courses.union(college_courses))    #combine all
#empty set
empty_set = set()
