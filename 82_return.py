#return automatically exits the function, despite having further code below within the same func


def sum(num1, num2):
    num1 + num2
print(sum(4,5)) #None

def total(num3, num4):
    return num3 + num4
print(total(4,5)) #9

#function should do one task really well, e.g. print or store calculated value
#function always have to return something!

#a function either modifies a variable's value or return a value

def sum_(num5, num6):
    return num5 + num6

total_ = sum_(10,5)
print(sum_(10, total_))
print(sum_(sum_(10,5),10))

#not recommended
def sum__(num7, num8):
    def another_func(num7, num8):
        return num7 + num8
    return another_func(num7, num8)    

total__ = sum__(10, 20)
print(total__)

#recommended
def sum__(num7, num8):
    def another_func(num9, num10):
        return num9 + num10
    return another_func(num7, num8)    

total__ = sum__(10, 20)
print(total__)
