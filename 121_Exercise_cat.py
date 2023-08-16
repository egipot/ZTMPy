#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Tom", 3)
cat2 = Cat("Fluffy", 4)
cat3 = Cat("Yoko", 2)


# 2 Create a function that finds the oldest cat
Cat_list = [cat1, cat2, cat3]
print(type(Cat_list))
print(Cat_list)

def find_oldest_cat(Cats):
    oldest_age = 0
    for i in range (len(Cats)):
        if Cats[i].age > oldest_age:
            oldest_age = Cats[i].age
            oldest_cat = Cats[i].name
            return oldest_cat, oldest_age

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat_name, oldest_cat_age = find_oldest_cat(Cat_list)
print(f'The oldest cat is {oldest_cat_name} who is {oldest_cat_age} years old.')