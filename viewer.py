import cv2
import numpy as np


class Viewer:
    def __init__(self, initial_value, max_value):
        cv2.namedWindow("Camera")
        self.capture = cv2.VideoCapture(0)
        cv2.createTrackbar("Slider", "Camera", 256, 256 * 2 - 1, lambda x: None)

    def get_trackbar_pos(self):
        return cv2.getTrackbarPos("Slider", "Camera")

    def process_frame(self, frame, trackbar_pos):
        return frame

    def run(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            trackbar_pos = self.get_trackbar_pos()
            frame = self.process_frame(frame, trackbar_pos)
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) == ord("q"):
                break


class BrightnessViewer(Viewer):
    def __init__(self):
        super().__init__(256, 256 * 2 - 1)

    def get_trackbar_pos(self):
        return super().get_trackbar_pos() - 256

    def process_frame(self, frame, trackbar_pos):
        return cv2.add(frame, trackbar_pos)


class BlurViewer(Viewer):
    def __init__(self):
        super().__init__(1, 300)

    def get_trackbar_pos(self):
        return super().get_trackbar_pos() * 2 + 1
        # self.kernel = np.ones((pos,pos),np.float32)/pos**2
        # self.kernel = cv2.getGaussianKernel(pos,-1)

    def process_frame(self, frame, trackbar_pos):
        return cv2.GaussianBlur(frame, (trackbar_pos, trackbar_pos), 0)
        # return cv2.filter2D(frame,-1,self.kernel)
