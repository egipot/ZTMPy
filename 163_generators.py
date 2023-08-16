# generate a range of 100
# avoid printing the whole list - it requires that the list is being completely printed, before the next commands can be run
# generators are efficient way to handle huge list

def make_list(num):
    result = []
    for i in range (num):
        result.append(i*2)
    return result

my_list = make_list (100)
print(list(range(100)))