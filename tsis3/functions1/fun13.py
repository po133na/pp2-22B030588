#guessthenumber

from random import random, randint, randrange

def guess(name):
    num = randint(1, 20)
    att = 1
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    while True:
        print('Take a guess.')
        inp = int(input())
        if inp == num:
            print(f'Good job, {name}! You guessed my number in {att} guesses!')
            break
        else:
            print('Your guess is too low.')
            att+=1
    
    
print('Hello! What is your name?')
name = input()
guess(name)
