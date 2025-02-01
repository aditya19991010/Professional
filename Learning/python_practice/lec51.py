#Shape manipulation operations
# Func - Ravel, Reshape, resize, column stack, vstack, hstack, hspilt
from os import PRIO_PGRP

import numpy as np
from numpy.ma.extras import column_stack

#intialize the seed
rg = np.random.default_rng(789)

# ravel - flatten the array, use to convert a matrix into vector or vectors
a = np.floor(10*rg.random((3,4)))
print(a)

print(a.shape)
#converting array a into a flattened
print(a.ravel())

print(a.T) #Transposing
print(a.T.shape)

print(a)
a.resize((2,6))
print(a.shape)


a = np.floor(10*rg.random((2,2)))
b = np.floor(10*rg.random((2,2)))

print(a)
print(b)
print(np.vstack((a,b))) # stacked two matrices vertically
print(np.vstack((b,a)))

print("hstack\n",np.hstack((a,b))) # stacked two matrices horizontally
print("hstack\n",np.hstack((b,a)))

from numpy import newaxis

c = np.column_stack((a,b))
print(c)
a = np.array([4., 2.])
b = np.array([3., 8.])

c = np.column_stack((a,b))
print(c)


#splitting a list
a = np.floor(10*rg.random((2,12)))
print(a)
h = np.hsplit(a,3)
print(h)


import pandas as pd

df = pd.DataFrame(
    {
        "Name":[
            "Braud,Mr Owen",
            "Allen, Mr William",
            "Bonnell, Miss Elizabeth"
        ],
        "Age":[22,33,44],
        "Pincode":[58742,78742,98742],
        "Sex":["M", "M","F"]
    }
)

print(df)
print(df.shape)
