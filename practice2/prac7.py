def ispalindrome(s: str):
    cnt = 0
    for i in range(len(s)):
        if s[0] == s[len(s)-1]:
            cnt += 1
    return 