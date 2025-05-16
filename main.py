import cv2
import PySide6


def ex1():
    img = cv2.imread("yoko_taro.jpg")
    cv2.imshow("", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    ex1()
