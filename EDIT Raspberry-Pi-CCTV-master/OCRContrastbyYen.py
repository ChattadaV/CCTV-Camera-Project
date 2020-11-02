import os
#output=os.system('python -m pip install -upgrade pip')
output=os.system('python -m pip install -U scikit-image')
#output=os.system('python -m pip install -U scikit-image[***optional***]') #to install optional application


#from skimage.filters import threshold_yen
#from skimage.exposure import rescale_intensity
#from skimage.io import imread, imsave

#img = imread('screenshot.jpg')

#yen_threshold = threshold_yen(img)
#bright = rescale_intensity(img, (0, yen_threshold), (0, 255))

#imsave('screenshotbyyen.jpg')