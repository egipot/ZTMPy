class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        return self

    def speak(self):
        print (f'My name is {self.name} and I am {self.age} years old.')

player1 = PlayerCharacter ('andrei', 100)
player1.speak() #My name is andrei and I am 100 years old.