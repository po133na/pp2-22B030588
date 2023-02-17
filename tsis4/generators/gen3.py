#Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4, 
#between a given range 0 and n.

def threefour(n):
    i = 0
    while True:
        if (i % 3 == 0) and (i % 4 == 0):
            yield i
        if i == n:
            break
        else: i += 1

n = int(input())
print(*threefour(n), ' ')