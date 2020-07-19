import cv2 as cv
import numpy as np


# 全局阈值
# 图形二值化(黑白图像)(阈值通过计算求出)
def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 根据阈值进行二值化、自动计算阈值的方法
    print("threshold value : %s" % ret)                                          # cv.THRESH_TRIANGLE应用于直方图仅有单个波峰
    cv.imshow("binary", binary)


# 全局阈值
# 图形二值化(黑白图像)(阈值自定义)
def threshold_demo2(image):
    gray = cv.cvtColor(image, cv.THRESH_TRUNC)
    ret, binary = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)  # cv.THRESH_BINARY_INV大于阈值的是黑色、cv.THRESH_BINARY(常用)大于阈值的是白色
    print("threshold value : %s" % ret)                           # cv.THRESH_TRUNC大于阈值的变成零、cv.THRESH_TOZERO小于阈值的变成零
    cv.imshow("binary", binary)


# 局部阈值
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,  25, 10)
    cv.imshow("local_threshold", binary)


# 局部阈值(自己计算阀值:平均值)
def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    # m = np.reshape(gray, [1, w*h])
    mean = gray.sum() / (w*h)  # 实际为全部像素点的平均值
    print("mean", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    print("custom_threshold : %s" % ret)
    cv.imshow("binary", binary)


print("------------Hello World------------")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
src = cv.imread("yuanyuan.jpg")
cv.imshow("image", src)

local_threshold(src)

cv.waitKey(0)
cv.destroyAllWindow()