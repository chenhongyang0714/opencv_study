import cv2 as cv


# 色彩的相互转换
def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 转化成灰度空间
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb", Ycrcb)


print("-------Hello World----------")
src = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

color_space_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
