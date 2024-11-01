#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.
#It is use  multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
# 1) -  NOise reduction(gauss)), 2) -Gradient calculation( ,
# 3) - Non-maximum suppresson, 4) - Double Threshold,
# 5) - Edge Tracking by Hysteresis 

import cv2
import numpy as np

import cv2
import numpy as np

img = cv2.imread("volleyball.jpeg",0)
# img = cv2.resize(img,(500,300))
cv2.imshow("img",img)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold","Canny",0,255,nothing)
while True:
    a = cv2.getTrackbarPos("Threshold","Canny")
    res = cv2.Canny(img,a,255)
    cv2.imshow("Canny",res)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

#parameter(img,thres1,thres2)
# canny = cv2.Canny(img,50,150)
# cv2.imshow("Canny",canny) 

# cv2.waitKey()
cv2.destroyAllWindows()