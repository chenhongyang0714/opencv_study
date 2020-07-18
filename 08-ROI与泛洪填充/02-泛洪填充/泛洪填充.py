import cv2 as cv
import numpy as np


# 彩色图像的填充(泛洪填充)   cv.FLOODFILL_FIXED_RANGE
def fill_color_demo(image):
    copyImg = image.copy()  # 拷贝图像
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)  # 操作掩码
    # 从起始像素点(30,30)起，填充黄色(（30,30）处的像素值分别减去(100, 100, 100)得到最小值，分别加上(50, 50, 50)得到最大值，如果连续处的像素值在此区域)
    cv.floodFill(copyImg, mask, (100, 100), (0, 0, 255), (100, 100, 100), (60, 60, 60), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyImg)


# 二值图像的填充  cv.FLOODFILL_MASK_ONLY
def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)  # 创建一个数组(黑色填充)
    image[100:300, 100:300, :] = 255  # 所有通道(填充白)
    cv.imshow("fill_binary", image)

    mask = np.ones([402, 402, 1], np.uint8)  # 必须为单通道(黑色填充)    # 注意此处的ones
    mask[101:301, 101:301] = 0  # (白色填充)                            # 注意此处的0     至关重要
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)  # 把白色的矩形块填充为红色
    cv.imshow("filled_binary", image)


print("-----Hello-----")
src = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

fill_color_demo(src)
# fill_binary()

cv.waitKey(0)
cv.destroyAllWindows()