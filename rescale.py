import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3,width)
    capture.set(4,height)
    #brightness, 10

capture = cv.VideoCapture('Videos/kelly.mp4')

img = cv.imread('Photos/Kitty.jpg')
rescaled_img = rescaleFrame(img, scale=0.25)
cv.imshow('Kitty larger image', img)
cv.imshow('Kitty', rescaled_img)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.1)
    #frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)
    
    #see if 'd' key was pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
#cv.destroyAllWindows() or remove it
