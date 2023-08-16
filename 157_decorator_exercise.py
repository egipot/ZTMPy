# Create an @authenticated decorator that only allows the function to run is user* has 'valid' set to True:


user1 = {
"name": "Sorna",
"valid": False, # changing this will either run or not run the message_friends function.
}

user2 = {
"name": "Sofia",
"valid": True, # changing this will either run or not run the message_friends function.
}

#decorator
def user_check(fn):
    def wrapper(user):
        if (user['valid'] == True):
            print(f"Hello, {user['name']}. Your access is granted.")
        else: 
            print(f"Sorry, {user['name']}. Your access is denied.")
    return wrapper

@user_check
def user_attempt(user):
    print('login attempt sent')

user_attempt(user1)
user_attempt(user2)

