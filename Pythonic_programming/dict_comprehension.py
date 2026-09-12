nums = [1,2,3,4,5,6,7,8,9]

squares = {}

#normal approach
for x in nums:
    squares[x] = x * x

print(squares)

squares = {x: x * x for x in nums}
print(squares)

# {key: value for item in iterable condition}
res = {x: x*x for x in nums if x %2 == 0}
print(res)


res = {x: x*x for x in nums if x %2 == 0}
print(res)

