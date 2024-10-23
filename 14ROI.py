import cv2

img = cv2.imread("Goku.jpg")
img = cv2.resize(img,(750,450))

cv2.imshow("img",img)

# ROI(Region of interest)
# (320,50)(440,200)
# y = 150,x = 120
roi = img[50:200,320:440]
cv2.imshow("roi",roi)

# now passing data in image
img[50:200,441:561] = roi
img[50:200,199:319] = roi
cv2.imshow("img_updated",img)


img1 = cv2.imread("Tanjiro.jpg")
img1 = cv2.resize(img1,(750,450))
# Assuming your image is loaded in a variable called 'img1' and ROI in 'roi'
target_height, target_width, channels = img1[1:156, 560:860].shape

# Resize ROI to match target area
resized_roi = cv2.resize(roi, (target_width, target_height))

# Now insert the resized ROI into the image
img1[1:156, 560:860] = resized_roi

cv2.imshow("img_on_img",img1)


cv2.waitKey()
cv2.destroyAllWindows()