import numpy as np
import cv2 as  cv
from matplotlib import pyplot as plt

img = np.zeros((200,200), np.uint8)

w_img = img.shape[0]
h_img = img.shape[1]
cv.rectangle(img,(w_img // 2, 0),(w_img,h_img),(255),-1)

cv.imshow("Image", img)

plt.hist(img.ravel(), 256, [0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()