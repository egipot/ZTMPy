basket_a = ['a', 'b', 'c', 'd', 'e', 'd']
#print(basket_a.sort())                             #returns None

#instead, separate the sorting process first
basket_a.sort()
print(basket_a)                                     #returns ['a', 'b', 'c', 'd', 'd', 'e']

#alternate sorting code:
basket_b = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(sorted(basket_b))                             #returns ['a', 'b', 'c', 'd', 'd', 'e', 'x']; Sorted produces a new copy of the array and not changing the original list
print(basket_b)                                     #returns ['a', 'x', 'b', 'c', 'd', 'e', 'd'


#copying list in two ways
#first
new_basket = basket_b[:]
new_basket.sort()
print(new_basket)                                   #returns ['a', 'b', 'c', 'd', 'd', 'e', 'x']
#second
new_basket_2 = basket_b.copy()
new_basket_2.sort()
print(new_basket_2)                                 #returns ['a', 'b', 'c', 'd', 'd', 'e', 'x']


#reverse
new_basket_2.reverse()
print(new_basket_2)
