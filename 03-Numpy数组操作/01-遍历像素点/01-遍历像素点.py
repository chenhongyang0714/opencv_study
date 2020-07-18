# -*- coding: UTF-8 -*-
import cv2 as cv
import numpy as np


def access_pixels(image):  # 访问像素
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]  # 通道数
    print("width:%d, height:%d, channels:%d" % (width, height, channels))

    for row in range(height):
        for col in range(width):
            # print(image[row, 200])
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


scr = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", scr)

t1 = cv.getTickCount()

access_pixels(scr)

t2 = cv.getTickCount()  # 用于返回从操作系统启动到当前所经的计时周期数
time = (t2 - t1) / cv.getTickFrequency()  # 用于返回CPU的频率  这里的单位是秒，也就是一秒内重复的次数
print("time : %s ms" % (time * 1000))

cv.waitKey(0)
cv.destroyAllWindows()
