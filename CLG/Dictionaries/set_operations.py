#Union (adds)
# The union of two sets is a set consisting of all the unique elements from both sets. You can
# calculate the union with the | operator or with the set type’s union method:

# When a mathematical
# set method receives a non-set iterable argument, it first converts the iterable to a
# set, then applies the mathematical operation. Again, though the new sets’ string representations
# show the values in ascending order, you should not write code that depends on this.

#print({1, 3, 5} | {2, 3, 4})
#print({1, 3, 5}.union([20, 20, 3, 40, 40]))

#INTERSECTION:(common)
# print({1, 3, 5} & {2, 3, 4})
# print({1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4]))

#DIFFERENCE:
# The difference between two sets is a set consisting of the elements in the left operand that
# are not in the right operand. You can calculate the difference with the - operator or with
# the set type’s difference method:

# print({1, 3, 5} - {2, 3, 4})
# print({1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4]))

# Symmetric Difference:

# The symmetric difference between two sets is a set consisting of the elements of both sets
# that are not in common with one another. You can calculate the symmetric difference with
# the ^ operator or with the set type’s symmetric_difference method:

#print({1, 3, 5} ^ {2, 3, 4})
# print({1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4]))

# Disjoint:
# Two sets are disjoint if they do not have any common elements. You can determine this with the set type’s isdisjoint method:

print({1, 3, 5}.isdisjoint({2, 4, 6}))
print({1, 3, 5}.isdisjoint({4, 6, 1}))