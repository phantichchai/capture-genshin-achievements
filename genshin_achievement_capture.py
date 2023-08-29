import numpy as np
import cv2 as cv
import time
import os

cap = cv.VideoCapture('Genshin_Impact_2023-08-29_12-34-20.mp4')
n = 0
frame_rate = 60
prev = 0
PATH = os.path.join("achievements", "resource")
IMAGE_TYPE = ".png"

while cap.isOpened():
    time_elapsed = time.time() - prev
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, threshold = cv.threshold(gray, 195, 255, cv.THRESH_BINARY)
    
    # using a findContours() function
    contours, _ = cv.findContours(
        threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # list for storing names of shapes
    for contour in contours:
        x,y,w,h = cv.boundingRect(contour)
        if 1000 < w < 1066 and 10 < h < 200:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            achievement = gray[y:y+h, x:x+w]

    cv.imshow('frame', frame)
    if time_elapsed > 1./frame_rate:
        prev = time.time()
        cv.imwrite(os.path.join(PATH, str(n) + IMAGE_TYPE), achievement)
        n += 1

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
