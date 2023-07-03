import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/kelly.mp4')
#capture = cv.VideoCapture('Videos/dog_video.mp4')

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
