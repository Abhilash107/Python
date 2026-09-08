my_list = [123, "chai", 3.14]
print(my_list)
print(len(my_list))
print(my_list[-1]) # last index

my_list_two = my_list
print(my_list_two)
my_list = "Hello"
print(my_list)
print(my_list_two)


l1 = [1, 2, 3]
l2 = l1

l1[0] = 44
# as l2 is referenced to l1
print(l2)  # [44, 2, 3]



# List is mutable
p1 = [9, 8, 7]
p2 = p1

# p2 is now pointing to a new list,
p2 = [9, 8, 7]

p1[0] = 55
# So it won't be affected by changes to p1
print(p2) #[9, 8, 7]


# Copying the list(not reference)

h1 =[1, 2, 3]
h2 = h1[:]

h1[0] = 100
print(h2) # [1, 2, 3]

n = [1, 2, 3]
m = n 
  
print(m is n)# print(m == n)





