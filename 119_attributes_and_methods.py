#OOP = object oriented programming
#create a class

#class names are usually singular
class PlayerCharacter:
    membership = True #class object attribute = does not change across the different instances
    def __init__(self, name, age): #dunder method or magic method; usually seen at the top; constructor method / init method
        if (PlayerCharacter.membership):
            self.name = name #where name is the parameter; also a class attribute = dynamic or changing or specific to each class object
            self.age = age
        
    def run(self):
        print('run')
        return 'done'  #if there is no return value, the output will be "None"

    def shout(self):
        print(f'my name is {self.name}')
        return 

#create a class of this object
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print (player1) #prints the memory where this object Cindy is located = <__main__.PlayerCharacter object at 0x000002300B787CD0>
print (player1.name) #Cindy
print (player1.age) #44

print (player2.name) #Tom
print (player2.age) #21

print(player1.run()) #run None if no return value; run done if with return value

print(player1) #<__main__.PlayerCharacter object at 0x000001A446244F10>; single memory used to refer to the same player which can be used over and over, when referring to the exact object instance
print(player2) #<__main__.PlayerCharacter object at 0x000001A446244F40>

print(player2.attack) #50

print(player1.membership)
print(player2.membership)

print(player1.shout())
print(player2.shout())