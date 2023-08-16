#own FOR-loop code:

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
special_for([1,2,3])

# <list_iterator object at 0x0000028482073070>
# 1
# <list_iterator object at 0x0000028482073070>
# 2
# <list_iterator object at 0x0000028482073070>
# 3
# <list_iterator object at 0x0000028482073070>  same memory is used in every iteration
