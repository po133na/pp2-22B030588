#palindrome

str = input()

def palindrome(str):
    if str[::-1] == str[::1]:
        return True
    return False

print(palindrome(str))