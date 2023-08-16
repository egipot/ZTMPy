#decorator pattern

#andrei solution
def my_decorator(func):
    def wrap_func(*args, **kwargs):  #passing as many arguments as we want into the wrap function, 
        print('********')
        func(*args, **kwargs)        #then unpacking them inside of a function
        print('********')
    return wrap_func

@my_decorator
def hello(greeting, emoji = ';)'):
    print(greeting, emoji)


hello('hiiii') 
hello('good day')