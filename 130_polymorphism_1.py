#poly = many
#morphism = forms
#ability to redefine methods for these derived classes 
#and an object that gets instantiated can behave in different forms in differnt ways based on polymorphism


#PARENT CLASS
class User(object):
    def sign_in(self):
        print('logged in')
    #both user and wizard can run the attack method
    def attack(self):
        print(f'do nothing')

#CHILDREN CLASSES / subclasses of User / derived class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self) #user as parameter
        print(f'attacking with power of {self.power}')

#CHILDREN CLASSES
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking arrows: arrows left-{self.num_arrows}')

wizard1 = Wizard('Merlin', 50) 
archer1 = Archer('Robin', 100) 

def player_attack(char):
    char.attack()

player_attack(wizard1) #attacking with power of 50
player_attack(archer1) #attacking arrows: arrows left-100

#another method
for char in (wizard1, archer1):
    char.attack()

print(wizard1.attack()) 
#outputs None - this is overriding whatever the original attack was because we already have that method in our wizard

