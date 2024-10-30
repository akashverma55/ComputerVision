# morphological transformations are some operations based on the image shape
# It is normally performed on binary images.
# It needs two inputs, 1)original image 2)Structuring elements
# Two more basics Morphological Transformations are
# 1) Opening 2) Closing

import cv2
import numpy as np

img = cv2.imread("color.jpeg",0)

# Opening---------
# Opening is just another name of erosion followed by dilation.
# means first erosion take place then dilation
_,mask = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)


cv2.imshow("img",img)
cv2.imshow("kernel",kernel)
cv2.imshow("mask",mask)
cv2.imshow("opening",o)

# Closing--------
# It is opposite of opening 
# Closing is just another name of dilation followed by erosion.
# Means first dilation take place then erosion
kernel = np.ones((3,3),np.uint8)
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing",c)


# -------Optional----------
x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)  #diff b/w mask and opening 
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #diff b/w dilation and erosion
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel) #diff b/w the closing of the input image and input image 
cv2.imshow("x1",x1)
cv2.imshow("x2",x2)
cv2.imshow("x3",x3)

cv2.waitKey()
cv2.destroyAllWindows()