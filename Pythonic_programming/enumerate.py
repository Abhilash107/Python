
#* enumerate()
# gives you both:

# index
# value

names = ["A", "B", "C"]

#normal
for i in range(len(names)):
    print(i, names[i])


#enumerate
for i, name in enumerate(names):
    print(i, name)

for i, name in enumerate(names,start=2):
    print(i, name)


#* zip()
#  combines element from multiple iterables

names = ["A", "B", "C"]
ages = [20, 21, 22]

result = zip(names, ages)
# print(result)# <zip object at 0x00000222DD81AEC0>
print(list(result))

for name , age in zip(names, ages):
    print(name , age)


#different length
a = [1, 2, 3]
b = ["a", "b"]

print(list(zip(a, b)))# [(1, 'a'), (2, 'b')]
# By default, zip() stops when the shortest iterable is exhausted.



#* any() ⭐⭐⭐
# Returns True if at least one element is truthy.

numbers = [False, False, True]

print(any(numbers))
# True


numbers = [1, 3, 5, 8]

print(any(x % 2 == 0 for x in numbers))

#* all()
# return true if every element is truthy

numbers = [1, 3, 5, 8]

print(all(x % 2 == 0 for x in numbers))# False

#* sorted()
# return a new sorted list


nums = [4,2,5,3,1]

result = sorted(nums)
print(nums, result)

# Key
# You can specify what should be used for sorting.
# Reverse sorting
result = sorted(nums, reverse=True)
print(result)

names = ['John', 'Bob', 'Alice']
print(sorted(names,key=len)) # ['Bob', 'John', 'Alice']

# using lambda
students = [
    ("A", 80),
    ("B", 95),
    ("C", 70)
]

print(sorted(students, key=lambda x: x[1]))


nums = [1,2,3,4]

#* reversed() ⭐⭐

# Returns an iterator that goes through a sequence in reverse order.
for x in reversed(nums):
    print(x)


#* min() / max()

print(min(nums))
print(max(nums))

#With key=
# Like sorted(), min() and max() can use a key.

print(max(names, key=len))

#* sum()

print(sum(nums)) # 10
# Starting value
sum(numbers, 10)# 10 + 10
