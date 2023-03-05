#Write a Python program to write a list to a file.

import os

path = r'/Users/mac/Documents/GitHub/pp2-22B030588/'

os.chdir(path)
txt = input()

output = open(txt, 'w') #creating new file
output.write(str(list(map(int, input().split()))))  #reading user's input and writing it to neww file
output.close()