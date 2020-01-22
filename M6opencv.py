import cv2
import numpy as np

# Set up the detector with default parameters.

video_capture = cv2.VideoCapture(0)

while True:
    detector = cv2.SimpleBlobDetector()
    lower_range = np.array([120, 100, 240])
    upper_range = np.array([190, 160, 255])
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    bgr = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    paperThing = cv2.inRange(bgr, lower_range, upper_range)

    # Detect blobs.
    keypoints = detector.detect(paperThing)

    cv2.waitKey(2)
    # Display the resulting frame
    cv2.imshow('Paper thing', paperThing)
    cv2.imshow('THE EYE', frame)

    '''   if k%256 == 27: #ESC Pressed
        break'''
''' elif k == orb('g'):
        # SPACE pressed
        img_name = "facedetect_webcam_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()'''