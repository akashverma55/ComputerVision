import cv2
import numpy as np

img = cv2.imread("Star.jpg")
img = cv2.resize(img,(750,450))

def nothing(x):
    pass

cv2.namedWindow("Color_Adjustments")

cv2.createTrackbar("Lower_H","Color_Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_S","Color_Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V","Color_Adjustments",0,255,nothing)

cv2.createTrackbar("Upper_H","Color_Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_S","Color_Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_V","Color_Adjustments",255,255,nothing)

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("Lower_H","Color_Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S","Color_Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V","Color_Adjustments")

    u_h = cv2.getTrackbarPos("Upper_H","Color_Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S","Color_Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V","Color_Adjustments")

    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,lower_bound,upper_bound)
    res = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("IMG",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Res",res)

    k=cv2.waitKey(1)
    if k==27:
        break

cv2.destroyAllWindows()