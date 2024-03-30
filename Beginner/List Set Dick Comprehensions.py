numbers = [1, 2, 3, 4, 5, 6, 7]
even =[]

for i in numbers:
    if i % 2 == 0:
        even.append(i)

print(even)


even = [i for i in numbers if i % 2 == 0]

print(even)

sqr_num = [2, 4, 2, 5, 1]

s = set(sqr_num)
print(s)


cities = ["1", '2', '3']
countries = ['A', 'B', 'C']

z = zip(cities, countries)
for a in z:
    print(a)


d = {city:country for city, country in zip(cities, countries)}
print(d)