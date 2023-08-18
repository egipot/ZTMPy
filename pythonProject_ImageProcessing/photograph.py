# ZTM Section #17 Scripting with Python
# Lesson 211

from PIL import Image, ImageFilter

#img = Image.open('./20150524-DSC_0826.jpg')
#print(img.size)
#new_img = img.resize((400,400))
#new_img.save('smaller.png', 'png') #the aspect ratio is not kept (not the same width and height before the filtering)
#print(new_img.size)

#in order to fix the aspect ratio
img = Image.open('./20150524-DSC_0826.jpg')
img.thumbnail((400,200))
img.save('smallerthumbnail.png', 'png') #results in a thumbnail with kept aspect ratio (despite the provided widthxheight 400,200). The thumbnail function automatically decides which best dimensions to use, based on the current aspect ratio

