# open
# open(filename, mode)

# Mode
# r read
# w write
# a append
# x create new file

# When using open() directly, close the file:

# file.close()
#* Why?
# Because files are external resources. Keeping them open unnecessarily can cause resource problems.

#* Read
# file = open('data.txt', 'r')
# content = file.read()
# file.seek(0)
# words = file.read(10)
# file.seek(0)
# line = file.readline()
# file.seek(0)
# lines = file.readlines()

# print(content)
# print(words)
# print(line)
# print(lines)
# file.close()


#* Write operation
# file = open('data.txt', 'w')
# file.write('I am Batman.\nI am IronMan')
# file.close()

# with Statement ⭐⭐⭐

# Use with for file handling.
# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# After the with block finishes, Python automatically handles closing the file.


with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

with open('data.txt', 'w') as file:
    file.write('New content')
    

with open('data.txt', 'a') as file:
    file.write('\nHehe siuuuuuuuuuu')






#Write operation
# file = open('data.txt', 'a')
# file.write('Currently I am staying in Bangalore')
# file.close()