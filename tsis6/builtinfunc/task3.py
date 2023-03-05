#Write a Python program with builtin function 
#that checks whether a passed string is palindrome or not.

str = input()
rts = str[::-1]

if hash(str) == hash(rts):
    print("Palindrome")
else:
    print("nah")