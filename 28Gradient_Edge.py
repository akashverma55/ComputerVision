#Image Gradient--
#It is a directional change in the color or intensity in an image.
#It is most important part to find inormation from image
#Like finding edges within the images.
#There are various methods to find image gradient.
#These are - Laplacian Derivatives,SobelX and SobelY.
#All these functions have diff. mathematical approach to get result.
#All load image in the gray scale

import cv2
import numpy as np

img = cv2.imread("volleyball.jpeg",0)
# img = cv2.resize(img,(500,300))
cv2.imshow("img",img)

# image should be gray scale
# Laplacian derivatives- Laplacian formula
# parameters(img, data_type for -ve value, ksize)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=1)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian",lap)

#Sobel operation - 
# is a joint Gausssian smoothing plus differentiation operation, 
#so it is more  resistant to noise
#This is use for x and y bth
#parameter (img,type for -ve val,x = 1,y = 0,ksize)
#Sobel X focus on vertical lines
#Sobel y focus on horizontal lines
sobelX = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
cv2.imshow("SobelX",sobelX)
cv2.imshow("SobelY",sobelY)

# combining the sobelX and sobelY
sobel_combine = cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("sobel_combine",sobel_combine)
sobel_combine_and = cv2.bitwise_and(sobelX,sobelY)
cv2.imshow("sobel_combine_x",sobel_combine_and)

cv2.waitKey()
cv2.destroyAllWindows()