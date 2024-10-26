# Simple thresholding not able to handle different type of low luminous pixels
# this algorithm calculate the threshold for a small regions of the image so that we get multiple threshold for different region in same place 

# there are two types of adaptive thresholding value in calculated
# cv2.ADAPTIVE_THRESH_MEAN_C
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C

# threshold(img,pixel_thres,_max_pixel_thres,method,style,no_of_pixels,contact_mean)

import cv2 
import numpy as np

img = cv2.imread("Goku.jpg",0)
img = cv2.resize(img,(500,300))
_,thres1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thres3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("img",img)
cv2.imshow("img1",thres1)
cv2.imshow("img2",thres2)
cv2.imshow("img3",thres3)
cv2.waitKey()
cv2.destroyAllWindows()