import cv2 as cv


# 高斯双边模糊
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)  # sigmaColor一般取大一点，让小的差异模糊掉   sigmaSpace一般取小一点，计算量会少
    cv.imshow("bi_demo", dst)


# 均值迁移滤波(油画的效果)
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 5, 50)  # 空间窗的半径  色彩窗的半径
    cv.imshow("shift_demo", dst)


print("-----Hello World-----")
src = cv.imread("example.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

bi_demo(src)
# shift_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
