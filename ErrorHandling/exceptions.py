# An exception is an error that occurs while the program is running.

# A syntax error means Python cannot understand the code.

#try
# Put code that might cause an exception inside 


#except

# except specifies what to do when an exception occurs.

try:
    x = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")



# try:
#     x = int(input("Enter a number: "))
#     res = 10 / x
# except ValueError:
#     print("Enter a valid number!!!!!!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!!!!!!")



# Catching the exception object
# You can use as
# except ZeroDivisionError as z:
#     print(z)



#else:
# else runs only when no exception occurred in the try block.


# finally ⭐⭐⭐
# finally always executes, whether an exception occurs or not.


try:
    x = int(input("Enter a number: "))
    res = 10 / x
except ValueError as v:
    print(v, "Enter a valid number!!!!!!")
except ZeroDivisionError as z:
    print(z, "Cannot divide by zero!!!!!!")
else:
    print("Division successful.........\nResult is: ",res)

finally:
    print("Execution finished.")

# raise
# allows you to deliberately raise an exception.

# age = -10
# if age < 0:
#     raise ValueError("Age cannot be negative")



try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as e:
    print("Invalid input:", e)


# Custom Exception
class InvalidAgeError(Exception):
    pass


try:
    age = -10
    if age < 0:
        raise InvalidAgeError("Age can not ne negative")

except InvalidAgeError as e:
    print(e)