#Bitwise operators
#However, there are four operators that allow you to manipulate single bits of data. They are called bitwise operators.

#They cover all the operations we mentioned before in the logical context, and one additional operator. 
#This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).

#Here are all of them:

#   & (ampersand) - bitwise conjunction;
#   | (bar) - bitwise disjunction;
#   ~ (tilde) - bitwise negation;
#   ^ (caret) - bitwise exclusive or (xor)


x = int(input("enter x: "))
y = int(input("enter y: "))
print(f'x in bit: {bin(x)}')
print(f'y in bit: {bin(y)}')
print(f'and_result = {x & y}')
print(f'or_result = {x | y}')
print(f'not_result = {~x}, {~y}')
print(f'nor_result = {x ^ y}')

# shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.
# The left argument of these operators is an integer value whose bits are shifted. 
# The right argument determines the size of the shift.
# Note:
#   17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)
#   17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)

#print(x,y)
print(f'var-right_result = {x} // {y} = {x} / (2^{y}) = {x >> y}')
print(f'var-left_result = {x} * 2^{y} =  {x << y}')