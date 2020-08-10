import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
person_name = input('Enter your Name : ')
face_data = []
skip = 0
dir_name = "./Data/"
offset = 10
while True:
    ret, frame = cap.read()
    if ret == False:
        continue
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    if(len(faces) == 0):
        continue
    faces = sorted(faces, key=lambda i: i[2]*i[3], reverse=True)
    for (x, y, w, h) in faces[-1:]:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_section = cv2.resize(face_section, (100, 100))
        skip += 1
        if skip % 10 == 0:
            face_data.append(face_section)
            print(len(face_data))
            print(type(face_data))
    cv2.imshow("Video Frame", frame)
    cv2.imshow("Face Framr", face_section)
    keyPressed = cv2.waitKey(1) & 0XFF
    if keyPressed == ord('q'):
        break
face_data = np.asarray(face_data)
print(face_data.shape)
face_data = np.reshape(face_data, (1, -1))
print(face_data.shape)
cap.release()
cv2.destroyAllWindows()
