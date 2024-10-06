a = 0
b = 0
c = 0

i = 1
while(i > 0):
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))
    c = int(input("Enter third num: "))
    i = i-1

max_num = a

if b > max_num:
    max_num = b;

if c > max_num:
    max_num = c;

print(f"Max num is: {max_num}")

# Another way to add comments to code
"""print(f"Max num is: {max_num}")"""

print(" i am",
      " a god")

# Chaining comparisons
value = 1 <= 2<= 5
print(f"value, {value}")


print(5 < 9, 5 <= 9, 5 > 9, 5 >= 9, 5 == 9, 5 != 9)

#Dynamic typing
x = 10
print(type(x))
x = 19.8
print(type(x))

