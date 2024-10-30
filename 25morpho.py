# ----------------------------Morphological Transformation-----------------------------

# morphological transformation are same simple operations based on the image shape 
# mnormally performed in binary images
# It needs two inputs - original image and Structuring element(kernel)
# Two basic morphological transformations are : 1.Erosion and 2.Dilation
# for there should be always a binary inverse image

import numpy as np
import cv2

# Erosion -------
# it erodes away the boundries of foreground object
# kernel slides through all the image and all the pixel
# from the original image conside 1 only if kernel's pixel is 1

img = cv2.imread('colorballs.jpeg',0)
img = cv2.resize(img,(500,400))
_,mask = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8) #5x5 kernel with full of ones
e = cv2.erode(mask,kernel)


#  Dilation----------
# It is just opposite of erosion
# here, apixel element is 'l' if atleast one pixel under the kernel is '1'
# so it inc. the white region in the image or size of foreground object in .
# normally, in cases like noise removal, erosion is following by dilation.
# Because, erosion removes white noises, but is also shrink our object.

kernel = np.ones((3,3),np.uint8)
d = cv2.dilate(mask,kernel)
cv2.imshow("dilation",d)

cv2.imshow("img", img)
# cv2.imshow("kernel", kernel)
cv2.imshow("mask", mask)
cv2.imshow("erosion", e)

cv2.waitKey()
cv2.destroyAllWindows()


from matplotlib import pyplot as plt
titles = ['img','mask','erosion','dilation']
images = ['img','mask','e','d']
for i in range(4):
    plt.subplot(2,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()