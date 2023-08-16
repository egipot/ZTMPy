#parameters = used to define the function

#default parameters
def say_hello(name = 'Darth Vader', emoji = '😂'):
    print(f'heloooo {name} {emoji}')

#arguments = used to call / invoke the function 
say_hello('Andrei', '😉' ) 
say_hello('Dan', '😉' ) 
say_hello('Emily', '😉' ) 
# ^ positional arguments, i.e. needs to be in the proper position

#keyword arguments --> Make sure that these have consistent order to avoid possible confusion
say_hello(emoji = '😉', name = 'Bibi')

#print the default
say_hello() 

print('😉')