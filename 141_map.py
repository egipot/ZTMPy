#map, filter, zip, reduce = functional programming
#map = allows us to simplify the code
#map = useful in iterations
# input #items and returns/outputs the same #items

def multiply_by2(item):
    #{new_li = []
    #for item in li:
    #    new_li.append(item*2)
    #return new_li } -->  NO NEED to define these lines in {}
    return item*2 

print(list(map(multiply_by2, [1,2,3]))) #define AFTER the function multiply_by2 = [2, 4, 6]
#print(multiply_by2([1,2,3])) 


#example2
#map allows you to create a whole new list without modifying the original list
my_list = [1,2,3]
def multiply_by2(item):
    return item*2 

print(list(map(multiply_by2, my_list))) #[2, 4, 6]
print(my_list) #[1, 2, 3]