import numpy as np 
import cv2

cap = cv2.VideoCapture()
cap.open("http://192.168.20.11:8080/stream/video.mjpeg")

# Capture frame-by-frame
ret, frame = cap.read()

# Display the resulting frame
cv2.imwrite('test.jpg',frame)

# When everything done, release the capture
cap.release()

output.write(site.read())
output.close()
