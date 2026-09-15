# os is a standard-library module for interacting with the operating system.
import os
print(os.getcwd())
print(os.listdir())
# print(os.listdir('data.txt'))
print(os.path.exists('data.txt'))
os.mkdir('data')

