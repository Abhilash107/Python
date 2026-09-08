import numpy as np

zeros = np.zeros(5)#[0. 0. 0. 0. 0.]
ones = np.ones(5)#[1. 1. 1. 1. 1.]


#Creating arrays from Ranges:

ints = np.arange(9)#[0 1 2 3 4 5 6 7 8]
#ints = np.arange(4,10)#[4 5 6 7 8 9]
#ints = np.arange(10, 1, -1)#[10  9  8  7  6  5  4  3  2]


#print(zeros, ones, ints)


arr = np.linspace(0.0, 1.0, 10)
print(arr)

arr2 = np.arange(1, 21).reshape(5, 4)
print(arr2)