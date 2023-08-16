
basket = [1,2,3,4,5]
print(basket.index(2))  #where is the number 2 in the list

basket_a = ['a', 'b', 'c', 'd', 'e']
print(basket_a.index('c'))
print(basket_a.index('c',0,3))

print('d' in basket_a)  #True
print('D' in basket_a)  #False

basket_a.append('d')
print(basket_a)
print(basket_a.count('d'))