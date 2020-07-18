import cv2 as cv
import numpy as np

print("----Hello----")
src = cv.imread("yuanyuan.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# 进行face  ROI 的选取
face = src[60:350, 200:600]  # 高、宽
# 对截取的face进行gray操作  不会影响原图片的颜色
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
# 对进行gray后的图片还原为原来的三通道RGB
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)  # 还原为RGB三通道的图像(如果不还原，则无法添加到原图像中)
src[60:350, 200:600] = backface
cv.imshow("face", src)


cv.waitKey(0)
cv.destroyAllWindows()
