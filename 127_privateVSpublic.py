#private - no true private variable in Python - how to workaround? use _ as prefix to a variable

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def run(self):
        print('run')

    def speak(self):
        print (f'My name is {self._name} and I am {self._age} years old.')

player1 = PlayerCharacter ('andrei', 100)
print(player1.speak()) #My name is andrei and I am 100 years old.reused in later part of the code


#if this is added:
#{
#player1.name = '!!!'
#player1.speak = 'BOOO'
#print(player1.speak()) #this will return error     print(player1.speak()) TypeError: 'str' object is not callable
# }

#if this is added:
#player1.name = '!!!'
#player1.speak = 'BOOO'
#print(player1.speak) #outputs BOOO which means the previously declared player1 relating to class is now overwritten to be strings

