# https://docs.python.org/3/library/exceptions.html

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers {err}')

print(sum(1, '2'))

#please enter numbers unsupported operand type(s) for +: 'int' and 'str'
#None