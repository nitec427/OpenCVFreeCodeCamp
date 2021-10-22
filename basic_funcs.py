import cv2 as cv
img = cv.imread('Resources/Photos/park.jpg')
# cv.imshow('Cat',img)

# Convert to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)


# Blurring an image may reduce the effect of faults in a photo

blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Canny image helps us to find contours in an image

canny = cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)

#Dilating the image
dilated  = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("dilated",dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("eroded",eroded)

#Resizing
resized  = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)