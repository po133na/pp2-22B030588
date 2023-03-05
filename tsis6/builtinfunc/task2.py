#Write a Python program with builtin function that accepts a string
#and calculate the number of upper case letters and lower case letters

str = input()

lower = 0
upper = 0

for i in str:
    if ord(i) >= 65 and 90 >= ord(i):
        lower += 1
    elif ord(i) >= 97 and 122 >= ord(i):
        upper += 1

print(lower, upper)