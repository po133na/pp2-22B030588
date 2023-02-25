#Write a Python program to find sequences of lowercase letters
#joined with a underscore.

import re

txt = input()

x = '[a-z_]+' 

txt = re.findall(x, input())
if txt:
    print(*txt, ' ')