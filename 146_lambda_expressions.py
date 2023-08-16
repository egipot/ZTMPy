#lambda expressions = one-time anonymous function that is used only once; no need for names
#lambda keeps the code clean (no need for too many functions that are used only once); but tends to be confusing for other readers

from functools import reduce

#lambda param: action(param)

my_list = [1,2,3]

#def multiply_by2(item):
#    return item*2  --> no need for separate functions

#def odd(item):
#    return item % 2 !=0 --> no need for separate functions

#def accumulator(acc, item):
#    print(acc,item)
#    return acc + item --> no need for separate functions


print(list(map(lambda item: item*2, my_list))) #[2, 4, 6]  --> instead of multiply_by2 function
print(list(filter(lambda item: item % 2 !=0, my_list))) #[1, 3]
print(reduce(lambda acc, item: acc + item, my_list )) #6