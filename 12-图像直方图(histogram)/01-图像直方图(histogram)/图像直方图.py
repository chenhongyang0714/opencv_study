import cv2 as cv
from matplotlib import pyplot as plt


# 直方图(反应图像的主要特征)
def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])  # 把像素出现的所有频次统计出来   Bins直方图的柱数   Range
    plt.show()


# 构造曲线图(三通道)
def image_hist(image):
    color = ('blue', 'green', 'red')  # 这里画笔颜色的值可以为大写或小写或只写首字母或大小写混合
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])  # 计算2d直方图   Mask  Bins  Range
        plt.plot(hist, color=color)  # 做出图
        plt.xlim([0, 256])  # 设置x坐标轴范围
        plt.title("Tittle")  # 图像的标题
        plt.xlabel("Bins")  # X轴标签
        plt.ylabel("# of Pixels")  # Y轴标签
    plt.show()  # 显示图像


print("----Hello World-----")
src = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# plot_demo(src)
image_hist(src)

cv.waitKey(0)
cv.destroyAllWindow()


