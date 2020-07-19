import cv2 as cv
import numpy as np


# 顶帽(灰度图像)
def top_hat_gray_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)  # 顶帽操作
    cimage= np.array(gray.shape, np.uint8)
    cimage = 100
    dst = cv.add(dst, cimage)  # 利用数组 增加 顶帽 之后的图像亮度
    cv.imshow("top_hat_gray_demo", dst)


# 黑帽(灰度图像)
def black_hat_gray_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)  # 黑帽操作
    cimage= np.array(gray.shape, np.uint8)
    cimage = 120
    dst = cv.add(dst, cimage)  # 增加 黑帽 之后的图像亮度
    cv.imshow("black_hat_gray_demo", dst)


# 顶帽(二值图像)
def top_hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_TOPHAT, kernel)  # 顶帽操作
    cv.imshow("top_hat_binary_demo", dst)


# 黑帽(二值图像)
def black_hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)  # 黑帽操作
    cv.imshow("black_hat_binary_demo", dst)


# 基本梯度(二值图像)(相当于提取边框)
def black_ladder_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 注意结构元素形状、大小
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)  # 黑帽操作
    cv.imshow("black_ladder_binary_demo", dst)


# 内部梯度、外部梯度
def demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 注意结构元素形状、大小
    dm = cv.dilate(image, kernel)  # 膨胀
    em = cv.erode(image, kernel)  # 腐蚀
    dst1 = cv.subtract(image, em)  # interial gradient
    dst2 = cv.subtract(dm, image)  # exterial gradient
    cv.imshow("interial", dst1)
    cv.imshow("exterial", dst2)


print("------Hello------")
src = cv.imread("example2.jpg")
cv.imshow("image", src)

black_ladder_binary_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
