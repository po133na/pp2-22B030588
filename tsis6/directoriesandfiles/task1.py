#Write a Python program to list only directories,
#files and all directories, files in a specified path.

import os

path = input()   #/Users/mac/Documents/GitHub/pp2-22B030588
os.chdir(path)      #change current dir to the path input below

dirctry = os.listdir(os.getcwd())   #get a list of all items in the current dir

for i in dirctry:
    if os.path.isdir(i):        #checking if its dir
        print(i)
    elif os.path.isfile(i):        #checking if its file
        print(i)