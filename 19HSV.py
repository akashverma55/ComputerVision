import cv2
import numpy as np

img = cv2.imread("OIP.jpeg")

while True:
    # hue, saturation, value
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    upper = np.array([130,225,225])
    lower = np.array([110,50,50])
    # creating mask
    mask = cv2.inRange(hsv,lower,upper)
    # Filter mask from image with bitwise operation
    res = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("IMG",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Res",res)

    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()