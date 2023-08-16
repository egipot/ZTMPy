import random
import string
import os

countries = ['Philippines', 'Vietnam', 'Poland', 'Bulgaria']

#Create a directory to store the text files
directory = './countries_1'
if not os.path.exists(directory):
    os.makedirs(directory)

#Generate 10 files with random country names
for i in range (1,11):
    #Generate a random country name from the list
    name = random.choice(countries)
    #Geneaate a random filename
    filename = f'{directory}/file{i}.txt'
    #Create and write the name to the file
    with open(filename, 'w') as file:
        file.write(name)

