import os
from PIL import Image
def imagemanip():
    image_size=300
    logo='catlogo.png'
    logoimobj=Image.open(logo).resize((50,47))
    image_list=os.listdir()
    for img in image_list:
        if not(img.endswith('.png') or img.endswith('.jpg')) or img==logo:
            continue
        image=Image.open(img)
        width,height=image.size
        if width>image_size and height>image_size:
            if width>height:
                height=int((image_size/width)*height)
                width=image_size
            else:
                width=int((image_size/height)*width)
                height=image_size
            print(width,height)
            print('resizing %s ...'%img)
            image=image.resize((width,height))
        print('adding logo to %s'%img)
        image.paste(logoimobj,(width-50,height-47),logoimobj)
        image.save(img)