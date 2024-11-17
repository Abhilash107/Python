s = "abc"
for i in range (0, len(s)):
    str = ""
    for j in range (i, len(s)):
        str += s[j]
        print(str)