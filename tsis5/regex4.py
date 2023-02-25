#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

txt = input()

x = '[A-Z_][a-z_]+' 

txt = re.findall(x, input())
if txt:
    print(*txt, ' ')