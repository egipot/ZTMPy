some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates) #['b', 'n']

#re-code using comprehension approach
duplicates2 = list({value for value in some_list if some_list.count(value)>1})
print(duplicates2) #['b', 'n']