import numpy as np 
import cv2

cap = cv2.VideoCapture()
cap.open("http://192.168.20.11:8080/stream/video.mjpeg")

for i in range(25):

    # Capture frame-by-frame
    ret, frame = cap.read()

    resized = cv2.resize(frame, (1280,720))
    cv2.imshow('Frame', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Display the resulting frame
    cv2.imwrite('./data/posSamples/sample' + str(i) + '.jpg',resized)

# When everything done, release the capture
cap.release()

#output.write(site.read())
#output.close()
