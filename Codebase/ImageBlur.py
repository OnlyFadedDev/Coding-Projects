# File used to blur and save images to cache and pop up on screen.

from PIL import Image, ImageFilter

img = Image.open('C:\Coding Stuff\\bulbasaur.jpg')
filter_img = img.filter(ImageFilter.BLUR)

filter_img.save('blur.png', 'png')

filter_img.show()