#Write a python program to convert snake case string to camel case string.

import re

def stoc(s):
    words = s.split('_') # split string into words separated by underscore
    capw = [words[0]] + [word.capitalize() for word in words[1:]] #capitalize first letter of each word except the first one
    
    camel = ''.join(capw) # join the words back together into a single string
    
    return camel

