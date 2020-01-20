import cv2

# reference the tutorial !!!!!!!!!!!!!!!!! https://towardsdatascience.com/https-medium-com-dilan-jay-face-detection-model-on-webcam-using-python-72b382699ee9

video_capture = cv2.VideoCapture(0)

img_counter = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    k = cv2.waitKey(1)

    # Display the resulting frame
    # cv2.imshow(window_name, image)
    cv2.imshow('Windowname', frame)

    if k % 256 == 27:  # ESC Pressed
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "facedetect_webcam_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()