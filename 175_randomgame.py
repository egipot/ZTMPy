import sys
import random

first = sys.argv[1]
last = sys.argv[2]

guess = int(input(f'Enter an integer between {first} and {last}'))

if guess == random.random(last):
    print('success!')
else:
    print('nope')
