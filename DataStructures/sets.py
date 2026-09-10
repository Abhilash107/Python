
# A set is an unordered collection of unique elements.
# Hence no indexing 
nums = {1, 2, 3, 4}


# print(nums)

A = {1, 2, 3}
B = {3, 4, 5}
# union -> |
# intersection -> &
# Difference -> -
# Symmetric diff -> ^

print(A | B)
print(A & B)

print(A - B)

print(A ^ B)

print(A | B)

A.add(10)

A.remove(10)


# A.remove(10)
# Raises an error if the element doesn't exist.

# A.discard(10)
# Doesn't raise an error if the element doesn't exist.

A.clear()


# Membership

if 3 in nums:
    print("Yes")