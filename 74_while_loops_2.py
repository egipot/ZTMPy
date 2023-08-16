
#useful for looping tasks with indefinite count of iteration, e.g. loop ends due to a condition that depends from another function's input

while True:
    #do something
    response = input('say something: ')
    if (response == 'bye'):
        break
    