#OOP = object oriented programming
#create a class

#class names are usually singular
class PlayerCharacter:
    def __init__(self, name): #dunder method or magic method; usually seen at the top; constructor method / init method
        self.name = name #where name is the parameter
        
    def run(self):
        print('run')

#create a class of this object
player1 = PlayerCharacter('Cindy')
player2 = PlayerCharacter('Tom')

print (player1) #prints the memory where this object Cindy is located = <__main__.PlayerCharacter object at 0x000002300B787CD0>
print (player1.name) #Cindy
print (player2.name) #Tom