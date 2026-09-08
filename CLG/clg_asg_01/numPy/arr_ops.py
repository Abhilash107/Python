import numpy as np

nums = np.arange(5)
print(nums)
print(nums * 2)
print(nums + 2)

# When one operand is a single value, called a scalar, NumPy performs the elementwise
# calculations as if the scalar were an array of the same shape as the other operand, but
# with the scalar value in all its elements. This is called broadcasting.
print(nums * [1,1,1,1,1])

nums2 = np.linspace(1.1, 5.5, 5)
print(nums2 * nums)

print(nums > 3)
print(nums < nums2)

print(nums.sum())
print(nums.min())
print(nums.max())
print(nums.mean())
print(nums.std())
print(nums.var())
