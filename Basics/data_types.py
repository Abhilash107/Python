age = 22
price = 99.5
name = "Abhilash"
is_student = True
result = None

print(type(age))        # int
print(type(price))      # float
print(type(name))       # str
print(type(is_student)) # bool
print(type(result))     # NoneType

print(0.1 + 0.2) # 0.30000000000000004
#This happens because floating-point numbers are represented approximately in binary.


#Complex numbers are written with a "j" as the imaginary part:
z = 3 + 4j
print(z.real) #3.0

print(z.imag) # 4.0
print(z) #(3+4j)
a = 1j + 3
b = 2 + 3j
print(a+b)# (5+4j)


name = "Abhilash"
print(name[0]) # A
print(name[len(name)-1]) # h

print(name[0:2])#0 , 1

print(name[:2])# start, 1

print(name[2:])# 2, end
name = "Python"

#name[0] = "J" # TypeError: 'str' object does not support item assignment cz str is immutable

first = "Hello"
second = "World"

result = first + " " + second
print(result)# Hello World
print("Hi " * 3)#Hi Hi Hi 

print(len("Python")) # 6

text = "I am IronMan"

print(text.lower)
print(text.lower())

print(text.upper)
print()
print()
print()
print()

