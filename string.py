# Expanded Notes: Strings - A Deeper Look

# Chapter 8: Strings - A Deeper Look

# 8.1 Introduction
# Notes: Strings are immutable and support sequence operations. Regular expressions (re module) allow pattern matching, critical for Natural Language Processing (NLP).

# 8.2 Formatting Strings
# Example: Formatting float values with f-strings
value = 17.489
formatted_value = f"{value:.2f}"
print("Formatted Value:", formatted_value)
# Output: Formatted Value: 17.49

# Notes: Presentation types like 'd' (integer), 'f' (float), and 'c' (character) specify how data is formatted.

# Self-Check:
# Question: What is the output of `f"{value:<10.2f}"`?
# Answer: `17.49     ` (left-aligned with 10-character width).

# 8.3 Concatenating and Repeating Strings
# Example: Concatenation and Repetition
s1 = "Hello"
s2 = "World"
print("Concatenated:", s1 + " " + s2)
# Output: Concatenated: Hello World
print("Repeated:", s1 * 3)
# Output: Repeated: HelloHelloHello

# 8.4 Stripping Whitespace
# Example: Removing leading, trailing, or all whitespace
name = "   Python String   "
print("Stripped:", name.strip())
# Output: Stripped: Python String
print("Left-Stripped:", name.lstrip())
# Output: Left-Stripped: Python String   
print("Right-Stripped:", name.rstrip())
# Output: Right-Stripped:    Python String

# Self-Check:
# Question: How does `strip('P ')` behave on "Python "?
# Answer: It removes 'P' and space, leaving "ython".

# 8.5 Changing Character Case
# Example: Changing case of strings
text = "happy birthday"
print("Capitalized:", text.capitalize())
# Output: Capitalized: Happy birthday
print("Title Case:", text.title())
# Output: Title Case: Happy Birthday
print("Uppercase:", text.upper())
# Output: Uppercase: HAPPY BIRTHDAY

# 8.6 Comparison Operators for Strings
# Notes: Comparisons are case-sensitive and based on Unicode values.
print("'Apple' < 'apple':", 'Apple' < 'apple')
# Output: 'Apple' < 'apple': True

# 8.7 Searching for Substrings
# Example: Count occurrences of a substring
sentence = "to be or not to be"
print("Occurrences of 'to':", sentence.count('to'))
# Output: Occurrences of 'to': 2

# Self-Check:
# Question: What is returned by `sentence.find('be')`?
# Answer: The index of the first occurrence, `3`.

# 8.8 Replacing Substrings
# Example: Replace substring
print("Replaced Sentence:", sentence.replace('to', 'TO'))
# Output: Replaced Sentence: TO be or not TO be

# 8.9 Splitting and Joining Strings
# Example: Splitting and joining
words = sentence.split()
print("Words:", words)
# Output: Words: ['to', 'be', 'or', 'not', 'to', 'be']
joined = ', '.join(words)
print("Joined:", joined)
# Output: Joined: to, be, or, not, to, be

# 8.10 Character-Testing Methods
# Example: Character testing
alphanumeric = "Python123"
print("Is Alphanumeric:", alphanumeric.isalnum())
# Output: Is Alphanumeric: True

# Notes: Common methods include `isalpha`, `isdigit`, and `isspace` for specific checks.

# 8.11 Raw Strings
# Notes: Useful for paths or strings with escape sequences.
path = r"C:\\Users\\Name"
print("Raw String Path:", path)
# Output: Raw String Path: C:\Users\Name

# 8.12 Regular Expressions
import re
# Example: Validate a phone number
pattern = r"\d{3}-\d{3}-\d{4}"
phone = "123-456-7890"
match = re.fullmatch(pattern, phone)
print("Valid Phone:", bool(match))
# Output: Valid Phone: True

# Exception Handling for Regular Expressions
# Example: Handle None when no match is found
no_match = re.fullmatch(pattern, "invalid-number")
try:
    if not no_match:
        raise ValueError("Invalid phone number format")
except ValueError as e:
    print("Error:", e)
# Output: Error: Invalid phone number format

# Self-Check: Can you modify this regex to allow spaces instead of hyphens?
# Answer: Use `pattern = r"\d{3} \d{3} \d{4}"`.

# 8.13 Data Munging with Pandas
import pandas as pd
# Example: Cleaning phone numbers
contacts = {"Name": ["Alice", "Bob"], "Phone": ["1234567890", "9876543210"]}
df = pd.DataFrame(contacts)
df['Phone'] = df['Phone'].map(lambda x: f"{x[:3]}-{x[3:6]}-{x[6:]}")
print("Cleaned DataFrame:", df)
# Output: Cleaned DataFrame: 
#     Name        Phone
# 0  Alice  123-456-7890
# 1    Bob  987-654-3210

# Exception Handling for Pandas
try:
    missing_column = df['Email']  # Attempting to access a non-existent column
except KeyError as e:
    print("Error:", e)
# Output: Error: 'Email'

# 8.14 Advanced Exercises
# Random Sentence Generator
import random
articles = ["the", "a", "one"]
nouns = ["cat", "dog", "man"]
verbs = ["jumps", "runs", "talks"]
prepositions = ["on", "over", "to"]
for _ in range(5):
    sentence = f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(prepositions)} {random.choice(articles)} {random.choice(nouns)}."
    print(sentence.capitalize())
# Output: Random sentences like "The cat runs to a dog."

# Pig Latin Conversion
# Example: Handle empty string input with exceptions
def to_pig_latin(phrase):
    if not phrase:
        raise ValueError("Input phrase cannot be empty")
    words = phrase.split()
    result = []
    for word in words:
        if word[0] in 'aeiou':
            result.append(word + 'ay')
        else:
            result.append(word[1:] + word[0] + 'ay')
    return ' '.join(result)

try:
    print("Pig Latin:", to_pig_latin(""))
except ValueError as e:
    print("Error:", e)
# Output: Error: Input phrase cannot be empty

print("Pig Latin:", to_pig_latin("hello world"))
# Output: Pig Latin: ellohay orldway

# Reverse a Sentence
sentence = "This is Python"
reversed_sentence = ' '.join(reversed(sentence.split()))
print("Reversed:", reversed_sentence)
# Output: Reversed: Python is This

# 8.15 Wrap-Up
# Notes: This chapter covered string formatting, manipulation, regular expressions, exception handling, and integration with pandas for data processing.
