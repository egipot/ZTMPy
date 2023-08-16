#pure function = same input returns the same ouput always AND no side effects
# ^makes less buggy
# ^less risk to overwrite
# ^use as a guideline/recommended approach since it is not possible to use pure functions everywhere.


#example1
def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item*2)
    return new_li #pure function

print(multiply_by2([1,2,3])) 

#example2
def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item*2)
    return print(new_li) # not a pure function due to the side effect of 'print'

multiply_by2([1,2,3])

#example3
new_li = [] #not a pure func since new_li can be changed in another assignment later
def multiply_by2(li):
    for item in li:
        new_li.append(item*2)
    return new_li 

print(multiply_by2([1,2,3])) 
