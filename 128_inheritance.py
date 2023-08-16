#PARENT CLASS
class User(object):
    def sign_in(self):
        print('logged in')

#CHILDREN CLASSES / subclasses of User / derived class
class Wizard(User):
    def __init__(self, name, power):
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

wizard1 = Wizard('Merlin', 50) 
archer1 = Archer('Robin', 100) 
wizard1.attack() #attacking with power of 50
archer1.attack() #attacking arrows: arrows left-100
print(isinstance(wizard1, Wizard)) #True because wizard1 is an instance of Wizard
print(isinstance(wizard1, User))    #True because wizard1 is an instance of Wizard which is under User
print(isinstance(wizard1, object))  #True because wizard1 inherits / gets method from Wizard class and even higher up base class (User)


#print(wizard1) # user is created <__main__.Wizard object at 0x0000024828397F10>

#print(wizard1.sign_in) #<bound method User.sign_in of <__main__.Wizard object at 0x0000017BCB977F10>> --therefore, add ()

#print(wizard1.sign_in()) #logged in /n None
