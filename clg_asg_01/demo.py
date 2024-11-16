#print("Hello \nWorld ")#
#print("Hello \tWorld ")

#name = input("Enter your name: ")
#print(f"Hello {name}, User no: ",2020392993 + 1 )

#print('int(5.2)', 'truncates 5.2 to', int(5.2))
#print(''' a  b 'd'  "Abc" ''')

#print(type(name))
# default type of any input from console is STRING
# so use type casting

# print("hehehe \\abhi ")
# for _ in range(1): 
#     a = int(input("Enter first num: "))
#     b = int(input("Enter second num: "))
#     c = int(input("Enter third num: "))

# max_num = max(a, b, c)

# print(f"Max num is: {max_num}")

# Notes: n Python, variables defined inside a for or loop (or any loop) are still in the same scope as the rest of the code that surrounds the loop. Python does not create a separate block scope for loops, so variables declared in a loop are available after the loop ends.

# In Python, if-else blocks also do not create a separate block scope, similar to loops. Any variables defined inside an if, elif, or else block will still be accessible outside of these blocks, provided that the block gets executed.
# a=int(input('Enter a:'))
# a=20
# b=10
# print(a+b) #30

# a = "nana "
# b = 8
# c = a * b
# print(c, "Batman")

# print('123');
# print(int("123") + 2)

# n = 10
# sum_of_number = (n)*(n + 1)//2;
# print(sum_of_number)

# num = 3141
# sum_of_digits = 0

# sum_of_digits += num % 10
# num//=10
# sum_of_digits += num % 10
# num//=10
# sum_of_digits += num % 10
# num//=10
# sum_of_digits += num % 10
# num//=10
# print(sum_of_digits)

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))

# min_num = min(num1, num2, num3)
# max_num = max(num1, num2, num3)
# sum_of_num = num1 + num2 + num3
# middle = sum_of_num - (min_num + max_num)

# print(min_num, middle, max_num)

days = int(input("Enter days: "))
hours = int(input("Enter days: "))
minutes = int(input("Enter days: "))
seconds = int(input("Enter days: "))

total_time = (days * 24 * 3600) +(hours * 3600) + (minutes * 60) + seconds
print(total_time)





