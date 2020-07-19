# -*- encoding: UTF-8 -*-
import cv2 as cv
import numpy as np


# 对象测量
def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 图形二值化
    # print("threshold value: %s" % ret)  # 阈值
    # cv.imshow("binary image", binary)  # 显示二值图像
    cloneImage, contours, heriachy, = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 图形轮廓查找
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)  # 轮廓面积
        print("contourArea is : %s" % area)
        x, y, w, h = cv.boundingRect(contour)  # 计算轮廓的垂直边界最小矩形
        rate = min(w, h) / max(w, h)  # 计算出矩形的宽高比
        print("rectangle rate", rate)
        mm = cv.moments(contour)  # 几何矩
        # print(type(mm))  字典型
        cx = mm['m10'] / mm['m00']  # 利用几何矩求取重心坐标
        cy = mm['m01'] / mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)  # 绘制出重心坐标
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)  # 绘制矩形
    cv.imshow("measure_object", image)


# 多边形逼近(在灰度图像上绘制)
def measure_object_1(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 图形二值化
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    cloneImage, contours, heriachy, = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 图形轮廓查找
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)  # 轮廓面积
        print("contourArea is : %s" % area)
        x, y, w, h = cv.boundingRect(contour)  # 计算轮廓的垂直边界最小矩形
        rate = min(w, h) / max(w, h)  # 计算出矩形的宽高比
        print("rectangle rate", rate)
        mm = cv.moments(contour)  # 几何矩
        # print(type(mm))  字典型
        cx = mm['m10'] / mm['m00']  # 利用几何矩求取重心坐标
        cy = mm['m01'] / mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)  # 绘制出重心坐标
        # cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)  # 绘制矩形x
        approxCurve = cv.approxPolyDP(contour, 4, True)  # 多边形逼近
        # print(approxCurve.shape)
        if approxCurve.shape[0] > 6:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)  # 绘制轮廓
        if approxCurve.shape[0] == 4:  # 检测矩形
            cv.drawContours(dst, contours, i, (255, 0, 0), 2)  # 绘制轮廓
        if approxCurve.shape[0] == 3:  # 检测三角形
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)  # 绘制轮廓
    cv.imshow("measure_object", dst)


print("------Hello------")
src = cv.imread("example2.jpg")
cv.imshow("image", src)

measure_object_1(src)

cv.waitKey(0)
cv.destroyAllWindows()