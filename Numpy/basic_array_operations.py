import numpy as np
import random

a = np.array([5, 6, 9])
print(a[0], a[1])

a = np.array([[1,2,3], [3,4 ,5], [5,6,7], [7,8,9]])
print(a[1])
print(a.ndim)
print(a.itemsize)
print(a.dtype)

a = np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a)
print(a.shape)

a = np.array([[1,2],[3,4],[5,6]], dtype=complex)
print(a)

a = np.zeros((3,4))
print(a)

a = np.arange(1,5,2)
print(a)

l = np.linspace(1, 5 ,10)
print(l)

a = np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)
print(a.T)
print('-'*30)
print(a.transpose())

print(a.reshape(2,3))
print(a.ravel())
print('-'*30)

a = np.array([[1,2],[3,4],[5,6]])
print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

b = np.sqrt(a)
print(b)
print(np.std(a))
print('-'*30)


