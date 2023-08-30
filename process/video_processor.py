import cv2
import tempfile
import os
import time

class VideoProcessor:
    def __init__(self, video_path):
        self.temp_folder = tempfile.TemporaryDirectory()
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.frame_rate = 60
        self.prev = time.time()
        self.n = 0
        self.temp_folder_path = self.temp_folder.name
        self.extension = ".png"

    def process_video(self):
        try:
            while self.cap.isOpened():
                time_elapsed = time.time() - self.prev
                ret, frame = self.cap.read()

                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                _, threshold = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)
                
                contours, _ = cv2.findContours(
                    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                relevant_frame = None
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    if 1000 < w < 1066 and 10 < h < 200:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
                        relevant_frame = gray[y:y+h, x:x+w]

                cv2.imshow('frame', frame)
                if time_elapsed > 1.0 / self.frame_rate and relevant_frame is not None:
                    self.prev = time.time()
                    frame_filename = f"{self.n:04d}{self.extension}"
                    frame_path = os.path.join(self.temp_folder_path, frame_filename)
                    cv2.imwrite(frame_path, relevant_frame)
                    self.n += 1

                if cv2.waitKey(1) == ord('q'):
                    break

        except Exception as e:
            print("An error occurred:", str(e))

        finally:
            self.cap.release()
            cv2.destroyAllWindows()

    def cleanup(self):
        self.temp_folder.cleanup()

# Example usage
if __name__ == "__main__":
    video_processor = VideoProcessor("input_video.mp4")
    video_processor.process_video()
