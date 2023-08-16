a,b,c = ['x', 'y', 'z']
print(a)    #x
print(b)    #y
print(c)    #z


a,b,c,*other, d = ['x', 'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee']
print(other) #['aa', 'bb', 'cc', 'dd']
print(d)     #ee