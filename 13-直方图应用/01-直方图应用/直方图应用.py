import cv2 as cv
import numpy as np


# 全局直方图均衡化(增强图像对比度)
def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # opencv的直方图均衡化要基于单通道灰度图像
    dst = cv.equalizeHist(gray)  # 自动调整图像对比度，把图像变得更清晰
    cv.imshow("equalHist_demo", dst)


# 局部直方图均衡化
def calhe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # opencv的直方图均衡化要基于单通道灰度图像
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(3, 3))  # 对比度的大小  每次处理块的大小
    dst = clahe.apply(gray)  # 进行局部均衡化处理
    cv.imshow("calhe_demo", dst)


# 做一个RGB的直方图
def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16  # 降维(重点)
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1  # 相当于在x轴上加数据
        return rgbHist


# 比较函数
def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)  # 获取该图像的基本数据
    # print("hist1  %s" % hist1)
    hist2 = create_rgb_hist(image2)
    # print("hist2  %s" % hist2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离 : %s, 相关性 : %s, 卡方 : %s" % (match1, match2, match3))  # 图像越相近，巴氏距离越小、相关性越接近1、卡方很小


print("-----Hello-----")
image1 = cv.imread("yuanyuan1.jpg")
image2 = cv.imread("yuanyuan2.jpg")
# cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image1", image1)
# cv.imshow("input image2", image2)

# equalHist_demo(image1)
# calhe_demo(image1)
hist_compare(image1, image2)

cv.waitKey(0)
cv.destroyAllWindows()













