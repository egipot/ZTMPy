#own generator or own RANGE function

class myGen():
    current = 0
    def __init__(self, first, last):    #init function to have the range defined - first and last
        self.first = first
        self.last = last

    def __iter__(self):                 #iterate each step through the object myGen, using dunder method
        return self

    def __next__(self):
        if myGen.current < self.last:      #loop through the for-loop, then use the next value because the current/step is increased
            num = myGen.current
            myGen.current +=1
            return num
        raise StopIteration

gen = myGen(0,100)
for i in gen:
    print(i)
