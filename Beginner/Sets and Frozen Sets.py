#Set is an unordered collection of unique elements

numbers = [1, 2, 3,4 ,3,2, 4]
unique_numbers =  set (numbers)
print(unique_numbers)

unique_numbers.add(5)
print(unique_numbers)

fs = frozenset(numbers)
print(fs)
#fs.add(5)


x = {'a', 'b', 'c'}
y = {'a', 'd', 'g'}


print(x|y)
print(x&y)
print(x-y)
print(x > y)

x = {'a', 'd', 'g', 'h'}
print(x > y)