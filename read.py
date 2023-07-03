import cv2 as cv

# Reading images -------------------------
'''
img = cv.imread('Photos/kitten.jpg')
cv.imshow('kitten', img)
'''

# Reading videos -------------------------
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    #see if 'd' key was pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
