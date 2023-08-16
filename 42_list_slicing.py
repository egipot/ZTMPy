#lists are mutable

list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']
list_c = [1,2,'a', True]
list_amazoncart = ['notebooks', 'sunglasses', 'toys', 'grapes']

print(list_amazoncart[0::2]) #outputs ['notebooks', 'toys']
list_amazoncart[0] = 'laptop'

print(list_amazoncart)  #outputs ['laptop', 'sunglasses', 'toys', 'grapes']
print(list_amazoncart[0:3])

new_amazoncart = list_amazoncart    #this replaces the initial list GLOBALLY (including the previous declarations)
new_amazoncart[0] = 'gum'
print(new_amazoncart)
print(list_amazoncart)

new2_amazoncart = list_amazoncart[:] #using '[:]' in the syntax, copies the previous list into a new one, with means, this replaces only the new list (new2_amazoncart) and does not affect the previous declarations
new2_amazoncart[0] = 'phone'
print(new2_amazoncart) #outputs with new value 'phone' in location/index 0
print(list_amazoncart) #outputs the previously changed "gum", same as the globally changed value in new_amazoncart list