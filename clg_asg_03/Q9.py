def binary_to_decimal(num):
    power = 0
    decimal = 0
    temp = num
    while(temp > 0):
        decimal += ((2**power ) * (temp%10))
        temp //= 10
        power += 1
    return decimal

def decimal_to_binary(num):
    if num == 0:
        return '0'
    temp = num
    res =""
    while(temp > 0):
        res = str(temp%2)+ res #Nice lomgic
        temp//=2
    
    return res



num1 = binary_to_decimal(1011)
num2 = decimal_to_binary(4)

print(num1)
print(num2)



