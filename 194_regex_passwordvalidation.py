#password checker
# at least 8 char long
# contain any letters, numbers, and only these special characters $ % # @
# has to end with a number

import re

password = input("Enter the password: ")
pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}\d")
check = pattern.fullmatch(password)
print(check)              #prints <re.Match object; span=(0, 10), match='asdfqwer#2'>

if check:
    print("Accepted")
    print(check.group())  #prints the <match> based on the result : "<re.Match object; span=(0, 10), match='asdfqwer#2'>"
else: 
    print("Denied")
#print(check)
#print(check.group())

print(re.match(pattern, password))      # <re.Match object; span=(0, 10), match='asdfqwer#3'>
print(re.fullmatch(pattern, password))  # <re.Match object; span=(0, 10), match='asdfqwer#3'>

