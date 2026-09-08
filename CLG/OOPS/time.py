from custom_time import Time

t2 = Time()

print(t2)

# Next, let’s create a Time object. Class Time’s __init__ method has hour, minute and second
# parameters, each with a default argument value of 0. Here, we specify the hour and
# minute—second defaults to 0:

t1 = Time(hour = 10, minute = 9)
print(t1)#<custom_time.Time object at 0x0000021598227410> when __repl__ is not defined
print(t1)#Time(hour= 10, minute=9, second=0) when __repr__ is  defined
print(t1)#10:09:00 AM when __str__ is  defined

# The print() function and str() call the __str__ method because it is designed to provide a more user-friendly output.

# If __str__ is not defined, Python falls back to __repr__.

t2 = Time(hour = 10, second= 9)# 10:09:00 AM --> wrong here
t3 = Time(hour=10, minute=9, second=0)  # Correct initialization

t3.hour = 70
print(t3.hour + t3.minute)# 19

t3.set_time(hour = 20, minute = 45, second = 10)
print(t3)

#IPython calls an object’s special method to produce a string representation
# of the object :::::Answer: __repr__.

#Properties are used like data attributes, but (as we’ll see in the next section) are implemented as methods.

t3.set_time((1,3,4))
print(t3)