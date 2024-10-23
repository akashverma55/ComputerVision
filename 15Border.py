import cv2

img = cv2.imread("Goku.jpg")
img = cv2.resize(img,(750,450))

border = cv2.copyMakeBorder(img,10,10,5,5,cv2.BORDER_CONSTANT,value=[255,0,125])
#border width = top, bottom, right, left 

cv2.imshow("img",border)
cv2.waitKey()
cv2.destroyAllWindows()