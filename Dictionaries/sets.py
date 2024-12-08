# A set is an unordered collection of unique values
# No, sets in Python do not display data in sorted order. The elements in a set are stored in an unordered manner because sets are implemented using hash tables, which prioritize quick lookups over maintaining order.

# Sets are mutable—you can add and remove elements, but set elements must be immutable.

#A frozenset is an immutable set—it cannot be modified after you create it, so a set can contain FROZENSET as elements. The built-in function frozenset creates a frozenset from any iterable.

# Sets may contain only immutable objects, like strings, ints, floats and tuples that contain only immutable elements.

# Though sets are iterable, they are not sequences and do not support indexing and slicing with square brackets, []. 
# Dictionaries also do not support slicing.

# list= []
# tuple = ()
# dictionary = {key: values}
# set = {}
colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
# print(colors)
nums = {2,6,4,1,2,3}
# print(nums)

# print(len(nums))# 5

# CHECKING A VALUE IN A SET:

res = 2 in nums
# print(res)# True

res = 5 in nums
# print(res)# False

#ITERATION: 

# for color in colors:
    # print(color.upper(), end=' ')# ORANGE BLUE GREEN YELLOW RED 

#USING BUILT-IN FUNCTION:

list1 = [1,2,3,4,5,2,3,4,5,6,7]
set1 = set(list1)
# print(set1)# {1, 2, 3, 4, 6}

string = "to be or not to be that is the question"
# as the set is an unordered collection, so sorting it won't do any diff.

unique_words = set(string.split())
# for word in sorted(unique_words):
#     print(word, end=' ');

# SET COMPARISONS:
# print({1, 3, 5} == {3, 5, 1})# true
# print({1, 3, 5} != {3, 5, 1})# false


# The < operator tests whether the set to its left is a proper subset of the one to its right

# print({1, 3, 5} < {3, 5, 1})# False

# print({1, 3, 5} < {7, 3, 5, 1})# True

# The <= operator tests whether the set to its left is an improper subset of the one to its right

# print({1, 3, 5} <= {3, 5, 1})# true
# print({1, 3} <= {3, 5, 1})# true

# check for an improper subset with the set method issubset:
# print({1, 3, 5}.issubset({3, 5, 1}))# True 
# print({1, 2}.issubset({3, 5, 1}))# false


# similarly > , >= check for left is 
# The > operator tests whether the set to its left is a proper superset of the one to its right


# The >= operator tests whether the set to its left is an improper superset of the one to
# its right—

print({1, 3, 5}.issuperset({3, 5, 1}))# true
print({1, 3, 5}.issuperset({3, 2}))# false






















