import os

#Set the directory path where the text files are located
directory_path = 'countries_1/'

#Set the name of the output file
output_file = 'merged_text.txt'

#create an empty list to store the text from each file
file_text = []

#Loop through each file in the directory
for filename in os.listdir(directory_path):
    #Make sure we're only looking at text files
    if filename.endswith ('.txt'):
        #Open the file and add its text to the list
        with open(directory_path + filename, 'r') as file:
            file_text.append(file.read())

#Merge the text from all the files into one string
merged_text = '\n'.join(file_text)

#Write the merged text to a new file
with open(output_file, 'w') as file:
    file.write(merged_text)