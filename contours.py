import cv2 as cv
import numpy as np

img = cv.imread('Photos/street.jpg')
cv.imshow('Street', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 1st method - find edges cascades with canny edge detector and findContours
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Detect edges, which is different from 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# 2nd method - binarise the image with cv.threshold and findContours
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# RETR_TREE - all detailed contours, EXTERNAL - external contours, LIST - all contours in image
# CHAIN_APPROX_NONE - contour approximation method, all of them. SIMPLE - compress some of them in one
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0, 255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)