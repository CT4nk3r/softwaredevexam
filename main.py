import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def drawing(ImageName, Width, Height, CenterX, CenterY):
    fig, ax = plt.subplots()
    im = Image.open(ImageName)
    posx = (CenterY*im.height) - (CenterY*im.height)/2
    posy = (CenterX*im.width)- (CenterX*im.width/2)
    ax.imshow(im)
    rect = patches.Rectangle((posx, posy), Height*im.height, Width*im.width, linewidth=1, edgecolor='Green', facecolor='none')
    ax.add_patch(rect)
    plt.show()

def main():
    ImageName = '1_6.jpg'
    Width = 0.0310077518
    Height = 0.055552192
    CenterX = 0.25
    CenterY = 0.38377896
    drawing(ImageName, Width, Height, CenterX, CenterY)

if __name__ == "__main__":
    main()