# Strings are ordered and immutable.
st = 'Python'

print(st[0], st[1], st[-1])

print(st)
text = 'I am the GOAT'
print(text.lower())
print(text.upper())
print(text.strip())
print(text.split())
print(text.replace("a", "a\t"))
print(text.startswith("a"))
print(text.endswith("T"))
print(text.find("t"))
print(text.count("a"))


words = ["Python", "is", 'easy']

word = " ". join(words)
print(word)


# ^ Important: Strings are immutable ⭐⭐⭐

# This doesn't work:

text = "Python"
# text[0] = "J" # TypeError: 'str' object does not support item assignment
