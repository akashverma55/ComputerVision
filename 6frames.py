import cv2
import os

video_path = "E:\\All Model Implementation\\machine learning\\ComputerVision\\video.mp4"
frame_dir = "E:\\All Model Implementation\\machine learning\\ComputerVision\\frames"

vidcap = cv2.VideoCapture(video_path)
count = 0

while True:
    success, image = vidcap.read()
    if not success:
        break
    filename = os.path.join(frame_dir, f"img_{count}.jpg")
    cv2.imwrite(filename, image)
    count += 1

vidcap.release()
cv2.destroyAllWindows()
