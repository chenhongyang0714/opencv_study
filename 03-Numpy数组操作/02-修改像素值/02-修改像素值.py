import cv2 as cv
import numpy as np


def access_pixels(image):  # 访问像素
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]  # 通道数
    print("width:%s, height:%s, channels:%s" % (width, height, channels))

    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def inverse(image): 
    dst = cv.bitwise_not(image)  # 非
    cv.imshow("inverse demo", dst)


def create_image():

    # # 多通道操作
    # img = np.zeros([400, 400, 3], np.uint8)  # 返回一个给定形状和类型的用0填充的数组
    # img[ : , : , 0 ] = np.ones([400, 400]) * 255  # 将第一个通道(0) 变色
    # img[ : , : , 2 ] = np.ones([400, 400]) * 255
    # cv.imshow("new image", img)

    # 单通道操作
    # img = np.zeros([400, 400, 1], np.uint8)
    # img[ : , : , 0 ] = np.ones([400, 400]) * 127
    # cv.imshow("new image", img)
    # 或者
    # img = np.ones([400, 400, 1], np.uint8)
    # img = img * 127
    # cv.imshow("new image", img)
    # cv.imwrite() # 保存

    # 创建数组(1)(二维)
    m1 = np.ones([3, 3], np.uint8)
    m1.fill(20)
    cv.convertScaleAbs(m1)  # https://blog.csdn.net/guduruyu/article/details/81605726  用于图像增强
    print(m1)

    # 不同维度数组之间的转化
    m2 = m1.reshape([1, 9])  # 转化为一行九列
    print(m2)

    # 创建数组(2)
    m3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # m3.fill(9)
    # print(m3)


scr = cv.imread("yuanyuan.jpg")  # blue green red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", scr)

t1 = cv.getTickCount()
# access_pixels(scr)  # 像素取反(自己敲的代码)
create_image()  # 创建多维数组
# inverse(scr)  # 像素取反(官方代码)
t2 = cv.getTickCount()  # 用于返回从操作系统启动到当前所经的计时周期数
time = (t2 - t1) / cv.getTickFrequency()  # 用于返回CPU的频率  这里的单位是秒，也就是一秒内重复的次数
print("time : %s ms" % (time * 1000))

cv.waitKey(0)
cv.destroyAllWindows()