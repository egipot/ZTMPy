#OOP = object oriented programming
#create a class


class PlayerCharacter:
    membership = True #class object attribute = does not change across the different instances
    def __init__(self, name = 'anonymous', age = 0):  
        if (age > 18):
            self.name = name  
            self.age = age

def shout(self):
    print(f'my name is {self.name}')

player1 = PlayerCharacter("Tom", 20)

print(player1.shout())