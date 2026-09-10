print("Hello world")
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

2 + 2

50 - 5*6

(50 - 5*6) / 4

print(8 / 5)  # division always returns a floating-point number
print(8 // 5) # floor division

17 / 3  # classic division returns a float


17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

5 * 3 + 2  # floored quotient * divisor + remainder

5 ** 2  # 5 squared

2 ** 7  # 2 to the power of 7

print('doesn\'t')
print('"Yes," they said.')
print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
print(s)


print('C:\this\name')  # here \t means tab, \n means newline


print(r'C:\this\name')  # note the r before the quote

prefix = 'Py'
print(prefix + 'thon')  # can't concatenate a variable and a string literal


print(('un' * 3) + 'ium') # unununium


word = 'Python'
word[0]  # character in position 0

word[5]  # character in position 5





# Multi-line documentation/comments
# Python doesn't have a dedicated multi-line comment syntax.
# Triple-quoted strings are often used for documentation:

"""
This is a string literal.
It can span multiple lines.
"""