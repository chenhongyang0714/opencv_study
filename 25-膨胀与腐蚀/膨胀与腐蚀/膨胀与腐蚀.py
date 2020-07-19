import cv2 as cv
import numpy as np


# 腐蚀(灰度图像)
def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 图像二值化
    cv.imshow("binary image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))  # 得到一个结构元素
    dst = cv.erode(binary, kernel)  # 腐蚀
    cv.imshow("erode_demo", dst)


# 膨胀(灰度图像)
def Swell_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 图像二值化
    cv.imshow("binary image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))  # 得到一个结构元素
    dst = cv.dilate(binary, kernel)  # 膨胀
    cv.imshow("Swell_demo", dst)


# 腐蚀(彩色图像)
def color_erode_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))  # 得到一个结构元素
    dst = cv.erode(image, kernel)  # 腐蚀
    cv.imshow("color_erode_demo", dst)


# 膨胀(彩色图像)
def color_Swell_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))  # 得到一个结构元素
    dst = cv.dilate(image, kernel)  # 膨胀
    cv.imshow("color_Swell_demo", dst)


print("------Hello------")
src = cv.imread("yuanyuan.jpg")
cv.imshow("image", src)

color_erode_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()