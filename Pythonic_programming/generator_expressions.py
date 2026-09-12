
# squares = [x * x for x in range(5)]#List comprehension:


#Generator expression
# Produces values lazily, as needed.
#  produce values when needed

squares = (x * x for x in range(5)) 
# print(squares) #<generator object <genexpr> at 0x0000025394E09560>

for i in squares:
    print(i)