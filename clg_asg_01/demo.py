#print("Hello \nWorld ")#
#print("Hello \tWorld ")

#name = input("Enter your name: ")
#print(f"Hello {name}, User no: ",2020392993 + 1 )

#print('int(5.2)', 'truncates 5.2 to', int(5.2))
#print(''' a  b 'd'  "Abc" ''')

#print(type(name))
# default type of any input from console is STRING
# so use type casting

print("hehehe \\abhi ")
for _ in range(1): 
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))
    c = int(input("Enter third num: "))

max_num = max(a, b, c)

print(f"Max num is: {max_num}")

# Notes: n Python, variables defined inside a for or loop (or any loop) are still in the same scope as the rest of the code that surrounds the loop. Python does not create a separate block scope for loops, so variables declared in a loop are available after the loop ends.

# In Python, if-else blocks also do not create a separate block scope, similar to loops. Any variables defined inside an if, elif, or else block will still be accessible outside of these blocks, provided that the block gets executed.