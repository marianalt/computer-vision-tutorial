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
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (800,800), interpolation=cv.INTER_CUBIC) #useful to scale the image, slowest but has more quality
cv.imshow('Resized', resized)

# Cropping - array slicing
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)