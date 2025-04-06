def linear_search(arr, key):
    for i in range (len(arr)):
        if key == arr[i]:
            return i
    return -1

a = [1,2,3,4,5]
res = linear_search(a, 2)
# print(res)

import numpy as np

# values = np.random.randint(1, 10, 10)
# Implementing on numpy Array
values = np.array([1,2,3,4,5,6])

ind = linear_search(values, 7)
print(ind)