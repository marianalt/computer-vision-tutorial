import cv2 as cv

img = cv.imread('Photos/street.jpg')

cv.imshow('Street', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Detect edges, which is different from 
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny Edges', canny)

# RETR_TREE - all detailed contours, EXTERNAL - external contours, LIST - all contours in image
# CHAIN_APPROX_NONE - contour approximation method, all of them. SIMPLE - compress some of them in one
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)