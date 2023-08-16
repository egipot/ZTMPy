my_File = open('test185.py')

#print(my_File.read())   #OUTPUT: print('hellowieee')
#these lines 5 and 6 are not run becuase reading is done only once
#print(my_File.read())
#print(my_File.read())

#to resolve:
#my_File.seek(0)
#print(my_File.read())   #OUTPUT: print('hellowieee')
#my_File.seek(0)
#print(my_File.read())   #OUTPUT: print('hellowieee')

my_File2 = open('test185.txt')
#print(my_File2.readline())
#print(my_File2.readline())
#print(my_File2.readline())
print(my_File2.readlines())

#need to close the file, so that it can be read in another part of the program
my_File.close()
my_File2.close()