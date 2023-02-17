#generator

#import random

def ngen(N):
    i = 0
    while True:      #continues to return until the sq of N
        yield i*i
        if i == N:
            break
        else:
            i += 1
    
    
N = int(input())
print(*ngen(N))