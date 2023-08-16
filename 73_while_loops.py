# while <condition> do <something>

i=0
#while i < 5:
#    print(i)
#    i += 1
#else: #will only execute if the while condition is false AND there is no "break" inside the while-loop
#    print('done with all the work')
#watch out / be careful for infinite loops


while i < 5:
    print(i)
    i += 1
    break
else: #will never be executed because there is "break" inside the while-loop
    print('done with all the work')