#short circuiting is done with OR logic because one of the logic (usually the 1st logic) is already satisfied

is_friend = False
is_user = True

print(is_friend or is_user) #True because both are true (AND logic)

if is_friend and is_user:
    print("best friends forever")