import cv2 as cv

img = cv.imread('Photos/street.jpg')
cv.imshow('Cat', img)

# # Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Blur - Gauss blur method
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge Cascade - Canny edge detector
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# # Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# # Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) #useful to shrink image
cv.imshow('Resized', resized)

cv.waitKey(0)