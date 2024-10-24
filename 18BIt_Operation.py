# Bitwise Operator includes and , or, xor, not
# It is most and important and used in various purpose like masking
# and find roi which is in complex shape 

import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1,(150,100),(200,250),(255,255,255),-1)
img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2,(10,10),(170,190),(255,255,255),-1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

bitAND = cv2.bitwise_and(img1,img2)
cv2.imshow("imgAND",bitAND)

bitOR = cv2.bitwise_or(img1,img2)
cv2.imshow("imgOR",bitOR)

bitnot = cv2.bitwise_not(img1)
cv2.imshow("imgnot",bitnot)

bitxor = cv2.bitwise_xor(img1,img2)
cv2.imshow("imgxor",bitxor)

cv2.waitKey()
cv2.destroyAllWindows()