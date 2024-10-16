import cv2
from pytube import YouTube

# Replace 'your_video_url' with the actual URL of the YouTube video
url = 'https://www.youtube.com/watch?v=2PNRREdTuK4'

# Create a YouTube object
yt = YouTube(url)

# Get the highest resolution stream (adjust format if needed)
stream = yt.streams.get_highest_resolution()

# Download the video
video_path = stream.download()

# Open the downloaded video using OpenCV
cap = cv2.VideoCapture(video_path)

# Process the video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame here (e.g., resize, apply filters, detect objects)
    # ...

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()