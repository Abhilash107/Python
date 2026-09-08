
import numpy as np
#array
ints = np.array([1,2,3,4,5])
mat = np.array([ [1,2,3,4,5], [6,7,8,9,10]])

floats = np.array([0.1, 0.2, 0.5, 0.6])# same type

# ndarray. faster than lists

# print(ints, floats)# [1 2 3 4 5] [0.1 0.2 0.5 0.6]
# print(type (ints))# <class 'numpy.ndarray'>
# print(type (mat))# <class 'numpy.ndarray'>

#DIMENSION:
# print(ints.ndim)# dimension 1

#ORDER:

# print(ints.shape)# (5,) column row 1
# print(mat.shape)#(2, 5)
# print(floats.shape)#(4,) column row 1

#SIZE:
#size-> integers’ size is the product of the shape tuple’s values
#itemsize -> itemsize is 8 because integers contains int64 values and floats contains float64 values, which each occupy 8 bytes.


# print(ints.size)# size of array 5
# print(ints.itemsize, "\n")# size of array 8(bytes)



# print(mat.size)# no. of elements 10
# print(mat.itemsize)# 8 :indicates that each element occupies 8 bytes of memory

#ITERATING THROUGH A MULTIDIMENSIONAL ARRAY'S ELEMENTS:

#This is an attribute of a NumPy array that returns an iterator over all the elements of the array, flattened into a 1D array.

for i in mat.flat:
    print(i, end = " ")#1 2 3 4 5 6 7 8 9 10




