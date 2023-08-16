is_old = True
is_licensed = False

# if <condition evaluating = True or False> :



if is_old and is_licensed:
    print('You are old enough to drive and you can drive!')
elif is_old==False and is_licensed:
    print("Age limit violation. You are not old enough")
elif is_old and is_licensed==False:
    print("Get a license first!")
else:
    print('Application rejected. Age limit violation and no license found. ')
