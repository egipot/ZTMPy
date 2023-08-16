# implement Fibonacci number
# starts with 0 and 1, then add the result to the next number

def fib(num): #maximum index number of the fibonacci that is required by an input, e.g. 20
    fib0 = 0  #declare the fixed first element in fib series
    fib1 = 1  #declare the fixed second element in fib series
    for i in range (num):       #loop until the user-defined max index minus 1
        yield fib0              #store the first element for later use
        temp_fib0 = fib0        #assign the current first element to a temp param fib0
        fib0 = fib1             #assign the current second element as the new first element
        fib1 = fib0 + temp_fib0 #assign the sum of current 1st and second as the new second element

max_index = int(input("Enter the maximum index in Fibonacci series: "))  #ask the user to input the max index in the fib series
for n in fib(max_index):        #loop to print each element according to the increasing n until max_index (user input)
    print(n)

    