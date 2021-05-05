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
Panels = p10i + p11i
p12 = panel1['Panels_1'][2]

def color_switch(color_code):
    if color_code == 0:
        # "Name": "Examined are"
        return 'Yellow'  
    if color_code == 1:
        # "Name": "Micro crack"
        return 'Green'      
    elif color_code == 2:
        #"Name": "Crack"
        return 'Blue'
    elif color_code == 3:
        #"Name": "Short circuit cell"
        return 'Blue'
    elif color_code == 4:
        #"Name": "Contamination"
        return 'Lime'
    elif color_code == 5:
        #"Name": "Dark spot"
        return 'Lime'
    elif color_code == 6:
        #"Name": "Unknown  error"
        return 'Lime'
    elif color_code == 7:
        #"Name": "Scratch"
        return 'Lime'
    elif color_code == 8:
        #"Name": "Low power cell"
        return 'Orange'
    elif color_code == 9:
        #"Name": "Short circuit string"
        return 'Red'
    else:
        return 'Magenta'

def drawing(ImageName):
    fig, ax = plt.subplots()
    im = Image.open(ImageName)
    j = 0
    found = False
    while(j < len(Panels) and not found):
        if Panels[j]['ImageName'] == ImageName:
            for i in range(len (Panels[j]['BoundingBoxes'])):
                CenterY = Panels[j]['BoundingBoxes'][i]['CenterY']
                print(Panels[j]['BoundingBoxes'][i]['CenterY'])
                CenterX = Panels[j]['BoundingBoxes'][i]['CenterX']
                print(Panels[j]['BoundingBoxes'][i]['CenterX'])
                Width = Panels[j]['BoundingBoxes'][i]['Width']
                print(Panels[j]['BoundingBoxes'][i]['Width'])
                Height = Panels[j]['BoundingBoxes'][i]['Height']
                print(Panels[j]['BoundingBoxes'][i]['Height'])
                posx = (CenterX*im.width) - ((Width*im.width)/2)
                posy = (CenterY*im.height) - ((Height*im.height)/2)
                color_code = Panels[j]['BoundingBoxes'][i]['ObjectIndex']
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