#filter

my_list = [1,2,3]
def multiply_by2(item):
    return item*2 

def odd(item):
    return item % 2 !=0

print(list(filter(odd, my_list)))  # [1, 3]
print(my_list)   # [1, 2, 3]