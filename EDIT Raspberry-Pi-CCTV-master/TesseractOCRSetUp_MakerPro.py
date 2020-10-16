import os


#-------The following code is based on https://maker.pro/raspberry-pi/tutorial/optical-character-recognizer-using-raspberry-pi-with-opencv-and-tesseract
#_______Example video: https://www.youtube.com/watch?v=efHYZ-Fcfmw&t=10s

#output=os.system('sudo apt -y autoremove') #use this command to clear any leftover dependencies
output=os.system('sudo apt-get -y update') #update the installed packages on your Raspberry Pi to the latest versions
output=os.system('sudo apt-get -y upgrade') #update the installed packages on your Raspberry Pi to the latest versions
output=os.system('sudo apt install libatlas3-base libsz2 libharfbuzz0b libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4') #install the required packages for OpenCV on your Raspberry Pi:
output=os.system('sudo pip3 install opencv-contrib-python libwebp6') #install OpenCV 3 for Python 3 on your Raspberry Pi. 
output=os.system('sudo apt install tesseract-ocr') #install the Tesseract library by typing
output=os.system('sudo apt install libtesseract-dev') #Install the command line Tesseract tool
output=os.system('sudo pip install pytesseract') #install Python wrapper for Tesseract

#to check if OpenCV is installed or not, type the following into shell: import cv2 [hit enter]
#to check if OpenCV is installed or not, type the following into terminal: python3 [hit enter] import cv2
#to check OpenCV version, type the following into shell/terminal: cv2.__version__
#to check tesseract's installation, type the following into shell/terminal: import pytesseract
#to check tesseract's installation, type the following into shell/terminal: tesseract --version

