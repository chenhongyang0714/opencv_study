# -*- coding:utf-8 -*-
import cv2 as cv


# 轮廓发现(通过 cv.Canny 获取边缘检测图像 传入 cv.findContours )
def edge_dem_contours(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)  # 高斯降低噪声
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

    # x Grodient
    # xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # y Grodient
    # ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)  # 通过 x、y梯度 计算Canny
    edge_output = cv.Canny(gray, 50, 100)  # 不用 x、y梯度
    cv.imshow("Canny Edge", edge_output)

    cloneImage, contours, heriachy, = cv.findContours(edge_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        # cv.drawContours(image, contours, i, (0, 0, 255), 2)
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print(i)
    cv.imshow("edge_dem_contours", image)


# 轮廓发现(通过 cv.threshold 获取二值图像 传入 cv.findContours )
def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)  # 0 :高斯核在x方向的标准差
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 图形二值化
    cv.imshow("binary image", binary)

    cloneImage, contours, heriachy, = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        # cv.drawContours(image, contours, i, (0, 0, 255), 2)
        cv.drawContours(image, contours, i, (0, 0, 255), -1)  # 填充整个轮廓
        print(i)
    cv.imshow("detect contours", image)


print("------Hello------")
src = cv.imread("example.jpg")
cv.imshow("image", src)

contours_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()