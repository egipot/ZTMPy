#poly = many
#morphism = forms

#PARENT CLASS
class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

#CHILDREN CLASSES / subclasses of User / derived class
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) #super class or class above User no need for self . Allows us to refer to User class  and not have to worry about passing self
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

#CHILDREN CLASSES
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking arrows: arrows left-{self.num_arrows}')

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com') 
archer1 = Archer('Robin', 100) 

def player_attack(char):
    char.attack()

player_attack(wizard1) #attacking with power of 50
player_attack(archer1) #attacking arrows: arrows left-100

#another method
for char in (wizard1, archer1):
    char.attack()

print(wizard1.email) 
#outputs None - this is overriding whatever the original attack was because we already have that method in our wizard

