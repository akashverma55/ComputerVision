import cv2

camera = "http://192.168.110.223:8080/video"

cap = cv2.VideoCapture(0)
cap.open(camera)
print("check==",cap.isOpened())

# to save the video
video=cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("out.mp4",video,20,(640,480))# pass 0 for gray video

while cap.isOpened():
    ret, frame=cap.read()
    if ret==True:
        frame=cv2.resize(frame, (800,500)) #for changing the size
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        # cv2.imshow("gray",gray)
        output.write(frame)
        k=cv2.waitKey(1)
        if k==ord("k") & 0xff:
            break
cap.release()
output.release()
cv2.destroyAllWindows()