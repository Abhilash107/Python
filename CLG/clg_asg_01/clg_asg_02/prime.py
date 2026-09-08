import math
num = 17
flag = True
sqrt_num = int(math.sqrt(num))
for i in range(2, sqrt_num+1):
    if(num%i == 0):
        flag = False
        break
if(flag):
    print("prime")
else:
    print("Nope")




