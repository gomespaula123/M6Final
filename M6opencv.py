import cv2
import numpy as np


# Turn on the camera
video_capture = cv2.VideoCapture(0)

while True:
    # Determine the spotting range of RED
    lower_range = np.array([120, 100, 240])
    upper_range = np.array([190, 160, 255])

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    bgr = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Filter out from the capture the RED object
    paperThing = cv2.inRange(bgr, lower_range, upper_range)

    # Determine if there is indeed an object in the image
    hight = int(format(paperThing.shape[0]))
    width = int(format(paperThing.shape[1]))
    whiteness = 0
    for i in range(hight - 1):
        for j in range(width - 1):
            if paperThing[i, j] > 200:
                whiteness = whiteness + 1
    if whiteness >= hight * width / 10:
        # Object confirmed
        print('RED!!!')
    # Display the resulting captures
    cv2.imshow('Paper thing', paperThing)
    cv2.imshow('THE EYE', frame)

    # Waits for next frame
    cv2.waitKey(200)