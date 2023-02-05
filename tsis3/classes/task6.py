#Write a program which can filter prime numbers in a list by using filter function. 
#Note: Use lambda to define anonymous functions.

numbers = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)