# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. 
# This will reveal an image!

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

#egi solution: /*
#print(len(picture)) #6
#print(len(picture[0])) #7

row = 0
col = 0
gui = []
for row in range (0,len(picture),1):
    for col in range (0,len(picture[row]),1):
        current_element = picture[row][col]
    
        if current_element == 0:
            print(' ', end ='')
        else:
            print('*', end = '')
#        col += 1
#    row += 1
    print('\n', end = '')
# */

#andrei solution:
for image in picture:
  for pixel in image:
    if (pixel):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')