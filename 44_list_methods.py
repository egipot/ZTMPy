
basket = [1,2,3,4,5]

print(len(basket))
print(basket.append(6)) #does not produce a value (no result) -->outputs: None

print(len(basket))
print(basket)           #outputs the original list "basket" with the appended element

#to reflect the "append" process in a new list, use = 
basket.append(7)
new_list = basket
print(basket)
print(new_list)

#insert
basket.insert(4,100)    #nothing to return
new_list2 = basket
print(basket)
print(new_list2)

#extend
basket.extend([101])
new_list3 = basket
print(basket)
print(new_list3)

#removing
basket.pop()        #removes the last element in the list (rightmost) ; RETURNS THE VALUE OF THE ELEMENT THAT WAS REMOVED
print(basket)
#basket.remove()

basket.pop(0)       #removes the 1st element (left most)
print(basket)

new_list4 = basket.remove(4)    #removes the element in location index 4 ; #nothing to return
print(new_list4)                #returns none

basket.clear()
print(basket)                   #returns empty list due to clear command

