import cv2 as cv
import numpy as np


# 高斯金字塔 reduce
def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)  # 将采样 reduce = 高斯模糊+将采样
        pyramid_images.append(dst)
        cv.imshow("pyramid_demo"+np.str(i), dst)
        temp = dst.copy()
    return pyramid_images


# 拉普拉斯金字塔
def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        if (i-1) < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])  # 还原的图像  需要还原的大小
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_down"+str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lapalian_down" + str(i), lpls)


print("---------Hello------------")
src = cv.imread("example1.jpg")
cv.imshow("image", src)

pyramid_demo(src)

cv.waitKey(0)
cv.destroyAllWindow()