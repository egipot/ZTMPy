#decorators start wtih '@'

#heirarchy: 
# 1 : function
# 2 : decorators
# 

#higher order function
# a. a function that accepts another function
def greet(func):
    func()

# b. a function that returns another function
def greet2():
    def func():
        return 5
    return func

