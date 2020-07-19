# -*- encoding: UTF-8 -*-

import cv2 as cv
import numpy as np


# Canny 边缘提取(对噪声敏感)
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)  # 降低噪声
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

    # x Grodient
    # xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # y Grodient
    # ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)  # 通过 x、y梯度 计算Canny
    edge_output = cv.Canny(gray, 50, 150)  # 不用 x、y梯度
    cv.imshow("Canny Edge", edge_output)

    # 将提取的边缘 用彩色显示出来
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("Color Edge", dst)


print("-------Hello World----------")
src = cv.imread("example.jpg")
cv.imshow("example", src)

edge_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()