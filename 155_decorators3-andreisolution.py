#decorator

#my solution
def my_decorator(func):
    def wrap_func(x):
        print('********')
        func(x)
        print('********')
    return wrap_func

greeting = 'okay!'

@my_decorator
def hello(greeting):
    print(greeting)


hello('hiiii') 