#https://docs.python.org/3/library/functions.html
#https://www.w3schools.com/python/python_ref_string.asp 

quote = 'to be or not to be'
print(quote.upper())        #all caps
print(quote.lower())        #all lower-case 

print(quote.capitalize())   #only the beginning of the sentence
print(quote.encode())       #bytes

print(quote.find('be'))     #find a string and returns the location == outputs 3

quote2 = quote.replace('be', 'me')
print(quote2)

print(quote)                #outputs the same as declared above == because strings are immutable, i.e. cannot be changed; but can be replaced


