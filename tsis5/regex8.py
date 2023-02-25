#Write a Python program to split a string at uppercase letters.

def split_up(s):
    strings = []  #an empty list to store strngs
    index = 0 #pointer -> first char of split string
    
    for i in range(1, len(s)):      # iterate over the characters
        if s[i].isupper():
            strings.append(s[index:i])
            index = i       #start index to curr char
    
    strings.append(s[index:]) #last split string to the list
    
    return strings