# thresholding are of three types - simple thresholding, adaptive thresholding and advanced thresholding
# simple thresholding(img, pixel_thresh, max_thresh_pixel, style)

import cv2
import numpy as np

img = cv2.imread("Goku.jpg",0)
img = cv2.resize(img,(625,375))

cv2.imshow("img",img)

_, thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
_, thresh3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
_, thresh4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
_, thresh5 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("thresh_image1",thresh1)
cv2.imshow("thresh_image2",thresh2)
cv2.imshow("thresh_image3",thresh3)
cv2.imshow("thresh_image4",thresh4)
cv2.imshow("thresh_image5",thresh5)

cv2.waitKey()
cv2.destroyAllWindows()