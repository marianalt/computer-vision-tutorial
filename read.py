import cv2 as cv

#to read an image, returns the matrix of pixels
img = cv.imread('Photos/kitten.jpg')

#to show the matrix of pixels
'''
str - name of the window
var - matrix of pixels to be shown
'''
cv.imshow('kitten', img)

#waiting a delay seconds or a key to be pressed
'''in this case, wait 0 seconds, so wait infinitely for a key to be pressed'''
cv.waitKey(0)
