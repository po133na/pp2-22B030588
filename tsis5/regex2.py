#Write a Python program that matches a string
#that has an 'a' followed by two to three 'b'.

import re

txt = input()
x = re.search("\bab{2, 3}", txt)

if x:
    print('Its a match')
else:
    print('Its not a match')