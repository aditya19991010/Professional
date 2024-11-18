#Numpy
import sys

import numpy as np

y = np.empty((2,3))
print(y)


a = np.arange(10,30,5) #start:stop:step
print(a)
print(a.shape)

a = np.arange(0.10,1.0,0.3) #start:stop:step
print(a)

n = np.linspace(0,2,9) #create 9 numbers between 0 and 2
print(n)

a = np.arange(12).reshape(4,3)
print(a)

x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)
print(type(f))


#Printing 1D array
a =np.arange(6)

print(np.arange(100).reshape(5,20) )
np.set_printoptions(threshold=sys.maxsize)
# print(np.arange(10000).reshape(100,100) )

a = np.array([[1,1],
              [0,1]])
b = np.array([[2,0],
              [3,4]])

d = a@b
print(d)
c = a.dot(b)
print(c)

#
#inplace -changing the value of element in the matrix
rg = np.random.default_rng(1)
a= np.ones((2,3),int)
b= rg.random((2,3))
#seed = random number gets generates using seed. using same seed will generate same set of random numbers.
print(a)
a *= 3 #multiple each num of a matrix by 3
print(a)

a= rg.random((2,2))

print(a)
print(a.sum())
print(a.max())
print(a.min())
print(a.sum(axis=0)) #columnwise sum
print(a.sum(axis=1)) #rowwise sum

# all, any, apply_along_axism argmax, argmin, argsort, average, bincount,
# ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum,.....

#slicing
a =np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])

print(a[::-1]) #reverse the string





