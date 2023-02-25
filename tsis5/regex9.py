#Write a Python program to insert spaces between words starting with capital letters.

import re

def insert_spaces(s):
    strings = re.findall('[A-Z][^A-Z]*', s) #for splitting string at capital letters
    
    spaces = ' '.join(strings) #join the split strings with spaces
    
    return spaces
