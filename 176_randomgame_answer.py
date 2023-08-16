from random import randint
import sys

#the range to be defined in the terminal command

# generate a number 1-10
answer = randint(int(sys.argv[1]),int(sys.argv[2]))
print(answer) #cheating hehe

# input from the user?

# check that input is a number 1-10
while True: #while loop is recommended in order to break when satisfied and not have an infinite loop
    try:
        guess = int(input(f'guess a number between {int(sys.argv[1])} to {int(sys.argv[2])}: '))
        if int(sys.argv[1]) <= guess <= int(sys.argv[2]):
            #print('all good')
            if guess == int(answer):
                print("you're a genius") 
                break
        else: 
            print(f'hey bozo, i said {int(sys.argv[1])} to {int(sys.argv[2])}. try again.')
    except ValueError:
            print('please enter a valid number')
            continue 
    


# check if number is the right guess. Otherwise, ask again