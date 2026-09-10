# ordered, mutable collection
nums = [1,2,3,4,5,6,7,8]

nums.append(9)
print(nums)

print(nums.count(1))

nums.extend([10,11])
print(nums)

print(nums.index(8))
nums.pop()
print(nums)

nums.reverse()
# print(nums)

nums.remove(10)
# print(nums)

nums.sort()
# print(nums)

# nums.clear()
# print(nums)

# Slicing

print(nums[0: 2])
print(nums[:2])
print(nums[1:])
print(nums[::-1])

numbers = [ 1,2,3,4,5]

numbers.sort()
# Works on a list and modifies it.

new_nums = sorted(numbers)
# Returns a new sorted list.