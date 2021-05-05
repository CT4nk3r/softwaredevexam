import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import json


def jsopen(filename) -> dict:
    file = open(filename,'r')
    file_contents = json.load(file)#dictionary-t készít belőle miután betölti a fájl adatait
    file.close()
    return file_contents


panel1 = jsopen('Panels_1.json')

p10i = panel1['Panels_1'][0]['Images']
p11i = panel1['Panels_1'][1]['Images']
p12 = panel1['Panels_1'][2]

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
                rect = patches.Rectangle((posx, posy), Width*im.width, Height*im.height, linewidth=1, edgecolor='Green', facecolor='none')
                ax.add_patch(rect)
            found = True
        j = j+1
    ax.imshow(im)
    plt.show()

def main():
    ImageName = ''
    drawing(ImageName)

if __name__ == "__main__":
    main()