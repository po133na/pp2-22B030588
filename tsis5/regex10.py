#Write a Python program to convert a given camel case string to snake case.

import re

def camtosnake(s):
    camel = re.findall('[A-Za-z][^A-Z]*', s) #to split string at capital letters
    snake = '_'.join(camel).lower() #convert to lowercase from underscores
    
    return snake