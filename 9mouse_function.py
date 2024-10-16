import cv2
import numpy as np

def draw(event, x, y, flags, param):
    print("x=",x)
    print("y=",y)
    print("flags=",flags)
    print("param=",param)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (125,0,255), 5)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x,y), (x+100,y+75), (125,125,255),2)

cv2.namedWindow(winname="res")

img = np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == 27: #esc
        break

cv2.destroyAllWindows()