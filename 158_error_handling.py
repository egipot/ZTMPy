
while True:
    try:
        age = int(input('what is your age?'))
        if age < 0:
            age = age * -1
            print(f'the input is a negative number, but it is automatically converted to its numerical positive value')
        print(age)
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number that is not equal to zero, but higher than zero')
    except ValueError: #this part is not run since the previous check is already satisfied
        print('!!!!') 
    else:
        print('thank you')
        break