name = 'Johnny'
age = 55
age_str = str(age)

print('Hello ' + name + '. You are ' + str(age) + ' years young.')      #old method of declaring strings 

print(f'Hello {name}. You are {str(age)} years young.')                 #F-string == new feature of Python3

print('Hello {}. You are {} years young.'.format(name,age_str))         #other method of declaring strings with variables in Python2
print('Hello {1}. You are {0} years young.'.format(name,age_str))       #reversing 


