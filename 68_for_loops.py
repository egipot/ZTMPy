 #for element/character in <iterable>

#string
for item in 'Zero to Mastery':
    print(item)

#list
for item in [1,2,3,4,5]:
    print(item)

#set
for item in (1,2,3,4,5):
    print(item)

#dictionary
for item in {1:'a', 2:'b', 3:'c'}:
    print(item)

#nesting for-loops where inner loops are iterized/finished first before going to the next item in the outer loop
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)