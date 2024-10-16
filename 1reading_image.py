import cv2

# Read an image
img1 = cv2.imread('Transformers.jpeg',0) #black and white image
img2 = cv2.imread('Transformers.jpeg',1) #colorful image
img3 = cv2.imread('Transformers.jpeg',-1) #more color contrast
img1 =cv2.resize(img1,(500,500))
img2 =cv2.resize(img2,(500,500))
img3 =cv2.resize(img3,(500,500))
flipimg=cv2.flip(img1,1)
# 1 will flip horizontally, 0 will flip vertically and -1 will flip from both side

# Display the image in a window
cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow('Image3', img3)
cv2.imshow('Image4', flipimg)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
