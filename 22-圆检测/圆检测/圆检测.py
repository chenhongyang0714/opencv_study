# -*- encoding: UTF-8 -*-

import cv2 as cv
import numpy as np


# 霍夫圆检测
def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)  # (中值滤波)空间窗的半径  色彩窗的半径
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)  # OneNote

    # print(f"circles1:{circles}")
    # print(f"circles:{str(type(circles))}")

    circles = circles[0, :, :]  # 降一个维度
    # print(f"circles2:{circles}")
    circles = np.around(circles)
    print(f"circles3:{circles}")
    circles = np.uint16(np.around(circles))
    print(f"circles4:{circles}")
    # print(f"circles3:{circles[0][0]}")
    # print(f"circles3:{circles[0][1]}")

    # circles = np.uint16(np.around(circles))  # 返回四舍五入后的值
    # for i in circles[0, :]:  # 找多个圆
    #     cv.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 画 圆
    #     cv.circle(image, (i[0], i[1]), 1, (255, 255, 0), 2)  # 画 圆心
    # cv.imshow("circles", image)


print("-----Hello World-----")
src = cv.imread("example.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)


detect_circles_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
