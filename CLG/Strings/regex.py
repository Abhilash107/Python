
import re
pattern = '02215'
# print('Match' if re.fullmatch(pattern, '02215') else 'No match')
# print('Match' if re.fullmatch(pattern, '20215') else 'No match')

#metacharacters
# [] {} () \ * + ^ $ ? . |
#The \ metacharacter begins each of the predefined character classes, each matching a specific set of characters

# print('Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid')
# In the regular expression \d{5}, \d is a character class representing a digit (0–9). A character
# class is a regular expression escape sequence that matches one character. To match more
# than one, follow the character class with a quantifier. The quantifier {5} repeats \d five
# times, as if we had written \d\d\d\d\d, to match five consecutive digits
#print('Valid' if re.fullmatch(r'\d{4}', '02215') else 'Invalid')


# \d      Any digit (0–9).
# \D      Any character that is not a digit.
# \s      Any whitespace character (such as spaces, tabs and newlines).
# \S      Any character that is not a whitespace character.
# \w      Any word character (also called an alphanumeric character)—that is,
#         any uppercase or lowercase letter, any digit or an underscore
# \W       Any character that is not a word character.


#print('Valid' if re.fullmatch('[A-Z][a-z]*', 'W') else 'Invalid')
# print('Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid')
# print('Valid' if re.fullmatch('[A-Z][a-z]*', 'W0lly') else 'Invalid')

#The * quantifier matches zero or more occurrences
# of the subexpression to its left (in this case, [a-z]). So [A-Z][a-z]* matches an uppercase
# letter followed by zero or more lowercase letters, such as 'Amanda', 'Bo' or even 'E'.


#When a custom character class starts with a caret (^), the class matches any character
# that’s not specified. So [^a-z] matches any character that’s not a lowercase letter
# print('Match' if re.fullmatch('[^A-Z]', 'A') else 'No match')
# print('Match' if re.fullmatch('[^A-Z]', 'a') else 'No match')

#[*+$] matches a single *, + or $ character
# print('Match' if re.fullmatch('[*+$]', '*') else 'No match')
# print('Match' if re.fullmatch('[*+$]', '!') else 'No match')


#+, which matches at least one occurrence of a subexpression
#Both * and + are greedy—they match as many characters as possible
# print('Valid' if re.fullmatch('[A-Z]+[a-z]', 'WWWWWWa') else 'Invalid')
# print('Valid' if re.fullmatch('[A-Z][a-z]+', 'Waaa') else 'Invalid')


#The ? quantifier matches zero or one occurrences of a subexpression:
# print('Match' if re.fullmatch('labell?ed', 'labelled') else 'No match')
# print('Match' if re.fullmatch('label?ed', 'labeled') else 'No match')

#Then l? indicates that there can be zero or one more l characters before the remaining literal ed characters

#You can match at least n occurrences of a subexpression with the {n,} quantifier
# print('Match' if re.fullmatch(r'\d{3,}', '123') else 'No match')
# print('Match' if re.fullmatch(r'\d{17,}', '3465645456456567876867') else 'No match')


#You can match between n and m (inclusive) occurrences of a subexpression with the {n,m} quantifier.
# print('true' if re.fullmatch(r'\d{3,6}', '123') else 'No match')
# print('Match' if re.fullmatch(r'\d{3,6}', '12456655673') else 'No match')


#sub function replaces all occurrences of a pattern with the replacement text you specify.
# • the pattern to match (the tab character '\t')
# • the replacement text (', ') and
# • the string to be searched ('1\t2\t3\t4')
# and returns a new string.
# print(re.sub(r'\t', ', ', '1\t2\t3\t4'))
# print(re.sub(r'\t', ', ', '1\t2\t3\t4', count=2))


#The split function tokenizes a string, using a regular expression to specify the delimiter, and returns a list of strings
# splitting it at any comma that’s followed by 0 or more whitespace characters—\s is the whitespace character class and * indicates zero or more occurrences
#
#print(re.split('\$+', '123$Main$$Street'))

#Function search looks in a string for the first occurrence of a substring that matches a regular expression and returns a match object (of type SRE_Match) that contains the matching substring. The match object’s group method returns that substring:
result = re.search('Python', 'Python is fun')
##Function search returns None if the string does not contain the pattern:
#print(result)
# print(result.group() if result else 'not found')

# #Ignoring Case with the Optional flags Keyword Argument
# result3 = re.search('SaM', 'SAM WHITE', flags=re.IGNORECASE)
# print(result3.group() if result3 else 'Not found')



#The ^ metacharacter at the beginning of a regular expression (and not inside square brackets) is an anchor indicating that the expression matches only the beginning of a string
# result = re.search('^Python', 'Python is fun') #IMP
# print(result.group() if result else 'not found')


result = re.search('^Python', 'Python is fun')
print(result.group() if result else 'not found')

#Similarly, the $ metacharacter at the end of a regular expression is an anchor indicating that the expression matches only the end of a string

result = re.search('Python$', 'Python is fun')
# print(result.group() if result else "Not found")

result = re.search('fun$', 'Python is fun') #IMP
# print(result.group() if result else "Not found")



#Function findall finds every matching substring in a string and returns a list of the matching substrings.
contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
#print(re.findall(r'\d{3}-\d{3}-\d{4,7}', contact))


#Function finditer works like findall, but returns a lazy iterable of match objects. For large numbers of matches, using finditer can save memory because it returns one match at a time, whereas findall returns all the matches at once:
# for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
#     #print(phone.group())


text = 'Charlie Cyan, e-mail: demo1@deitel.in'
pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{2,3})'

res = re.search(pattern, text)
print(res.group() if res else "haha")
# print(res.group(0))
# print(res.group(1))
# print(res.group(2))






