import cv2 as cv
import numpy as np


# Sobel 算子
def sobel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)  # x方向 梯度
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x", gradx)
    cv.imshow("gradient_y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)  # 图片融合
    cv.imshow("gradient", gradxy)


# Scharr 算子 -> Sobel 算子 的增强版
def scharr_demo(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)  # x方向 梯度
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x", gradx)
    cv.imshow("gradient_y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)  # 图片融合
    cv.imshow("gradient", gradxy)


# 拉普拉斯算子(API)
def lapalian_demo(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo", lpls)


# 拉普拉斯算子(自定义)
def lapalian_demo_self(image):
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])  # 拉普拉斯算子
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)  # 利用内核实现对图像的卷积运算
    lpls = cv.convertScaleAbs(dst)  # 变成一个单通道8位的、0～255 的一个图像
    cv.imshow("lapalian_demo_self", lpls)


print("-------Hello World----------")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
src = cv.imread("example.jpg")
cv.imshow("image", src)

scharr_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()