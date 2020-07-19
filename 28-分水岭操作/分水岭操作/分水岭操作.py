import cv2 as cv
import numpy as np


# 分水岭操作
# 分水岭分割流程：图像->灰度->二值->距离变换->寻找种子->生成Marker->分水岭变换->输出
def watershed_demo():
    # remove noise if any
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)  # 均值偏移滤波  空间窗的半径、色彩窗的半径
    # gray \ binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 图像二值化
    cv.imshow("binary image", binary)

    # morphologyEx operation 形态学操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 结构元素
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)  # 开操作  迭代次数
    sure_bg = cv.dilate(mb, kernel, iterations=3)  # 腐蚀次数
    cv.imshow("sure_bg image", sure_bg)

    # distance transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)  # 距离变换函数, 3 : 距离变换掩码矩阵的大小
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)  # 归一化数据
    cv.imshow("distance_t", dist_output*50)

    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)  # 图像二值化
    cv.imshow("surface_bin", surface)

    # find maskers
    surface_fg = np.uint8(surface)

    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)  # 设置种子
    print(ret)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 255, 255]
    cv.imshow("result", src)


print("------Hello------")
src = cv.imread("example.jpg")
cv.imshow("image", src)

watershed_demo()

cv.waitKey(0)
cv.destroyAllWindows()
