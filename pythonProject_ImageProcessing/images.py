# ZTM Section #17 Scripting with Python
# Lesson 210

from PIL import Image, ImageFilter
#NOTE: PNG supports the filter image functions, so error might be raised when image is kept in JPG format

img = Image.open('./smooth.png')
#print(img)

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png")

