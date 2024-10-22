import cv2
import numpy as np

img = cv2.imread("Tanjiro.jpg")
print("Shape == ",img.shape)
print("No of Pixels == ",img.size)
print("Datatype == ",img.dtype)
print("Imagetype == ",type(img))
img = cv2.resize(img,(600,400))

# this method split this image into three color channels blue, green and red
b, g, r =cv2.split(img)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

cv2.imshow("original",img)

mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)

mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)

mr3 = cv2.merge((g,r,b))
cv2.imshow("grb",mr3)

cv2.waitKey(0)
cv2.destroyAllWindows()