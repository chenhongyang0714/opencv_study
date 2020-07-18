import cv2 as cv
import numpy as np


# 均值模糊(对随机噪声有很好的去噪效果)
def blur_demo(image):
    dst = cv.blur(image, (5, 5))  # 横向模糊、纵向模糊程度
    cv.imshow("blur_demo", dst)


# 中值模糊(去除椒盐噪声)
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)


# 自定义模糊
def custom_blur_demo(image):
    # 自定义模糊
    # kernel = np.ones([5, 5], np.float32)/25

    # 锐化(增强图像立体感)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 注意：此处不用 除9
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("custom_blur_demo", dst)


print("Hello")
src = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# blur_demo(src)
median_blur_demo(src)
# custom_blur_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()