def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

even_num = 0
x = 5
n = 5
sign = -1
sum = 1

for i in range(1, n + 1):
    even_num = 2 * i
    sum += (pow(x, even_num) * sign)/factorial(even_num)
    sign *= -1

print(sum)
