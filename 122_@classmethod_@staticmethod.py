#OOP

class PlayerCharacter: 
    membership = True
    def __init__(self, name, age): #instantiate an object
        self.name = name #attributes
        self.age = age
        
    def shout():
        print(f'my name is {self.name}')

    @classmethod #Can access limited methods in the class. Can modify class specific details.
    def adding_things(cls, num1, num2):
        return cls ("Teddy", num1+num2) 
    @classmethod
    def adding_things2(cls, num3, num4):
        return num3 + num4

    @staticmethod #Cannot access anything else in the class. Totally self-contained code.
    def adding_things3(num5, num6):
        return (num5 + num6)

#player1 = PlayerCharacter('Tom', 20)
player3 = PlayerCharacter.adding_things2(5,6)
player4 = PlayerCharacter.adding_things3(7,8)

#print(player1.adding_things(2,3)) #5

print(PlayerCharacter.adding_things(3,4)) #7 if without the cls Teddy; if with "<__main__.PlayerCharacter object at 0x000001E59EB34F40>" = instantiated class
print(player3) #11
print(player4) #15