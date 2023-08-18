# ZTM Section 15: Testing in Python


def do_stuff(num):
    try:
        if num: #default to True if it has any value, otherwise if NoneType or not existing = 0
            return int(num) + 5
        else:
            return 'please enter a number'
    except ValueError as err:
        return err
