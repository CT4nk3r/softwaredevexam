import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import json


def jsopen(filename) -> dict:
    file = open(filename,'r')
    file_contents = json.load(file)
    file.close()
    return file_contents

panel1 = jsopen('Panels_1.json')

p10i = panel1['Panels_1'][0]['Images']
p11i = panel1['Panels_1'][1]['Images']
p12 = panel1['Panels_1'][2]

def color_switch(color_code):
    if color_code == 0:
        return 'Yellow'        
    elif color_code == 2:
        return 'Green'
    elif color_code == 3:
        return 'Blue'
    elif color_code == 4:
        return 'Lime'
    elif color_code == 5:
        return 'Lime'
    elif color_code == 6:
        return 'Lime'
    elif color_code == 7:
        return 'Cyan'
    elif color_code == 8:
        return 'Orange'
    elif color_code == 9:
        return 'Red'
    else:
        return 'Lime'

def drawing(ImageName):
    fig, ax = plt.subplots()
    im = Image.open(ImageName)
    j = 0
    found = False
    while(j < len(p10i) and not found):
        if p10i[j]['ImageName'] == ImageName:
            for i in range(len (p10i[j]['BoundingBoxes'])):
                CenterY = p10i[j]['BoundingBoxes'][i]['CenterY']
                print(p10i[j]['BoundingBoxes'][i]['CenterY'])
                CenterX = p10i[j]['BoundingBoxes'][i]['CenterX']
                print(p10i[j]['BoundingBoxes'][i]['CenterX'])
                Width = p10i[j]['BoundingBoxes'][i]['Width']
                print(p10i[j]['BoundingBoxes'][i]['Width'])
                Height = p10i[j]['BoundingBoxes'][i]['Height']
                print(p10i[j]['BoundingBoxes'][i]['Height'])
                posx = (CenterX*im.width) - ((Width*im.width)/2)
                posy = (CenterY*im.height) - ((Height*im.height)/2)
                color_code = p10i[j]['BoundingBoxes'][i]['ObjectIndex']
                color = color_switch(color_code)
                rect = patches.Rectangle((posx, posy), Width*im.width, Height*im.height, linewidth=1, edgecolor=color, facecolor='none')
                ax.add_patch(rect)
            found = True
        j = j+1
    ax.imshow(im)
    plt.show()

def main():
    ImageName = '1_6.jpg'
    drawing(ImageName)

if __name__ == "__main__":
    main()