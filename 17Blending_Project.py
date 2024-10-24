import cv2
import numpy as np

img1 = cv2.imread("japan.jpg")
img1 = cv2.resize(img1,(750,450))

img2 = cv2.imread("Goku.jpg")
img2 = cv2.resize(img2,(750,450))

cv2.imshow("Img1",img1)
cv2.imshow("Img2",img2)

def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow("win")
cv2.createTrackbar("Blending","win",1,100,blend)
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch,"win",0,1,blend)
cv2.createTrackbar("Alpha","win",0,100,blend)

while True:
    s = cv2.getTrackbarPos(switch,"win")
    b = cv2.getTrackbarPos("Blending","win")
    a = cv2.getTrackbarPos("Alpha","win")
    n = float(b/100)
    print(n)

    if s==0:
        dst = img[:]

    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,a)
        cv2.putText(dst,str(b),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)

    cv2.imshow("win",dst)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

cv2.waitKey()
cv2.destroyAllWindows()