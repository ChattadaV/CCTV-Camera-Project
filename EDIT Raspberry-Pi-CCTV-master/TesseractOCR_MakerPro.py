import cv2 
import pytesseract
from picamera.array import PiRGBArray #for Pi camera module
from picamera import PiCamera #for Pi camera module

#Need to import usb webcam (from Nathan's code)
import PIL
from PIL import Image
#from PIL import ImageTk

#-------The following code is based on https://maker.pro/raspberry-pi/tutorial/optical-character-recognizer-using-raspberry-pi-with-opencv-and-tesseract
#-------Example video: https://www.youtube.com/watch?v=efHYZ-Fcfmw&t=10s


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    
    rawCapture.truncate(0)

    if key == ord("s"):
        text = pytesseract.image_to_string(image)
        print(text)
        cv2.imshow("Frame", image)
        cv2.waitKey(0)
        break

cv2.destroyAllWindows()