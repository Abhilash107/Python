# var name can't start with number, can't contain any space
variable_1 = 2
#print(variable_1)

# input => display and take input from user
# print > only display 

str = '123'
#print(int(str))


#a = int(input("Enter a: "))
# a = 20
# b = 10
#print(a+b)  # 30

# c = 'nana '
# d = 8
# e = c * d
#print(e, "batman")


#x = int(input("Enter a number: "))
#equation = pow(x,3) + 2 * pow(x,2) + 3 * x + 4

#print(equation)

# r = int(input("Enter a number: "))
# print(3.14 * pow(r, 2))
# print(4/3 * pow(r, 3))


# a = float(input("Enter a Number: "))
# b = float(input("Enter a Number: "))
# c = float(input("Enter a Number: "))

# if a<b | (c!=b) & (c<a):
#     print("Yes")
# else:
#     print("No")


p = 1000
r = 12 / 100
n = [10, 20, 30]

for years in n:
    a = p * pow((1 + r), years)
    print(f"Amount after {years} years: {a:.2f}")








