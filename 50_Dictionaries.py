#Dictionaries a.k.a. hastable, maps, one of the data structures, organized data

dictionary = {
   #key:value
    'a': 1,
    'b': 2,
    'x': 3
}

print(dictionary['b']) #returns the value = 2
#print(dictionary[1]) #unordered key-value pair. This will return a KeyError


listed_dict = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
    },
    {
    'c': [4,5,6],
    'd': 'hi',
    'e': False    
    }
]

print(listed_dict[0]['a'][2])