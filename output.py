# a = 20
# def f():
#     a = 10
#     b = 10
#     def g():
#         nonlocal b
#         b = b + 2
#         print(b)
#     g()
#     print(a, b)
# f()
# print(a)

# s = "abc"
# for i in range (len(s)):
#     str = s[i:] + s[:i]
#     print(str)

# import re
# res = re.findall(r'[a-zA-Z]+ing', 'walking down and think and smiling')
# print(res)

# l = [1,2,3,3,4,4]
# # iterate backwards
# for i in range (len(l) -1, -1, -1):
#     if l.count(l[i]) > 1:
#         l.remove(l[i])

# print(l)

tup1 = (1,2,3,4)
tup2 = (2,3,4)

tup3 = [ i+j for i, j in zip(tup1, tup2) ]
res = list(zip(tup1, tup2))
print(res)
print(tup3)



