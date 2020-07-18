import cv2 as cv
import numpy as np


# 读取视频(色彩筛选)
def extrace_object_demo():
    capture = cv.VideoCapture("aiqing.mp4")  # 读取视频
    while True:
        ret, frame = capture.read()  # 布尔值 帧值
        if ret == False:  # 如果都读取到最后一帧
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # 将每一个帧值转化成HSV
        lower_hsv = np.array([0, 0, 0])  # 选取将要过滤的色彩的范围
        upper_hsv = np.array([180, 255, 46])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)  # 得到一个二值化图像(筛选)

        dst = cv.bitwise_and(frame, frame, mask=mask)  # 将提取出的颜色显示出来

        # cv.imshow("video", frame)
        # cv.imshow("mask", mask)
        cv.imshow("dst", dst)
        c = cv.waitKey(40)  # 等待键盘的输入
        if c == 27:  # 如果键盘按压的键是“esc”
            break


print("-------Hello World----------")
src = cv.imread("yuanyuan.jpg")
cv.imshow("yuan", src)

extrace_object_demo()

# # 通道的分离
b, g, r = cv.split(src)  # 将图像分离
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)

# # 通道的合并
src = cv.merge([b, g, r])  # 将三通道图片合并
src[:, :, 2] = 0  # 将第三个通道的红色弄没了
# cv.imshow("changed image", src)


cv.waitKey(0)
cv.destroyAllWindows()
