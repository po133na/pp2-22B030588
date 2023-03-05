#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.

import os
#print('exists? ', os.access('/Users/mac/Documents/GitHub/pp2-22B030588', os.F_OK))
path = r'/Users/mac/Documents/GitHub/pp2-22B030588'

os.chdir(path)
    
print(os.getcwd())  #current working directory 

dirctr = os.listdir(os.getcwd())  #a list of it
for i in dirctr:
    if os.path.isdir(i):
        print(i)
    elif os.path.isfile(i):
        print(i)