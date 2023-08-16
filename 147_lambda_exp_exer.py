my_list = [5,4,3]
print(list(map(lambda x: x**2, my_list)))


#list sorting
tuple_a = [(0,2), (4,3), (10, -1), (9,9)]
tuple_a.sort()
print(f'sorting according to the key: {tuple_a}')

tuple_b = [(0,2), (4,3), (10, -1), (9,9)]
tuple_b.sort(key=lambda x: x[1])
print(f'sorting according to the value: {tuple_b}')
