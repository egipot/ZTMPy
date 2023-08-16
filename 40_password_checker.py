username = input('What is your username:')
password = input('What is your password:')

#egipot solution
print(f'Hi {username}! Your password {("*"*len(password))} is {len(password)} letters long.')

#andrei's solution == MORE READABLE CODE! (even though there is the same output)
password_length = len(password)
hidden_password = password_length*'*'
print(f'Hi {username}! Your password {hidden_password} is {password_length} letters long')