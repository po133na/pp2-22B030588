#Write a program using generator to print the even numbers 
#between 0 and n in comma separated form 
#where n is input from console.

def evenums(n):
    nums = 0
    while True:
        if (nums % 2) == 0:
            yield nums
        if nums == n:   #endpoint
            break
        else: nums += 1

n = int(input())
print(*evenums(n), ' ')