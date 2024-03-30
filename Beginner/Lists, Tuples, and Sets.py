courses = ['history', 'math', 'physics']
courses_2 = ['Chinese', 'Japanese']

print(courses)
print(len(courses))
print(courses[2])
print(courses[-1])
print(courses[1:3])

courses.append('art')
print(courses)
courses.insert(0, 'Art')
print(courses)

courses.insert(0, courses_2)
print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('math')
print(courses)

poped = courses.pop()
print(courses)
print(poped)

courses.reverse()
print(courses)

nums = [1, 5, 3, 2, 6]
nums.sort()
print(nums)

nums.sort(reverse=1)
print(nums)

sorted_nums = sorted(nums)
print(sorted_nums)

print(max(nums), sum(nums))

print(courses.index('history'))
print('art' in courses)

for item in courses:
    print(item)

for index, item in enumerate(courses, start=1):
    print(index, item)

course_str = ' + '.join(courses)
print(course_str)

new_list = course_str.split(' + ')



# Tuples remain stable
# Sets