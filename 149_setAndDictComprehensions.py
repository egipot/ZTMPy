# comprehensions
# usable in list, set, dictionary
# quick way to create loops, sets or dictionaries instaed of looping

#1
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k, v in simple_dict.items() if v%2 == 0}
print(my_dict)

#2 item is the key and item*2 is the value
#my_dict2 = {for num in [1,2,3]}
my_dict2_result = {num:num*2 for num in [1,2,3]   }
print(my_dict2_result)