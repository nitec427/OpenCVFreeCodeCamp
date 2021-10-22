import cv2 as cv

#You can also capture the video by utilizing VideoCapture class

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)
while True:
    truthy , frame = capture.read()
    cv.imshow('Video',frame)
    #Resizing video
    frames_resized = rescaleFrame(frame)
    cv.imshow('Video Resized',frames_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.destroyAllWindows()