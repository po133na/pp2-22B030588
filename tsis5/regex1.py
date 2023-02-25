#Write a Python program that matches a string 
#that has an 'a' followed by zero or more 'b''s.


import re

txt = input()
x = re.search(r"\ba*b", txt)

if x:
    print(x)