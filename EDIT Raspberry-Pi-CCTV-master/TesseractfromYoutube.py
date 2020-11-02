#----------From Youtube: https://youtube.com/watch?v=kxHp5ng6Rgw

import cv2
import PIL
from PIL import Image #from Python Imaging Libraries, import Image
import pytesseract #import image_to_text program
import numpy as np

#thresholding
img = Image.open("/home/pi/Downloads/image.jpg") #Directory of image file to extract text from
thresh = 130
fn = lambda x : 255 if x > thresh else 0
img = img.convert('L').point(fn, mode='1') #
#img = img.convert('1')
img.save('/home/pi/Downloads/image_black.jpg')

#img = Image.open('screenshot_grey.jpg')

text = pytesseract.image_to_string(img, lang="eng") #use pytesseract to extract text in form of string, english langauge
print(text)


#----****--- Need to compile to make it automatic (if, elif, else) with buttons GUI

