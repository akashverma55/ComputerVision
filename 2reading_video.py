import cv2
# for accessing the store video
# cap=cv2.VideoCapture("video.mp4")
# print("cap",cap)

# while True:
#     ret, frame=cap.read()
#     frame=cv2.resize(frame, (700,500)) #for changing the size
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame",frame)
#     cv2.imshow("gray",gray)
#     k=cv2.waitKey(1)
#     if k==ord("k") & 0xff:
#         break
# cap.release()
# cv2.destroyAllWindows()


# for accessing the real-time video

cap=cv2.VideoCapture(0)
print("cap",cap)

# to save the video
video=cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi",video,20,(640,480))# pass 0 for gray video

while cap.isOpened():
    ret, frame=cap.read()
    if ret==True:
        # frame=cv2.resize(frame, (700,500)) #for changing the size
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        k=cv2.waitKey(1)
        if k==ord("k") & 0xff:
            break
cap.release()
output.release()
cv2.destroyAllWindows()