# 1. imp
# def replace_repeated(s):
#     result = [s[0]]
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             result.append('*')
#         else:
#             result.append(s[i])
#     return ''.join(result)
# print(replace_repeated('balloon'))

# 2.
# def are_anagrams(str1, str2):
    # return sorted(str1) == sorted(str2) 
    # or
    # return set(str1) == set(str2)
# print(are_anagrams('listen', 'silent'))

# 3.
# def word_count(sentence):
#     return len(sentence.split())
# print(word_count('This is a sample sentence'))

# 4.
# def char_count(s, char):
#     return s.count(char)
# print(char_count('balloon', 'o'))

# 5. 
# def longest_word_length(sentence):
#     return max(len(word) for word in sentence.split())
# print(longest_word_length('Python programming language'))

# 6.


# 7.imp
# def is_rotational_palindrome(s):
#     for i in range(len(s)):
#         if (s[i:] + s[:i]) == (s[i:] + s[:i])[::-1]: ----> GPT
#             return True
#     return False
# print(is_rotational_palindrome('aab'))

# 8.
# import re
# def is_valid_url(url):
#     pattern = re.compile(
#         r'^(http|https)://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(:[0-9]+)?(/.*)?$' ----> simplify it(remove optional groups)
#     )
#     return bool(pattern.match(url))
# print(is_valid_url('https://example.com'))

# 9.
# def count_vowels_consonants(s):
#     vowels = 'aeiou'
#     v_count = sum(1 for char in s if char.lower() in vowels)
#     c_count = sum(1 for char in s if char.isalpha() and char.lower() not in vowels)
#     return v_count, c_count
# print(count_vowels_consonants('hello baby'))

# s = 'aeiou'
# c_count = v_count = 0
# vowel = 'aeiou'
# for c in s:
#     if c in vowel:
#         v_count = v_count + 1 
#     else:
#         c_count=c_count + 1
       

# print(c_count, v_count)




# 10.  imp
# def reverse_tokens(sentence):
#     return ' '.join(sentence.split()[::-1])
# print(reverse_tokens('This is a test'))

# 11.
# def extract_b_d_words(sentence):
#     import re
#     pattern = r'\bb\w*d\b'
#     return re.findall(pattern, sentence)
# print(extract_b_d_words('The big bird baked a bread and bolted.'))


# 12.
# from itertools import permutations # ---> WOW
# def generate_three_letter_combinations(word):
#     return [''.join(p) for p in permutations(word, 3)]
# print(generate_three_letter_combinations('bathe'))

# 13.
# def remove_extra_spaces(sentence):
    # import re
    # return re.sub(r'\s+', ' ', sentence).strip()
    # or
    # return ' '.join(s.strip() for s in sentence.split())
# print(remove_extra_spaces('Hello    World  !  '))

# 14. imp
def reverse_middle_half(s):
    n = len(s)
    start = n // 4
    end = n - n // 4
    return s[:start] + s[start:end][::-1] + s[end:] # ---> GPT
print(reverse_middle_half('abcdefghij'))

# 15.
# def substrings_of_frequency(s, freq):
#     from collections import Counter
#     count = Counter(s)
#     return ''.join([char * freq for char in count if count[char] == freq])
# print(substrings_of_frequency('aabbbccccddddd', 3))

# 16. imp
# def unique_sorted_characters(s):
#     return ''.join(sorted(set(s)))

# print(unique_sorted_characters('mississippi'))
# Output: 'imps'


# 17. 
# s = "how now brown cow"
# print(s[s.find('o'):s.rfind('o')])
# Output: "ow now brown c"
# Explanation: The substring starts at the first 'o' and ends at the last 'o', excluding the last one.

# print(chr(ord('A') + 2) + chr(ord('Z') - 3))
# Output: "CW"
# Explanation: 'A' + 2 gives 'C', and 'Z' - 3 gives 'W'.

# s = "abc123def456ghi789"
# indices = [i for i, c in enumerate(s) if c == '']
# result = s[indices[1]+1:indices[2]] + s[indices[4]+1:]
# print(result)
# Output: SyntaxError due to incorrect use of `''` for empty string (should use space or valid character).

# s = "abracadabra"
# print(s.replace(s[s.find('a'):s.find('r')], "XYZ"))
# Output: "XYZracadabra"
# Explanation: Replaces the substring from the first 'a' to the first 'r' ("ab") with "XYZ".

# s = "hello"
# shift = 2
# print("".join(chr((ord(c) - 97 + shift) % 26 + 97) for c in s))
# Output: "jgnnq"
# Explanation: Shifts each character by 2 in the alphabet.

