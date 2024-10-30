def reverse_string(str):
    s = ''
    for i in range(len(str)-1, -1, -1):
        s += str[i]
    return s;


str = reverse_string("Abc")
print(str)
