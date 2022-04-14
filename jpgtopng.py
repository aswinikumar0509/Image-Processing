from ctypes import resize
from PIL import Image, ImageFilter

img = Image.open('./Image/pikachu.jpg')
filered_img = img.filter(ImageFilter.SMOOTH)
##filered_img = img.convert('L')
resize = filered_img.resize((300,300))
filered_img.save("blur.png",'png')

# Rotating the image
crooked=filered_img.rotate(90)
crooked.save("rot.png",'png')

# Croped the image
box = (100,100,400,400)
region = filered_img.crop(box)
region.save("crop.png",'png')


##filered_img.save("grey.png",'png')




