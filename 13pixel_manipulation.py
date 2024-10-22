import cv2

img = cv2.imread("japan.jpg")
print("Shape == ",img.shape)
print("No of Pixels == ",img.size)
print("Datatype == ",img.dtype)
print("Imagetype == ",type(img))
img = cv2.resize(img,(500,300))
cv2.imshow("res",img)

# access a pixel value by its row and column coordinates.
px = img[120,370]
print("The pixel value of that coordinates == ",px)

px = img[120,370,0]
print("The pixel value of blue color == ",px)

px = img[120,370,1]
print("The pixel value of green color == ",px)

px = img[120,370,2]
print("The pixel value of red color == ",px)

cv2.waitKey()
cv2.destroyAllWindows()