import cv2 as cv
import numpy as np


# 加法算法
def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add.demo", dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


# 除法算法
def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


# 求均值、方差   (若方差为零 则图像没有实际内容)
def others(m1, m2):
    # M1 = cv.mean(m1)  # 计算均值
    # M2 = cv.mean(m2)
    M1, dev1 = cv.meanStdDev(m1)  # 计算均值、方差
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]  # 取彩色图片的高、宽(切片)

    # print(h, w)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)

    # 数组都为 0 时的均值、方差
    img = np.zeros([h, w], np.uint8)  # 创建一个与m1等大的零数组(uint8是无符号八位整型)
    m, dev = cv.meanStdDev(img)  # 求取此数组的均值、方差
    print(m)
    print(dev)

    # 数组都为 1 时的均值、方差
    img = np.ones([400, 400], np.uint8)
    img = img * 127
    m, dev = cv.meanStdDev(img)  # 求取此数组的均值、方差
    print(m)
    print(dev)


print("----------Hello--------")
src1 = cv.imread("yuanyuan.jpg")
src2 = cv.imread("apple.jpg")
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)

# add_demo(src1, src2)
# subtract_demo(src1, src2)
# multiply_demo(src1, src2)
# divide_demo(src1, src2)

others(src1, src2)

cv.waitKey(0)
cv.destroyAllWindows()