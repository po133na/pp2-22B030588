#Write a Python program to generate 26 text files
#named A.txt, B.txt, and so on up to Z.txt

import os

path = r'/Users/mac/Documents/GitHub/pp2-22B030588/'
os.chdir(path)

for i in range(65, 91):
    res = open(chr(i)+'.txt', 'w')    #built in func w// letter and file format concatenated