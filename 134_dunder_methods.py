class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self): #modified __str__
        return f'{self.color}' #after this code is added, result = "red"

    def __len__(self):
        return 5

    #def __del__(self):
    #    print('deleted!')

    def __call__(self):
        return f'yes?'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())  #<__main__.Toy object at 0x000001C2CB8D7CD0>
print(str(action_figure))       #<__main__.Toy object at 0x000001C2CB8D7CD0>
print(str('action_figure'))
print(len(action_figure))
# del action_figure
print(action_figure()) #calling a function needs (). Remember to comment out "del action_figure" before running this line
print(action_figure['name']) #Yoyo


# double underscope dunder methods 
# example dunder str "__str__"
# https://docs.python.org/3/reference/datamodel.html#special-method-name
# Python allows custom modifiying of classes but be careful as it may cause confusion in huge programs