#numpy - N-dimentional array or nd array
# numpy.org and pandas.org

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a  = np.arange(15)
print(a)
a = a.reshape(3,5)
print(a)
print(a.size)
print(a.itemsize)

a = np.array([2,3,5])
print(a.dtype)

b = np.array([(1.5,2,3),(4,5,9)])
print(b.dtype)

# a = np.array(1,5,4,7,9) #Wrong

#for initiating a matrix
z = np.zeros((3,4))
print(z)

x = np.ones((2,4,2), dtype = np.int64)
print(x.ndim)



