import numpy as np
import cv2 
from cv2 import waitKey

# img = np.zeroes([512,512,3], np.unit8)*255 #for black image
# img = np.ones([512,512,3], np.unit8)*255 #for black image
img = cv2.imread("E:\All Model Implementation\machine learning\ComputerVision\Transformers.jpeg")
img = cv2.resize(img,(600,600))
img = cv2.line(img, (0,0), (200,200), (154,92,424),8) #color format is bgr
img = cv2.arrowedLine(img, (0,0), (400,500), (15,92,44),8)
img = cv2.rectangle(img, (100,100), (200,150), (85,192,54),-1)
#(img)(x1,y1)(x2,y2)(color)(thickness) 

font =cv2.FONT_ITALIC
img = cv2.putText(img, "Transformer", (200, 500), font, 1, (85, 192, 54), 4, cv2.LINE_AA)

cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()