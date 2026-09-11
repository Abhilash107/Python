def greet():
    print("hello")

greet()




# Important distinction ⭐⭐⭐
# greet
# → refers to the function.

# greet()
# → calls/executes the function.


def greet_1():
    print("hello")

msg = greet_1() # prints hello
print(msg) # None




#parameter & arguments

# def greet(name):
#     return "Welcome, "+ name

def greet(name):
    return f"Welcome, {name}"

guest_1 = greet("Abhilash")
# print(guest_1)


#^
# Parameter = variable in the function definition
# Argument = actual value passed during the call
# name -> parameter
# Abhilash -> argument

# Multiple Parameters
def add(a, b):
    print(a + b)

# add(3, 4)



def subtract(a, b):
    return a - b

#? imp
def calculate(a, b):
    return a + b, a - b

x, y = calculate(10, 5)



# Positional Arguments

def introduce(name, age):
    print(name, age)

# introduce("Abhilash", 22)
# introduce(22, "Abhilash")

#^ Instead of relying on position, specify the parameter name.
#Keyword arguments
introduce(age=23, name="Papun")

# ! IMP
# introduce(23, name="IronMan")
# Actually, this is NOT valid because 23 is assigned positionally to name, and then you're also assigning "IronMan" to name using a keyword.

# Python will give:
# TypeError: introduce() got multiple values for argument 'name'


#? Positional argument cannot appear after keyword arguments
# introduce(name="IronMan", 23)

# RULE
# function(positional, positional, keyword=value, keyword=value)


# introduce("IronMan", age = 23)
# introduce(age=23, name="Papun")


# Default Arguments
def greet_2(name ="User"):
    print(f"Hello, f{name}")

# we can override it
greet_2("Cool Joe")


## '*args'
# it allows a function to accept a variable number of positional arguments
# Inside the function, args is a tuple.
def execute(*args):
    print(args)

execute(1,2,3,4)



def add(*nums):
    print(nums)
    sum = 0

    for i in nums:
        sum += i
    print(sum)

add(1, 2, 3, 4)


# '**kwargs'
# '**kwargs' allows a function to accept a variable number of keyword arguments.









