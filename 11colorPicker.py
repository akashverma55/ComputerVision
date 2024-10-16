import cv2
import numpy as np

def cross(x):
    pass

# blank image
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Color_Picker")

# create switch
switch = "0:OFF\n1:ON"
cv2.createTrackbar(switch,"Color_Picker",0,1,cross)

# creating bar for rgb
cv2.createTrackbar("R","Color_Picker",0,255,cross)
cv2.createTrackbar("G","Color_Picker",0,255,cross)
cv2.createTrackbar("B","Color_Picker",0,255,cross)

while True:
    cv2.imshow("Color_Picker",img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

    # trackbar pos
    s = cv2.getTrackbarPos(switch,"Color_Picker")
    r = cv2.getTrackbarPos("R","Color_Picker")
    g = cv2.getTrackbarPos("G","Color_Picker")
    b = cv2.getTrackbarPos("B","Color_Picker")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()