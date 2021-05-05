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
panel3 = jsopen('Panels_3.json')
p30i = panel3['Panels_3'][0]['Images']
p31i = panel3['Panels_3'][1]['Images']
panel6 = jsopen('Panels_6.json')
p60i = panel6['Panels_6'][0]['Images']
p61i = panel6['Panels_6'][1]['Images']
Panels = p10i + p11i + p30i + p31i +  p60i + p61i

errors = panel1['Panels_1'][2]

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
    Menu()

def imageChooser():
    option = int(input('Which file would you like to open(use numbers): '))

    if option == 1:
        return '1_6.jpg'
 
    elif option == 2:
        return '7_12.jpg'
 
    elif option == 3:
        return '110.jpg'
 
    elif option == 4:
        return '361_366_D211AABB3A20200005.jpg'

    else:
        print("Incorrect option")
        Menu()

def Menu():
    print("1. 1_6.jpg")
    print("2. 7_12.jpg")
    print("3. 110.jpg")
    print("4. 361_366_D211AABB3A20200005.jpg")
    ImageName = imageChooser()
    drawing(ImageName)

def main():
    Menu()

if __name__ == "__main__":
    main()