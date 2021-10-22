import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat',img)
waitKey = cv.waitKey
def rescaleFrame(frame, scale=.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

waitKey(0)