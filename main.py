import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open('1_6.jpg')

def drawing():
    pass

fig, ax = plt.subplots()
Width = 0.0310077518
Height = 0.055552192
CenterX = 0.25
CenterY = 0.38377896
posx = (CenterY*im.Height) - (CenterY*im.Height)/2
posy = (CenterX*im.Width)- (CenterX*im.Width/2)
ax.imshow(im)

rect = patches.Rectangle((posx, posy), height*im.height, width*im.width, linewidth=1, edgecolor='r', facecolor='none')

ax.add_patch(rect)

plt.show()