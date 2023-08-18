# ZTM Section #17 Scripting with Python
# Lesson 210

from PIL import Image, ImageFilter

img = Image.open('./Pokedex_me/pikachu.jpg')
filtered_img = img.convert('L')
crooked = filtered_img.rotate(90)
resized = crooked.resize((300, 300)) #resize accepts tuple ((x,x)), note the parenthesis
resized.save("grey3.png", 'png')
resized.show()
#NOTE that for multiple filtering commands, different variables are used, e.g. filtered_img --> crooked --> resized


