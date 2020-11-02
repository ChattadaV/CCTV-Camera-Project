# https://pysource.com/2020/04/23/text-recognition-ocr-with-tesseract-and-opencv/

#import os

#output=os.system('sudo apt install tesseract-ocr')
#output=os.system('sudo apt install libtesseract-dev')
###########output=os.system('sudo port install tesseract') #For Mac user only
#output=os.system('pip install pytesseract')
#output=os.system('pip3 install pytesseract')




import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/home/pi/.local/lib/python3.7/site-packages/pytesseract/pytesseract.py"
#^^^^^^^^^Need to find location of tesserract files on linux



img = cv2.imread('bigsleep.jpg')
    
text = pytesseract.image_to_string(img)
print(text)
cv2.imshow("Frame", image)
cv2.waitKey(0)

