
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
# print('Valid' if re.fullmatch(r'\d{4}', '02215') else 'Invalid')


# \d      Any digit (0–9).
# \D      Any character that is not a digit.
# \s      Any whitespace character (such as spaces, tabs and newlines).
# \S      Any character that is not a whitespace character.
# \w      Any word character (also called an alphanumeric character)—that is,
#         any uppercase or lowercase letter, any digit or an underscore
# \W       Any character that is not a word character.


# print('Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid')
# print('Valid' if re.fullmatch('[A-Z][a-z]*', 'Wa lly') else 'Invalid')
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
# print('Valid' if re.fullmatch('[A-Z][a-z]+', 'WWWWa') else 'Invalid')


#The ? quantifier matches zero or one occurrences of a subexpression:
# print('Match' if re.fullmatch('labell?ed', 'labelled') else 'No match')
# print('Match' if re.fullmatch('labell?ed', 'labellled') else 'No match')

#Then l? indicates that there can be zero or one more l characters before the remaining literal ed characters

#You can match at least n occurrences of a subexpression with the {n,} quantifier
# print('Match' if re.fullmatch(r'\d{3,}', '123') else 'No match')
# print('Match' if re.fullmatch(r'\d{3,}', '3') else 'No match')


#You can match between n and m (inclusive) occurrences of a subexpression with the {n,m} quantifier.
# print('Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match')
# print('Match' if re.fullmatch(r'\d{3,6}', '12456655673') else 'No match')




















