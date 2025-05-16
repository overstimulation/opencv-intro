import cv2
import PySide6


def ex1():
    img = cv2.imread("yoko_taro.jpg")
    cv2.imshow("", img)
    cv2.waitKey(0)


def ex2():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        cv2.imshow("", frame)
        if cv2.waitKey(1) == ord("q"):
            break


def ex3():
    cv2.namedWindow("Camera")
    capture = cv2.VideoCapture(0)
    cv2.createTrackbar("Brightness", "Camera", 256, 256 * 2 - 1, lambda x: None)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        cv2.imshow("Camera", cv2.add(frame, cv2.getTrackbarPos("Brightness", "Camera") - 256))
        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    ex3()
