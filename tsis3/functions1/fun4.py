#numbersspaces

numbers = list(map(int, input().split()))

def filter_prime(numbers):
    if numbers == 1 or numbers == 0:
        return False
    for i in range(2, int(numbers**0.5 + 1)):
        if numbers % i == 0:
            return False
    return True
        

for i in range(len(numbers)):
    if(filter_prime(numbers[i])):
        print(numbers[i], end=' ')