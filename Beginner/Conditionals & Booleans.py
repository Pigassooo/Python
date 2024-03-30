language = 'Python'

if language == 'Python':
    print('language is Python')
elif language =='java':
    print('language is java')
else:
    print('No match')


logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(id(a))
print(id(b))
print(a is b)
print(c is a)