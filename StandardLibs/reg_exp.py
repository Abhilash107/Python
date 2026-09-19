# re = Regular Expressions

# Used for finding, matching, and replacing text based on patterns.


import re

text = "My phone is 9876543210"
match = re.search(r'\d+', text)
# \d → digit
# +  → one or more
print(match.group())


text = "I have 10 apples and 20 oranges"
print(re.search(r"\d+", text).group())
print(re.findall(r"\d+", text))


text = "hello 123"
result = re.sub(r"\d+", "XXX", text)
print(result)