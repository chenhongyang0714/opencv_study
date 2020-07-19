import cv2 as cv
import numpy as np


# 霍夫直线检测(基于图像边缘检测)(通过坐标之间的转化求得)(画直线)
def line_detestion_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # Sobel 算子内核大小
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)  # (累加平面的阈值参数) 返回 极坐标系下的角度、长度
    for line in lines:
        print(type(line))
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 + 1000 * (-b))  # 计算直线上两点坐标(源码求法)
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("image_lines", image)


# 霍夫直线检测(基于图像边缘检测)(直接调用API求得)(常用)(画线段)
def line_detect_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # Sobel 算子内核大小
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 75, minLineLength=20, maxLineGap=5)
    for line in lines:
        print(type(line))
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_detect_demo", image)


print("--------Hello-----------")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
src = cv.imread("250.jpg")
cv.imshow("image", src)

line_detect_possible_demo(src)

cv.waitKey(0)
cv.destroyAllWindow()