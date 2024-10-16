import cv2 as c
# for screen recording
import pyautogui as p
import numpy as np #for creating the array of image

import moviepy.editor as mp

rs = p.size()

file_name = input("Please enter any file name and path:")
frame_rate = 60.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(file_name, fourcc, frame_rate, rs)

c.namedWindow("Live Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live Recording",(600,400))

while True:
    img = p.screenshot()
    frame = np.array(img)
    frame = c.cvtColor(frame, c.COLOR_BGR2RGB)
    output.write(frame)
    c.imshow("Live Recording",frame)
    k=c.waitKey(1)
    if k==ord("k") & 0xff:
            break

output.release()
c.destroyAllWindows()