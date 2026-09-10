
# for i in [1,2,3,4]:
#     print(i)


# for i in range(6):
#     print(i)#0,1,2,3,4,5


# # range(start, stop, step)

# for i in range(100, 121, 2):
#     print(i)

# for i in range(140, 119, -2):
#     print(i,end=" ")

# print("\n")
# for c in 'Python':
#     print(c)



i = 1

while i <= 5:
    print(i)
    i += 1

# while True:
#     print('o')

# & break
i = 0
while i <= 5:
    if(i == 3):
        break
    print(i)
    i += 1

# & continue
i = 0
for i in range(10):
    if(i == 5):
        continue
    print(i)


if 2 > 1:
    pass
