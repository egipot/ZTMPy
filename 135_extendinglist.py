class SuperList(list):
    def __len__ (self):
        return 1000

super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list)) #True = is SuperList a subclass of list? = Yes

print(issubclass(list, object)) #True = is list a subclass of object? = Yes

# In python, everything is an object that inherits from the base object class. 
# We then inherit some built-in list methods and we're able to use all of that in our superlist just by inheriting.