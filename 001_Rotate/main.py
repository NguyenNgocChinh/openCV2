import cv2
import imutils

camera_id = 0

video = cv2.VideoCapture(camera_id)

rotate = 0
while True:
    ret, frame = video.read()
    if ret:
        if rotate != 0:
            frame = imutils.rotate(frame, rotate)
        cv2.imshow('Can Rotate', frame)
    key_press = cv2.waitKey(1)

    if key_press == ord('q'):
        break
    elif key_press == ord('a'):
        rotate = 90
    elif key_press == ord('d'):
        rotate = -90
