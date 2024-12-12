import numpy as np

ints = np.array([1,2,3,4,5])
mat = np.array([ [1,2,3,4,5], [6,7,8,9,10]])

floats = np.array([0.1, 0.2, 0.5, 0.6])# same type

# print(ints, floats)
# print(type (ints))
# print(type (mat))

print(ints.ndim)# dimension
# print(ints.shape)
print(mat.shape)

# print(ints.size)# size of array
# print(ints.itemsize, "\n")# size of array



# print(mat.size)# no. of elements
# print(mat.itemsize)# 8 :indicates that each element occupies 8 bytes of memory


#This is an attribute of a NumPy array that returns an iterator over all the elements of the array, flattened into a 1D array.
for i in ints.flat:
    print(i, end = " ")




