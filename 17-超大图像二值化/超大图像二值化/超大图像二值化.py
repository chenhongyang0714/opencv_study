import cv2 as cv
import numpy as np


# 分块求图像二值化(全局阀值)
def big_image_binary(image):
    # print(image.shape)
    cw = 256  # 确定 小块 的宽、高
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 注意返回两个参数
            gray[row:row + ch, col:col + cw] = dst
            print(np.std(dst), np.mean(dst))  # 求取每一小块矩阵 的标准差、均值
    cv.imwrite("QuanJu1.jpg", gray)


# 分块求图像二值化(局部阀值)(优)
def local_image_binary(image):
    # print(image.shape)
    cw = 256  # 确定 小块 的宽、高
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 127, 10)  # 注意返回一个参数
            gray[row:row + ch, col:col + cw] = dst
            print(np.std(dst), np.mean(dst))  # 求取每一小块矩阵 的标准差、均值
    cv.imwrite("JuBu2.jpg", gray)


# 分块求图像二值化(全局阀值)(方差小于某个值时，统一一个颜色)
def local_image_binary_1(image):
    # print(image.shape)
    cw = 256  # 确定 小块 的宽、高
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            print(np.std(roi), np.mean(roi))  # 求取每一小块矩阵 的标准差、均值
            if np.std(roi) < 15:
                gray[row:row + ch, col:col + cw] = 255
            else:
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row + ch, col:col + cw] = dst
    cv.imwrite("example1.jpg", gray)


print("-----------Python OpenCv Study--------------")
src = cv.imread("example.jpg")

# big_image_binary(src)
local_image_binary_1(src)

cv.waitKey(0)
cv.destroyAllWindow()
