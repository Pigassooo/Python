import numpy as np
import random

random.seed(100)
print(random.random())
print(random.random())
print(random.random())
print('-'*30)

a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print('-'*30)

a = np.arange(30).reshape(2,15)
print(a)
print(np.hsplit(a,3))
print(np.vsplit(a,2))
print('-'*30)

a = np.arange(12).reshape(3,4)
b = a > 4
print(b)
print('-'*30)
