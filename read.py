import cv2 as cv

#to read an image, returns the matrix of pixels
img = cv.imread('Photos/kitten.jpg')
#img = cv.imread('Photos/Kitty.jpg')

#to show the matrix of pixels
'''
str - name of the window
var - matrix of pixels to be shown
'''
cv.imshow('kitten', img)
#cv.imshow('Kitty', img)

#waiting a delay seconds or a key to be pressed
cv.waitKey(0)
'''in this case, wait infinitely for a key to be pressed'''
