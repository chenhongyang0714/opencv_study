import cv2 as cv
import numpy as np


# 开操作(形态学操作基于二值图像)
def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 注意结构元素形状、大小   (返回指定大小和形状的结构元素，用于形态操作)
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # 开操作
    cv.imshow("open_demo", dst)


# 闭操作(形态学操作基于二值图像)
def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)  # 闭操作
    cv.imshow("close_demo", dst)


# 开操作(提取水平线)
def open_demo_1(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 1))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # 开操作
    cv.imshow("open_demo_1", dst)


# 开操作(提取竖直线)
def open_demo_2(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 15))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # 开操作
    cv.imshow("open_demo_2", dst)


# 开操作(除背景斜线、噪点)
def open_demo_3(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # 开操作
    cv.imshow("open_demo_3", dst)


# 开操作(提取圆形)
def open_demo_4(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # 开操作
    cv.imshow("open_demo_4", dst)


print("------Hello------")
src = cv.imread("example5.jpg")
cv.imshow("image", src)

open_demo_4(src)

cv.waitKey(0)
cv.destroyAllWindows()
