#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

txt = input()

x = re.match(r'^a.*b$', txt) 
if x:
    print("match")
else: 
    print ("no")
