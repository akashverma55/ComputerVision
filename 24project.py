import cv2
import numpy as np
 
img1 = cv2.imread("japan.jpg")
img2 = cv2.imread("Goku.jpg")
img1 = cv2.resize(img1,(750,450))
img2 = cv2.resize(img2,(450,450))

r,c,ch = img2.shape
print(r,c,ch)

roi = img1[0:r,0:c]

img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(img_gry,80,255,cv2.THRESH_BINARY)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
thres3 = cv2.adaptiveThreshold(img_gry,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# removing background
mask_inv =  cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
result = cv2.add(img2_fg,img1_bg)
# cv2.imshow("japan",img1)
# cv2.imshow("Goku",img2)
# cv2.imshow("roi",roi)
# cv2.imshow("gray image",img_gry)
# cv2.imshow("binary image",mask)
cv2.imshow("binary_image",img2_fg)
cv2.imshow("Inverse image",mask_inv)
cv2.imshow("Combined Image",img1_bg)
cv2.imshow("Resulted Image",result)

final = img1
final[0:r,0:c] = result
cv2.imshow("Final Image",final)
cv2.waitKey()
cv2.destroyAllWindows()