#Abstraction in python is defined as hiding the implementation of logic from the client and using a particular application. 
#And the most important key feature of Object-Oriented Programming. 
#It hides the irrelevant data specified in the project, reducing complexity and giving value to efficiency.
#Disadvantage: Can be overwritten if class name is class PlayerCharacter:
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print('run')

    def speak(self):
        print (f'My name is {self.name} and I am {self.age} years old.')

player1 = PlayerCharacter ('andrei', 100)
player1.speak() #My name is andrei and I am 100 years old.reused in later part of the code


#if this is added:
#{
#player1.name = '!!!'
#player1.speak = 'BOOO'
#print(player1.speak()) #this will return error     print(player1.speak()) TypeError: 'str' object is not callable
# }

#if this is added:
player1.name = '!!!'
player1.speak = 'BOOO'
print(player1.speak) #outputs BOOO which means the previously declared player1 relating to class is now overwritten to be strings

