import cv2 as cv
from matplotlib import pyplot as plt


# 直方图反向衍射(反向投影)
def back_projection_demo():
    sample = cv.imread("sample1.jpg")
    target = cv.imread("target1.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show image
    cv.imshow("sample_hsv", sample)
    cv.imshow("target_hsv", target)

    # 对 sample 图像进行处理
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [8, 8], [0, 180, 0, 256])  # 制作sample的2d直方图
    cv.normalize(roiHist, roiHist, 255, 0, cv.NORM_MINMAX)  # 归一化数据

    # 对 target 图像进行处理
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)  # 反向投影
    cv.imshow("back_projection_demo", dst)


# 设计2D直方图
def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0, 1], None, [140, 180], [0, 180, 0, 256])  # 计算出2d直方图
    plt.imshow(hist, interpolation="nearest")  # 负责对图像进行处理，并显示其格式(临近点差值)
    plt.title("2D Hist")  # 标题
    plt.show()  # 将plt.imshow()处理后的函数图显示出来


print("-----Hello-----")
src = cv.imread("target.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)

# hist2d_demo(src)
# back_projection_demo()

cv.waitKey(0)
cv.destroyAllWindow()
