import sys
sys.float_info.dig,15
s1 = '3.14159265358979'   #decimal string with 15 significant digits
format(float(s1),'.15g')  #convert to float and back -> same value
print(s1)

s2 = '9876543211234567' # 16 significant digits is too many!
format(float(s2),'.15g')  ## conversion changes value
print(s2)


#https://stackoverflow.com/questions/61731913/understanding-sys-float-info-for-maximum-floats-in-python
#The documentation says “If X, then Y,” where X is:
# -- A decimal numeral with up to 15 significant digits is converted to your Python implementation’s float and back to the nearest decimal numeral with at most 15 significant digits.
#and Y is:
#
# -- The number represented by the original numeral equals the resulting numeral.
#That says only what happens if X is true. It does not say what happens if X is false. You have given us a situation where Y is true (you got back the original number) and complained that X is false. That is consistent with the documentation.

#  ""Also, sys.float_info.min yields 2.2250738585072014e-308 which is is obviously a lot smaller and also has 17 significant digits, if I'm correct? How does that work when sys.float_info.dig = 15? Am I confusing something here?""

#Every floating-point datum other than a NaN (Not a Number) represents one number exactly. It is exactly that number, regardless of how many decimal digits are required to express that number. sys_float_info.dig tells you a property about how fine the floating-point representation is. It tells you the floating-point representation is so fine, meaning that the numbers it does represent are so close together, that they can be used to distinguish between 15-digit decimal numerals. That just tells you how close the representable numbers are to each other. It does not tell you how many decimal digits it takes to exactly express any of those numbers.

#In fact, the smallest positive number representable in your Python implementation’s floating-point format is 2−1074, which is 4.940656458412465441765687928682213723650598026143247644255856825006755072702087518652998363616359923797965646954457177309266567103559397963987747960107818781263007131903114045278458171678489821036887186360569987307230500063874091535649843873124733972731696151400317153853980741262385655911710266585566867681870395603106249319452715914924553293054565444011274801297099995419319894090804165633245247571478690147267801593552386115501348035264934720193790268107107491703332226844753335720832431936092382893458368060106011506169809753078342277318329247904982524730776375927247874656084778203734469699533647017972677717585125660551199131504891101451037862738167250955837389733598993664809941164205702637090279242767544565229087538682506419718265533447265625•10−324.

#################

#https://www.demo2s.com/python/python-sys-intro.html
#https://www.demo2s.com/python/python-sys-float-info.html
#Example1
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize)
##result
## Float value information:  sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
## Integer value information:  sys.int_info(bits_per_digit=30, sizeof_digit=4)
## Maximum size of an integer:  9223372036854775807

#Example2
#print("Long Integer value information: ",sys.long_info) #Returns: AttributeError: module 'sys' has no attribute 'long_info'. Did you mean: 'float_info'?

#Example3
print('Smallest difference (epsilon):', sys.float_info.epsilon)
print()# w ww  .  dem o 2 s  . c om
print('Digits (dig)              :', sys.float_info.dig)
print('Mantissa digits (mant_dig):', sys.float_info.mant_dig)
print()
print('Maximum (max):', sys.float_info.max)
print('Minimum (min):', sys.float_info.min)
print()
print('Radix of exponents (radix):', sys.float_info.radix)
print()
print('Maximum exponent for radix (max_exp):',
      sys.float_info.max_exp)
print('Minimum exponent for radix (min_exp):',
      sys.float_info.min_exp)
print()
print('Max. exponent power of 10 (max_10_exp):',
      sys.float_info.max_10_exp)
print('Min. exponent power of 10 (min_10_exp):',
      sys.float_info.min_10_exp)
print()
print('Rounding for addition (rounds):', sys.float_info.rounds)
##Result
## Smallest difference (epsilon): 2.220446049250313e-16

## Digits (dig)              : 15
## Mantissa digits (mant_dig): 53

## Maximum (max): 1.7976931348623157e+308
## Minimum (min): 2.2250738585072014e-308

## Radix of exponents (radix): 2

## Maximum exponent for radix (max_exp): 1024
## Minimum exponent for radix (min_exp): -1021

## Max. exponent power of 10 (max_10_exp): 308
## Min. exponent power of 10 (min_10_exp): -307

## Rounding for addition (rounds): 1