import cv2 as cv

# Reading images -------------------------

'''
img = cv.imread('Photos/kitten.jpg')
cv.imshow('kitten', img)
'''

# Reading videos -------------------------

#str or int - path or camera (0/1/2)
# returns pointer
capture = cv.VideoCapture('Videos/dog.mp4')

#use a while loop and read video frame by frame
while True:
    '''
    bool - is frame was successfully read or not
    frame - frame read
    '''
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    #to every frame read, see if 'd' key was pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#if having error -215, the path is probably wrong or there are no frames left to be shown
#basically, there is nothing to be shown (for images or videos)
capture.release()
cv.destroyAllWindows()
