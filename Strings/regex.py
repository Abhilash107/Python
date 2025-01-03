
import re
pattern = '02215'
print('Match' if re.fullmatch(pattern, '02215') else 'No match')
print('Match' if re.fullmatch(pattern, '20215') else 'No match')




