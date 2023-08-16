#https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
#https://stackoverflow.com/questions/5119709/true-and-false-in-python 

#truthy and falsey checking is useful if parameter exists, without checking/converting the values themselves.

is_old = 'hello' #this is internally converted to boolean as TRUE value
is_licensed = 5 #this is internally converted to boolean as TRUE value

print(bool(is_old))
print(bool(is_licensed))

if is_old and is_licensed:
    print('you are old enough to drive and you have a license!')
else:
    print('You are not of age!')

    print('okoko')