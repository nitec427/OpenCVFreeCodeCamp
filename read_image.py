import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
img_2 = cv.imread('Resources/Photos/cat_large.jpg')

# Image is just a matrix and imread method reat the given matrix.
cv.imshow('Cat' ,img)
cv.imshow("Large Cat",img_2)
cv.waitKey(0)

