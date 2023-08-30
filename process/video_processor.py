import cv2 as cv
import os
import time

class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv.VideoCapture(video_path)
        self.frame_rate = 60
        self.prev = 0
        self.n = 0
        self.PATH = os.path.join("achievements", "resource")
        self.IMAGE_TYPE = ".png"

    def capture_frames(self):
        while self.cap.isOpened():
            time_elapsed = time.time() - self.prev
            ret, frame = self.cap.read()

            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            _, threshold = cv.threshold(gray, 195, 255, cv.THRESH_BINARY)
            
            contours, _ = cv.findContours(
                threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

            achievement = None
            for contour in contours:
                x,y,w,h = cv.boundingRect(contour)
                if 1000 < w < 1066 and 10 < h < 200:
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
                    achievement = gray[y:y+h, x:x+w]

            cv.imshow('frame', frame)
            if time_elapsed > 1. / self.frame_rate and achievement is not None:
                self.prev = time.time()
                cv.imwrite(os.path.join(self.PATH, str(self.n) + self.IMAGE_TYPE), achievement)
                self.n += 1

            if cv.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv.destroyAllWindows()
