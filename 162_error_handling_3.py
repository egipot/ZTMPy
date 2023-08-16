
while True:
    try:
        age = int(input('what is your age?'))
        10/age
        raise ValueError ('hey cut it out') 
        #customized error message
    except ZeroDivisionError:
        print('please enter a number that is not equal to zero, but higher than zero')
        break
    else:
        print('thank you')
    finally:
        print('ok, I am finally done')
    print('can you hear me?')

#what is your age?5
#ok, I am finally done
#Traceback (most recent call last):
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\162_error_handling_3.py", line 6, in <module>
#    raise ValueError ('hey cut it out')
#ValueError: hey cut it out