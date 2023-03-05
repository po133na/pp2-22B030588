#Write a Python program to delete file by specified path.
#Before deleting check for access and whether a given path exists or not.

import os

path = r'/Users/mac/Documents/GitHub/pp2-22B030588/'

os.chdir(path)
dirctr = os.listdir(os.getcwd())    #list of directory's content

for i in dirctr:        #
    if os.path.isdir(i):
        print(f'dir: {i}')
    elif os.path.isfile(i):
        print(f'file: {i}')

name = input()  #here we choose file's name
os.remove(name) #removin it

#In this case i've deleted file named P.txt as the result of task 6