# s = "mississippi"
# print("".join(sorted(set(s))))
# Output: "imps"
# Explanation: Extracts unique characters and sorts them.

# 18.
# quote = "The quick brown fox jumps over the lazy dog"

# (a) Convert to uppercase
# print("18a:", quote.upper())  # Output: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

# (b) Reverse the string
# print("18b:", quote[::-1])  # Output: "god yzal eht revo spmuj xof nworb kciuq ehT"

# (c) Extract a substring
# print("18c:", quote[4:19])  # Output: "quick brown fox"

# (d) Replace a word
# print("18d:", quote.replace('fox', 'cat'))  # Output: "The quick brown cat jumps over the lazy dog"

# (e) Count occurrences of 'o'
# print("18e:", quote.count('o'))  # Output: 4

# (f) Check if it starts with 'The'
# print("18f:", quote.startswith('The'))  # Output: True

# (g) Check if 'brown' is in the string
# print("18g:", 'brown' in quote)  # Output: True

# (h) Check if all characters are lowercase
# print("18h:", quote.islower())  # Output: False

# 19.
quote = "Knowledge is power. Power is gained through knowledge."

# (a) Find the index of 'power'
print("19a:", quote.index('power'))  # Output: 13

# (b) Find the last occurrence of 'knowledge'
print("19b:", quote.rfind('knowledge'))  # Output: 50

# (c) Convert to title case
# print("19c:", quote.title())  # Output: "Knowledge Is Power. Power Is Gained Through Knowledge."

# (d) Convert to lowercase
# print("19d:", quote.lower())  # Output: "knowledge is power. power is gained through knowledge."

# (e) Convert to uppercase
# print("19e:", quote.upper())  # Output: "KNOWLEDGE IS POWER. POWER IS GAINED THROUGH KNOWLEDGE."

# (f) Check if it ends with 'knowledge.'
# print("19f:", quote.endswith('knowledge.'))  # Output: True

# (g) Split the string by spaces
# print("19g:", quote.split(' '))  # Output: ['Knowledge', 'is', 'power.', 'Power', 'is', 'gained', 'through', 'knowledge.']

# (h) Partition the string at 'is'
# print("19h:", quote.partition('is'))  # Output: ('Knowledge ', 'is', ' power. Power is gained through knowledge.')

# (i) Check if all characters are alphabetic
# print("19i:", quote.isalpha())  # Output: False (contains spaces and punctuation)

# 20.
# import re
# string1 = "Python Programming Language"

# (a) Match any character followed optionally by 'm'
# match1 = re.search(r'. m?', string1)
# print("20a:", match1.group() if match1 else None)  # Output: " P"

# (b) Match the string ending with 'Language'
# match3 = re.search(r'.*Language$', string1)
# print("20b:", match3.group() if match3 else None)  # Output: "Python Programming Language"

# (c) Match 'w* s w*'
# match4 = re.search(r' w* s w*', string1)
# print("20c:", match4.group() if match4 else None)  # Output: None

# (d) Match the entire string
# match5 = re.search(r'.*', string1)
# print("20d:", match5.group() if match5 else None)  # Output: "Python Programming Language"

# 21.
# import re
# string1 = 'Python Programming Language'
# # match1 = re.fullmatch(r'[A-Za-z]*', string1)
# # print(match1.group() if match1 else None)

# match2 = re.sub(r'Programming', 'Coding', string1)
# print(match2)

# match3 = re.split(r'\s+', string1)
# print(match3)

# match8 = re.findall(r'\w+', string1)
# print(match8)

# 22.
# def is_symmetric(string):
#     return string == string[::-1]
# string = "madam"
# print("Symmetric" if is_symmetric(string) else "Asymmetric")

# 23.
def delete_char_at_index(s, i):
    return s[:i] + s[i+1:]
s = "example"
i = 3
print(delete_char_at_index(s, i))

# 24.
# import re
# def validate_password(password):
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*?]).{8,}$'
#     return bool(re.fullmatch(pattern, password))
# password = "Aa1@secure"
# print("Valid password" if validate_password(password) else "Invalid password")

# 25.
import re
def analyze_string(s):
    digits = len(re.findall(r'\d', s))
    non_digits = len(re.findall(r'\D', s))
    whitespaces = len(re.findall(r'\s', s))
    words = len(re.findall(r'\w+', s))
    return digits, non_digits, whitespaces, words
s = "This is a test string with 123 digits!"
digits, non_digits, whitespaces, words = analyze_string(s)
print(f"Digits: {digits}, Non-digits: {non_digits}, Whitespace: {whitespaces}, Words: {words}")