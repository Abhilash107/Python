nums = [1,2,3,4,5,6,7,8,9]

squares = []

# normal approach
for x in nums:
    squares.append(x*x)

print(squares)

#list comprehension
squares = [x * x for x in nums]
print(squares)

# Format ==> [expression for item in iterable]
# [expression for item in iterable if condition]
#^ if-else before for:


even = [x for x in nums if x%2 == 0]
squares_of_even = [x * x for x in nums if x%2 == 0]

print(even, squares_of_even)

res = ['even' if x % 2 == 0 else 'odd' for x in nums]
print(res)
