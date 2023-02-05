import math

#for

n = int(input())

for i in range (1, int(math.sqrt(n)+1)):
    print(i*i, ' ')

#while

i = 1
while i*i <= n:
    print(i*i)
    i += 1