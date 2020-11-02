# https://linuxhint.com/install-tesseract-ocr-linux/


import os

#output=os.system('sudo apt install -y imagemagick') #to convert image formats and resize image


output=os.system('tesseract bigsleep.jpg bigsleep.tif')

