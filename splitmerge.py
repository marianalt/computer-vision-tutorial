import cv2 as cv
import numpy as np

img = cv.imread('Photos/countryside.jpg')
cv.imshow('Street', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Split an image into its respective color channels
b, g, r = cv.split(img)

# Reconstruct the image to display the actual color involved in that channel
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# #is shown gray cause have a shape of one
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge the color channels back to its original image
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)