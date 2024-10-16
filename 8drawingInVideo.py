import cv2
import datetime

cap = cv2.VideoCapture("video.mp4")
print("for width ===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height ===",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("for width ===",cap.get(3))
print("for height ===",cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.resize(frame,(1000,600))
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = "Height: " + str (cap.get(4)) + " Width: " + str(cap.get(3))
        frame = cv2.putText(frame,text,(20,50), font,1,(0,155,255),1,cv2.LINE_AA)
        date_time = "Date: "+str(datetime.datetime.now())
        frame = cv2.putText(frame, date_time, (20, 80), font, 1, (100, 125, 255), 1, cv2.LINE_AA)
        frame = cv2.rectangle(frame, (100,100), (200,150), (85,192,54),-1)
        cv2.imshow("frame",frame)

        if cv2.waitKey(1) & 0xff == ord("k"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()