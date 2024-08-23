num = 2+2j
print(num + 3) # (5+2j)


octal_num = 0o20
print(octal_num)

hex_num = 0x20
print(hex_num)

binary_num = 0b100
print(binary_num)


print(int('64', 16)) # to hexadecimal
print(int('101', 2)) # to binary


x = 1
print(x << 2) # 4 ===> 100

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.4'))

print((0.1 + 0.1+ 0.1) - 0.3 )  # 5.551115123125783e-17