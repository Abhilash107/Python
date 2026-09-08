num = int(input("Enter a number: "))
sum = 0
temp = num
while(temp > 0):
    sum += temp % 10
    temp//=10

while sum >= 10:
    temp = sum
    sum = 0
    while(temp > 0):
        sum += temp % 10
        temp//=10

print(sum)
