# ZTM Section #17 Scripting with Python
# Lesson 210

from PIL import Image, ImageFilter

img = Image.open('./Pokedex_me/pikachu.jpg')
filtered_img = img.convert('L')
box = (100,100,400,400)
region = filtered_img.crop(box)

region.save("grey4.png", 'png')
region.show()
#NOTE that for multiple filtering commands, different variables are used, e.g. filtered_img --> crooked --> resized


