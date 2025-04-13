from custom_time import Time

t = Time()

print(t)

# Next, let’s create a Time object. Class Time’s __init__ method has hour, minute and second
# parameters, each with a default argument value of 0. Here, we specify the hour and
# minute—second defaults to 0:

t = Time(hour = 10, minute = 9)
print(t)#<custom_time.Time object at 0x0000021598227410> when __repl__ is not defined
print(t)#Time(hour= 10, minute=9, second=0) when __repr__ is  defined
print(t)#10:09:00 AM when __str__ is  defined

# The print() function and str() call the __str__ method because it is designed to provide a more user-friendly output.

# If __str__ is not defined, Python falls back to __repr__.

t = Time(hour = 10, second= 9)# 10:09:00 AM



