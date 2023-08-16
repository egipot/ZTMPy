from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
print(Counter(li))          # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
print(type(Counter(li)))    # <class 'collections.Counter'>

sentence = 'I want to check'
print(Counter(sentence))    # Counter({' ': 3, 't': 2, 'c': 2, 'I': 1, 'w': 1, 'a': 1, 'n': 1, 'o': 1, 'h': 1, 'e': 1, 'k': 1})

#turning an item e.g. list into a map or dictionary to keep count
#used in optimization 
#count duplicate users or duplicate emails

dictionary = {'a':1, 'b':2}
print(dictionary['a'])      #1

dictionary = defaultdict(lambda:5, {'a':1, 'b':2})  #give a callable object (lambda)
print(dictionary['c'])     #5

dictionary = defaultdict(lambda:'does not exist', {'a':1, 'b':2})  #give a callable object (lambda)
print(dictionary['c'])     #does not exist

dictionary = defaultdict(lambda:'does not exist', {'a':100, 'b':200})  #give a callable object (lambda)
print(dictionary['a'])     #100


d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print(d2 == d1) #False. OrderedDict checks the order obviously

d3 = {'c': 100}
d3['a'] = 1
d3['b'] = 2
d4 = {'c': 100}
d4['b'] = 2
d4['a'] = 1
print(d3 == d4) #True. Regular dictionaries have no sense of order