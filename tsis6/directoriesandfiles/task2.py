#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability 
#and executability of the specified path

import os

print('existence: ', os.access('/Users/mac/Documents/GitHub/pp2-22B030588', os.F_OK))
print('readability: ', os.access('/Users/mac/Documents/GitHub/pp2-22B030588)', os.R_OK))
print('writability: ', os.access('/Users/mac/Documents/GitHub/pp2-22B030588', os.W_OK))
print('executability: ', os.access('/Users/mac/Documents/GitHub/pp2-22B030588', os.X_OK))