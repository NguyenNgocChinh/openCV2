import cv2

camera_id = 0
video = cv2.VideoCapture(camera_id)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def save_face(image, faces):
    i = 0
    for (x, y, w, h) in faces:
        i += 1
        crop = image[y: y+h, x: x+w]
        cv2.imwrite('img{}.png'.format(i), crop)
while True:
    ret, img = video.read()

    if ret:
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_image, 1.2, 10, minSize=(100, 100))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Camera', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        save_face(img, faces)

video.release()
cv2.destroyAllWindows()