import cv2 as cv
import numpy as np


# 逻辑与运算(遮罩)、或、非
def logic_demo(m1, m2):
    # dst = cv.bitwise_and(m1, m2)
    # dst = cv.bitwise_or(m1, m2)

    image = cv.imread("yuanyuan.jpg")
    dst = cv.bitwise_not(image)
    cv.imshow("logic_demo", dst)


# 对比度、亮度的调节
def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)  # 原图像、对比度、blank、1-对比度、亮度
    cv.imshow("contrast_brightness_demo", dst)


print("Hello")
src1 = cv.imread("yuanyuan.jpg")
src2 = cv.imread("apple.jpg")
# cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)

cv.imshow("image1", src1)
# cv.imshow("image2", src2)

contrast_brightness_demo(src1, 1.0, 0)  # 图像、对比度、亮度

# logic_demo(src1, src2)

cv.waitKey(0)
cv.destroyAllWindows()