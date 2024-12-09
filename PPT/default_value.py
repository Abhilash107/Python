
def init(a = 2, b = 3, c = 4):
    print(a + b + c)

a = 2
b = 2
c = 2
#init(a,b,c) # 6
#init(a,b,)#8
#init(a, ,c)#Error
#init(a,)# 9 ==> 2 + 3 + 4
init(b,c) # 8