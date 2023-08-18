# ZTM Section #17 Scripting with Python
# Lesson 212

import sys
import os
from PIL import Image, ImageFilter

#1. grab the first and second argument
source_folder = sys.argv[1]
destination_folder = sys.argv[2]

#2. check if "new/" exists, if not, create it
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    img = Image.open(f'{source_folder}{filename}')
    clean_name = os.path.splitext(filename)[0] #returns atuple ('bulbasaur', '.jpg') so indicate [0] as first item in the tuple
    print(clean_name)
    img.save(f'{destination_folder}{clean_name}.png','png')
    print('all done')


#3. loop through all the 'Pokedex/" and convert images to PNG
#img = Image.open('./')


#4. Save to the new folder

