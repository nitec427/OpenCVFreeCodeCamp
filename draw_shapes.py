import cv2 as cv
import numpy as np

# width, height and the color channel
blank_img = np.zeros((500,500,3), dtype= 'uint8')
blank_img[:] = [2,102,242]
# cv.imshow('Blank', blank_img)

blank_img[100:400, 200:500] = [15, 45, 167]
# cv.imshow('Second', blank_img)


# Drawing a rectangle into an image
cv.rectangle(blank_img, (0, 0), (blank_img.shape[0] // 2, blank_img.shape[1] // 2), (0,255,0), cv.FILLED)
cv.imshow('Rectangle', blank_img)

# Drawing a circle

cv.circle(blank_img, (blank_img.shape[0] // 2, blank_img.shape[1] // 2), blank_img.shape[0] // 20, (255, 255,0), cv.FILLED)

cv.imshow('Circle Added',blank_img)

# Draw a line
# For lines (location, point1, point2, (color3), thickness)
cv.line(blank_img, (100, 250), (300, 400), (100,100,200), cv.FILLED)
cv.imshow(blank_img)

# Write text
cv.putText(blank_img, 'Hello! My name is Jason!!', (0,225),cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0))
cv.waitKey(0)