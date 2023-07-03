import cv2 as cv
import numpy as np

#uint8 -> datatype of images basically
#width, height, nº of color channels
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color - RGB => BGR
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
#same as: 
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a Line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

cv.waitKey(0)