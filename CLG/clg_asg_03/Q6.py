def is_palindrome(str):
    l = 0
    h = len(str)-1
    while(l <= h):
        if(str[l] != str[h]):
            return False
        l+=1
        h-=1
    return True;

str = is_palindrome("ama")
print(str)