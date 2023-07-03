import cv2 as cv
import numpy as np

#uint8 -> datatype of images basically
#width, height, nº of color channels
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. paint the image a certain color - RGB => BGR
blank[:] = 0,255,0
cv.imshow('Green', blank)
blank[:] = 0,0,255
cv.imshow('Red', blank)
blank[:] = 255,0,0
cv.imshow('Blue', blank)

cv.waitKey(0)