# operators and methods that modify an existing set

# |, union augmented assignment |=
nums = {1, 3, 5}
nums |= {2, 3, 5}
# print(nums) 1 2 3 5

# the set type’s update method performs a union operation modifying the set on which it's called—the argument

nums.update(range(8))
# print(nums)# {0, 1, 2, 3, 4, 5, 6, 7}

# The other mutable set methods are:
# -> intersection augmented assignment &=
# -> difference augmented assignment -=
# -> symmetric difference augmented assignment ^=
# and their corresponding methods with iterable arguments are:
# -> intersection_update
# -> difference_update
# -> symmetric_difference_update

# Methods for Adding and Removing Elements:

# Set method add inserts its argument if the argument is not already in the set; otherwise, the set remains unchanged:
nums.add(10)
# print(nums)# {0, 1, 2, 3, 4, 5, 6, 7, 10}
nums.remove(10)
# print(nums)# {0, 1, 2, 3, 4, 5, 6, 7}
#nums.remove(11)# causes an exception if the value is not in the set.
# print(nums)
# Traceback (most recent call last):
#   File "e:\Languages\Python\Dictionaries\muatble_set_operations.py", line 29, in <module>
#     nums.remove(11)
# KeyError: 11

# where as,
nums.discard(11)# does not cause an exception
# print(nums)# {0, 1, 2, 3, 4, 5, 6, 7}

popped_val = nums.pop()
 #Set method pop returns the first element added to the set.
 #Answer: False. Set method pop returns an arbitrary set element.
# print(popped_val)# 0
# print(nums)# {1, 2, 3, 4, 5, 6, 7}


nums.clear()# method clear empties the set
# print(nums)# set()

evens = {i for i in range(1, 21) if i % 2 == 0}
print(evens)







