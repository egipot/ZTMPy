#decorator


def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('helloooo')

hello() #helloooo
#********
#helloooo
#********

@my_decorator
def bye():
    print('see ya later!')

bye()
#********
#see ya later!
#********

#alternate writing but no need to write this way. adding @ on top of the function is clearer approach
hello2 = my_decorator(hello)
hello2()
#********
#********
#helloooo
#********
#********