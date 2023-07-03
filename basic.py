import cv2 as cv

img = cv.imread('Photos/street.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur - Gauss blur method
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade - Canny edge detector
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

cv.waitKey(0)