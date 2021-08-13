!pip install opencv-python

import cv2
import numpy as np
import urllib.request
  
# first image 
urllib.request.urlretrieve('https://static.wikia.nocookie.net/motu-patlu/images/3/3e/Profile_motu2.png',"motu.png")
motu=cv2.imread('motu.png')
cv2.imshow('motu',motu)
cv2.waitKey()
cv2.destroyAllWindows()

# second image
urllib.request.urlretrieve('https://static.wikia.nocookie.net/motu-patlu/images/9/98/Profile_patlu.png', "patlu.png")
patlu=cv2.imread('patlu.png')
cv2.imshow('patlu',patlu)
cv2.waitKey()
cv2.destroyAllWindows()


#resizing the images
m = cv2.resize(motu, (300,400))
p = cv2.resize(patlu,(300,400))

#concat the images
mp = cv2.hconcat([m, p])


cv2.imshow('Motu aur Patlu ki Jodiii',mp)
cv2.waitKey()
cv2.destroyAllWindows()


