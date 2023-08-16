#Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'n', 'c', 'A', 'A']

#egi solution
element = 0
duplicate_list = []
for element in range (len(some_list)):
    counter = some_list.count(some_list[element])
    #print(count_all)
    if counter > 1 and not duplicate_list.count(some_list[element]):
        duplicate_list.append(some_list[element]) 
print(duplicate_list)

#andrei solution
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)