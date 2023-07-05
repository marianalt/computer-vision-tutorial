import cv2 as cv
import numpy as np

img = cv.imread('Photos/countryside.jpg')
cv.imshow('Street', img)

b, g, r = cv.split(img)

#is shown gray cause have a shape of one
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)