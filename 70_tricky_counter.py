#counter

my_list = [1,2,3,4,5,6,7,8,9,10]

#egi solution
y=0
for x in my_list:
    y=y+x
print(y)
#lesson: use more readable variable names

#andrei solution
counter = 0 #use a variable outside the loop in order to avoid resetting the counter back to zero
for item in my_list:
    counter = counter + item
print(counter) #print outside/after the loop has finished