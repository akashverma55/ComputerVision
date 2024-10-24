# BLending means adding two images
# if you want to blend two images then both should have the same size

import cv2
import numpy as np

img1 = cv2.imread("Goku.jpg")
img1 = cv2.resize(img1,(750,450))

img2 = cv2.imread("japan.jpg")
img2 = cv2.resize(img2,(750,450))

cv2.imshow("Img1",img1)
cv2.imshow("Img2",img2)

# Simple Blending
simple_combined_image = img1 + img2
cv2.imshow("Simple_Image",simple_combined_image)

# Recommeded Blending but cant be controlled by hypertuning 
result = cv2.add(img1,img2)
cv2.imshow("Combined_Image",result)

result1 = cv2.addWeighted(img1,0.7,img2,0.3,100)
cv2.imshow("Combined_Weighted_Image",result1)
# Addweight which can be controlled

cv2.waitKey()
cv2.destroyAllWindows()