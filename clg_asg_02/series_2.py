def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

sum = 1
x = 5
n = 5

for i in range(1, n+1):
    sum += pow(x, i)/factorial(i)

print(sum)
