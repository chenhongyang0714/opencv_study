import cv2 as cv

scr = cv.imread("yuanyuan.jpg")  # 读取一张图片
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)  # 创建一个GUI用于将图片显示出来
cv.imshow("image", scr)
cv.waitKey(0)  # 暂停图像、等待键盘输入，频率时间为delay，单位为ms
cv.destroyAllWindows()  # 销毁所有已打开的GUI窗口
