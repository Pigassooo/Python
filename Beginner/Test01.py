odd_nums =[]
x = int(input("plz in put:"))
for i in range(1,x):
    if i % 2 == 1:
        odd_nums.append(i)

print(odd_nums)