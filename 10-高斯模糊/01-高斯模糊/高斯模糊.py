import cv2 as cv
import numpy as np


# 控制变化后b g r每个通道的值在0~255之间
def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


# 加上高斯噪声
def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)  # 生成 3个 高斯分布的概率密度随机数
            b = image[row, col, 0]  # blue  # 取出像素点每个通道的值
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])  # 将每个通道的值进行高斯变换(加噪)
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image", image)


print("----Hello------")
src = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

t1 = cv.getTickCount()  # 计算出高斯变换所需的时间
# gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
# print("time consume: %s" % (time*1000))  # 毫秒


# 高斯模糊API(可抑制高斯噪声)(保留图像的主要特征)
dst = cv.GaussianBlur(src, (0, 0), 2)  # (5, 5), 10 不需要都设置（x 与 σ）会通过一个计算出另一个
cv.imshow("Gaussian Blur", dst)

cv.waitKey(0)
cv.destroyAllWindows()
