import io

try:
    with open('sad.txt', mode = 'w') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except io.UnsupportedOperation as err3:
    print('unsupported operation, check the mode versus the defined method (read/write/append, ...)')
    raise err3
except IOError as err2:
    print('issue with reading/writing the required file')
    raise err2


#when sad.txt is deleted in the current folder, the complete output is:
#file does not exist
#Traceback (most recent call last):
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\188_fileIOerrors.py", line 7, in <module>
#    raise err
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\188_fileIOerrors.py", line 3, in <module>
#    with open('sad.txt', mode = 'r') as my_file:
#FileNotFoundError: [Errno 2] No such file or directory: 'sad.txt''

#when sad.txt exists but the mode is changed from 'r' to 'w', which is inconsistent to read(), the output is:
# issue with reading/writing the required file
#Traceback (most recent call last):
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\188_fileIOerrors.py", line 11, in <module>
#    raise err2
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\188_fileIOerrors.py", line 5, in <module>
#    print(my_file.read())
#io.UnsupportedOperation: not readable

#if except ..err3 is stated before err2, only the print of err3 is printed
#unsupported operation, check the mode versus the defined method (read/write/append, ...)
#Traceback (most recent call last):
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\188_fileIOerrors.py", line 11, in <module>
#    raise err3
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\188_fileIOerrors.py", line 5, in <module>
#    print(my_file.read())
#io.UnsupportedOperation: not readable