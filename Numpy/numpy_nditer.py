import numpy as np

a = np.arange(12).reshape(3,4)
for row in a:
    print(row)

for row in a:
    for cell in row:
        print(cell)

for cell in a.flatten():
    print(cell)
print('-' * 30)

a = np.arange(12).reshape(3,4)
for x in np.nditer(a, order='C'):
    print(x)
for x in np.nditer(a, order='F'):
    print(x)

for x in np.nditer(a, order='F',flags=['external_loop']):
    print(x)

print('-' * 30)

a = np.arange(12).reshape(3,4)
for x in np.nditer(a,op_flags=['readwrite']):
    x[...] = x*x
print(a)
b = np.arange(3,15,4).reshape(3,1)
for x,y in np.nditer([a,b]):
    print(x,y)