#standard way to read a file without the need to close it:
with open('test185.txt') as my_file:
    print(my_file.readlines()) #['hello, my name is what?\n', 'slim shady\n', ':D']


#default of mode = read; otherwise, specify the mode e.g. 'r+' to open the file for updating/writing 
with open('test185.txt', mode = 'w') as my_file_rw:
    text = my_file_rw.write(":)")
    #print(my_file_rw.readlines()) 
    #output is visible in test185.py 
    #hello, my name is what?
    #slim shady
    #:D
    #hey it's me  --> this line is added with line break as stated in the write command (line8)

    #mode = 'w' write is overwriting the all file!

#creating a new text file
with open('sad.txt', mode = 'w') as my_file_w:
    text_sad = my_file_w.write(':(')
    print(text_sad)

