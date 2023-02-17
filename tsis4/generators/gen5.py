#Implement a generator that returns all numbers from (n) down to 0.

def retrn(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in retrn(n):
    print(i)