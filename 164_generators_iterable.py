# range is an iterable and also a generator
# list is an iterable but not a generator
# a generator is a subset of an iterable

# yield keyword turns a function into a generator, for the "next" iteration
# https://www.geeksforgeeks.org/python-yield-keyword/ 


def generator_function(num):
    for i in range (num):
        yield i*2
        #yield pauses the function and comes back to it when "next" is called

g = generator_function(100)
#print(g) #<generator object generator_function at 0x0000023C041A2BA0>
next(g)
next(g)
next(g)
next(g)
print(next(g)) #8
next(g)
print(next(g)) #12

# for item in generator_function(10):
#     print(item)
