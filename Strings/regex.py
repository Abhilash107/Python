
import re
pattern = '02215'
print('Match' if re.fullmatch(pattern, '02215') else 'No match')
print('Match' if re.fullmatch(pattern, '20215') else 'No match')

#metacharacters
# [] {} () \ * + ^ $ ? . |
#The \ metacharacter begins each of the predefined character classes, each matching a specific set of characters




