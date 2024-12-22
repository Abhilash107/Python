import numpy as np
nums = np.array([1,4,9,16,25])
res1 = (np.sqrt(nums))
#print(res1)

nums2 = np.arange(1, 6) * 10
#print(nums2)


res3 = np.add(nums, nums2)# shapes must be same
print(res3)

res4 = np.multiply(nums2, 5)
#print(res4)

nums3 = np.array([1,2,3,4,5,6])

res5 = nums3.reshape(2, 3)
#print(res5)

n1 = np.array([1,2,3])
n2 = np.array([1,2,3])


res6 = np.multiply(n1, n2)
#print(res6)

res7 = np.power(n1, 3)
#print(res7)


grades = np.array([[87, 96, 70], [100, 87, 90],
[94, 77, 90], [100, 81, 82]])

#print(grades)
#print(grades[0, 1])# row, col

#print(grades[1])#1st row
#print(grades[0:2])# sliced the 1st row to 2ns row

print()
#print(grades[[1, 3]])# selects the 2nd and 4th row

#print(grades[:, 0])# selects the 1st column

#print(grades[:, 1:3])# selects the 2nd and 3rd column

#print(grades[:, [0, 2]])#selects the 1st and 3rd column


#shallow copies
nums4 = np.arange(1, 6)

res9 = nums4.view()
print(res9)
print(nums4)
# The array method view returns a new array object with a view of the original array
# object’s data.
#Views are also known as shallow copies.

res9[1] *= 10
# print(res9)# shallow copies
# print(nums4)# shallow copies

#slice views
res9 = nums4[0:3]
# print(res9)
# print(nums4)

#deep copies
nums5 = np.array([1,2,3,4,5])

nums6 = nums5.copy()
nums5[0] = 10

print(nums5)
print(nums6)

# 7.13 to be continued






