#Write a Python program to count the number of lines in a text file.

import os

path = r'/Users/mac/Documents/GitHub/pp2-22B030588/'
os.chdir(path)
txt = input()

result = open(txt, 'r')
cnt = 0

for str in result:
    if str != "\n":
        cnt += 1
        print(cnt)
