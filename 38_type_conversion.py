name = 'egipot'
age = 50
relationship_status = 'single'

relationship_status = "it's complicated"

print(relationship_status)

#create a program that guesses your age:
#egi solution:
birth_year = input('Guess what year were you born:')
if (2021 - int(birth_year)) == age:
    print('you guessed it right!')
else:
    print('you guessed it wrong')

#andrei's solution:
birth_year_2 = input('What year were you born:')
age = 2021 - int(birth_year)
print(f'your age is: {age}')