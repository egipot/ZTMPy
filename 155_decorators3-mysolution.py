#decorator
def my_decorator(func):
    def wrap_func():
        print('********')
        func(greeting)
        print('********')
    return wrap_func

greeting = 'okay!'

@my_decorator
def hello(greeting):
    print(greeting)


hello() 