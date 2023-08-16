for i, char in enumerate("Helloooo"):  #i = index counter
    print(i,char)
    
#0 H
#1 e
#2 l
#3 l
#4 o
#5 o
#6 o
#7 o

#egi solution
for index, character in enumerate (list (range(100))):
    if index == 50:
        print("the index of " + str(index) + " is " + str(character))
        print(f'the index of {index} is {character}')
        print('the index of {} is {}'.format(index, character))