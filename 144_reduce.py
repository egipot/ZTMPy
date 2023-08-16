#reduce(function, sequence, initial value)
#map and filter functions also use reduce internally


from functools import reduce
my_list = [1,2,3,4]

def accumulator(acc, item):
    print(acc,item)
    return acc + item

print(reduce(accumulator, my_list, 10)) #reduce does not output a list
print(my_list)    

# if initial value = 0, the output is: 10
#0 1
#1 2
#3 3
#6 4
#10
#[1, 2, 3, 4]

# if initial value = 10, the output is: 20
#10 1
#11 2
#13 3
#16 4
#20
#[1, 2, 3, 4]